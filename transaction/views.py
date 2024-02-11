from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated
from .serializers import FixedDepositViewSerializer, LoanDetailViewSerializer, OnlineTransactionViewSerializer, UpiTransactionViewSerializer, LoanDetailViewSingleSerializer
from .models import FixedDeposit, LoanDetail, OnlineTransaction, UpiTransaction
from account.models import User, UserProfile
from decimal import Decimal
from datetime import datetime, timedelta
from .utils import add_amount, subtract_amount
from account.permissions import IsOwnerOrReadOnly
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import generate_unique_transaction_number

class UpiTransactionView(GenericAPIView, ListModelMixin):
    def get_queryset(self):
        user = self.request.user
        return UpiTransaction.objects.filter(user=user)
    serializer_class = UpiTransactionViewSerializer

    permission_classes = IsAuthenticated,

    def get(self, request):
        return self.list(request)

    def post(self, request):
        data = request.data
        serializer = UpiTransactionViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # checking if the entered upi id is correct or incorrect
        if not (UserProfile.objects.filter(upi_id = serializer.validated_data['upi_id'])):
            raise ValidationError('Invalid Upi ID')
        
        # checking if the user has balance to make transaction
        myuser = UserProfile.objects.filter(user = self.request.user)
        my_balance = myuser.values()[0]['balance']
        if Decimal(my_balance) < serializer.validated_data['amount']:
            raise ValidationError('Your balance is low to make this trasaction')
        
        instance1, instance2 = serializer.save(user = self.request.user)

        # Obtaining the user who has received the amount
        amount_receiver = UserProfile.objects.filter(upi_id = serializer.validated_data['upi_id']).values()[0]['user_id']
        
        # Assigning the receiver transaction
        instance2.user = User.objects.filter(id = amount_receiver)[0]
        instance2.save()
        
        # Obtaining the sender
        amount_sender = myuser.values()[0]['user_id']
        
        # getting the transactions performed in both sender and receiver
        subtract_amount(amount_sender, serializer.validated_data['amount'])
        add_amount(amount_receiver, serializer.validated_data['amount'])
        return Response({"instance1": UpiTransactionViewSerializer(instance1).data, "instance2": UpiTransactionViewSerializer(instance2).data})

class OnlineTransactionView(GenericAPIView, ListModelMixin):
    def get_queryset(self):
        user = self.request.user
        return OnlineTransaction.objects.filter(user=user)
    
    serializer_class = OnlineTransactionViewSerializer

    permission_classes = IsAuthenticated,

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        data = request.data
        serializer = OnlineTransactionViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # checking if the user has balance to make transaction
        sender = UserProfile.objects.filter(user = self.request.user)
        my_balance = sender.values()[0]['balance']
        if Decimal(my_balance) < serializer.validated_data['amount']:
            raise ValidationError('Your balance is low to make this trasaction')
        

        # checking if the entered account number and ifsc is correct or incorrect
        receiver_user = UserProfile.objects.filter(account_number = serializer.validated_data['account_number'])
        if not receiver_user:
            raise ValidationError('Invalid Account Number')
        if not receiver_user.values()[0]['ifsc_code'] == serializer.validated_data['ifsc_code']:
            raise ValidationError('Invalid IFSC')
        

        subtract_amount(sender.values()[0]['user_id'], serializer.validated_data['amount'])
        add_amount(receiver_user.values()[0]['user_id'], serializer.validated_data['amount'])
        
        instance1, instance2 = serializer.save(user = self.request.user)
        instance2.user = User.objects.get(id = receiver_user[0].user_id)
        instance2.save()
        return Response({"instance1": OnlineTransactionViewSerializer(instance1).data, "instance2": OnlineTransactionViewSerializer(instance2).data})
    
class LoanDetailView(GenericAPIView, ListModelMixin):

    def get_queryset(self):
        user = self.request.user
        user_type = UserProfile.objects.get(user_id = user).account_holder_type
        if user_type == 'S':
            return LoanDetail.objects.all()
        else:
            return LoanDetail.objects.filter(user=user)
    serializer_class = LoanDetailViewSerializer

    permission_classes = IsAuthenticated,

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        data = request.data
        serializer = LoanDetailViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data)
    
class LoanDetailSingleView(GenericAPIView, UpdateModelMixin, ListModelMixin):
    def get_queryset(self):
        user = self.request.user
        user_type = UserProfile.objects.get(user_id = user).account_holder_type
        if user_type == 'S':
            return FixedDeposit.objects.all()
    
    serializer_class = LoanDetailViewSingleSerializer

    def get(self, request, pk):
        return self.list(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)
    


def approve_loan(sender, instance, created, **kwargs):
    if (instance.is_approved == True) and (instance.always_yes_because_of_signals == False):
        loan_user = LoanDetail.objects.get(user = instance.user)
        loan_user.loan_account_number = generate_unique_transaction_number()
        loan_user.start_date = datetime.now().date()
        loan_year_tenure = int(instance.tenure)
        loan_year = datetime.now().date() + timedelta(days=loan_year_tenure*365)
        loan_user.end_date = loan_year
        loan_user.always_yes_because_of_signals = True
        loan_user.loan_active = True
        add_amount(User.objects.get(email = instance.user), instance.amount)
        loan_user.save()

post_save.connect(approve_loan, sender=LoanDetail)

class FixedDepositView(GenericAPIView, ListModelMixin):
    def get_queryset(self):
        user = self.request.user
        user_type = UserProfile.objects.get(user_id = user).account_holder_type
        if user_type == 'S':
            return FixedDeposit.objects.all()
        else:
            return FixedDeposit.objects.filter(user=user)
    serializer_class = FixedDepositViewSerializer

    permission_classes = IsAuthenticated,

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        data = request.data
        serializer = FixedDepositViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # checking if the user has balance to make transaction
        sender = UserProfile.objects.filter(user = self.request.user)
        my_balance = sender.values()[0]['balance']
        if Decimal(my_balance) < serializer.validated_data['amount']:
            raise ValidationError('Your balance is low to make this trasaction')
        serializer.save(user=self.request.user)
        my_user = User.objects.filter(email=self.request.user).values()[0]['id']
        subtract_amount(my_user, serializer.validated_data['amount'])
        return Response(serializer.data)