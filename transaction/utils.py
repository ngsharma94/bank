import random
from .models import UpiTransaction
from account.models import UserProfile
from decimal import Decimal

def generate_unique_transaction_number():
    while True:
        transaction_number = str(random.randint(1000000000000000, 9999999999999999))
        if not UpiTransaction.objects.filter(transaction_number=transaction_number).exists():
            return transaction_number
        

def subtract_amount(user, amount):
    my_user = UserProfile.objects.get(user_id = user)
    available_balance = my_user.balance
    updated_balance = Decimal(available_balance) - Decimal(amount)
    my_user.balance = updated_balance
    my_user.save()
    

def add_amount(user, amount):
    my_user = UserProfile.objects.get(user_id = user)
    available_balance = my_user.balance
    updated_balance = Decimal(available_balance) + Decimal(amount)
    my_user.balance = updated_balance
    my_user.save()