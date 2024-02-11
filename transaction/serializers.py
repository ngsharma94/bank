from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import FixedDeposit, LoanDetail, OnlineTransaction, UpiTransaction
from .utils import generate_unique_transaction_number
from decimal import Decimal
from datetime import datetime, timedelta


class FixedDepositViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    fixed_deposit_number = serializers.CharField(read_only=True)
    interest = serializers.CharField(read_only=True)
    maturity_amount = serializers.DecimalField(max_digits=25, decimal_places=2, read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    class Meta:
        model = FixedDeposit
        fields = ['amount', 'interest', 'maturity_amount', 'fixed_deposit_number', 'start_date', 'end_date', 'tenure', 'user']
    def create(self, validated_data):
        validated_data['interest'] = '5%'
        interest = Decimal(validated_data['amount']) * Decimal(0.05)
        validated_data['maturity_amount'] = Decimal(validated_data['amount']) + Decimal(interest)
        validated_data['fixed_deposit_number'] = generate_unique_transaction_number()
        validated_data['start_date'] = datetime.now().date()
        loan_year_tenure = int(validated_data['tenure'])
        validated_data['end_date'] = datetime.now().date() + timedelta(days=loan_year_tenure*365)
        return super().create(validated_data)

class LoanDetailViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    loan_account_number = serializers.CharField(max_length=255, read_only=True)
    is_approved = serializers.BooleanField(default=False, read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    loan_active = serializers.BooleanField(default=False, read_only=True)
    class Meta:
        model = LoanDetail
        fields = ['id', 'loan_account_number', 'amount', 'start_date', 'end_date', 'tenure', 'loan_active', 'is_approved', 'user']
    

class OnlineTransactionViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    transaction_number = serializers.CharField(max_length=255, read_only = True)
    transaction_type = serializers.CharField(max_length=255, read_only = True)
    class Meta:
        model = OnlineTransaction
        fields = ['amount', 'account_number', 'ifsc_code', 'name', 'transaction_type', 'transaction_number', 'user']
    def create(self, validated_data):
        validated_data['transaction_type'] = 'D'
        validated_data['transaction_number'] = generate_unique_transaction_number()
        instance1 = OnlineTransaction.objects.create(**validated_data)
        validated_data['transaction_type'] = 'C'
        instance2 = OnlineTransaction.objects.create(**validated_data)
        return instance1, instance2

class UpiTransactionViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    transaction_number = serializers.CharField(max_length=255, read_only = True)
    transaction_type = serializers.CharField(max_length=255, read_only = True)
    class Meta:
        model = UpiTransaction
        fields = ['upi_id', 'amount', 'transaction_number', 'transaction_type', 'user']

    def create(self, validated_data):
        validated_data['transaction_type'] = 'D'
        validated_data['transaction_number'] = generate_unique_transaction_number()
        instance1 = UpiTransaction.objects.create(**validated_data)
        validated_data['transaction_type'] = 'C'
        instance2 = UpiTransaction.objects.create(**validated_data)
        return instance1, instance2
    
class LoanDetailViewSingleSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    loan_account_number = serializers.CharField(max_length=255, read_only=True)
    # is_approved = serializers.BooleanField(default=False, read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    amount = serializers.CharField(read_only=True)
    tenure = serializers.CharField(read_only=True)
    loan_active = serializers.BooleanField(read_only=True)
    class Meta:
        model = LoanDetail
        fields = ['id', 'loan_account_number', 'amount', 'start_date', 'end_date', 'tenure', 'is_approved', 'loan_active', 'user']