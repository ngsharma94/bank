import random
from .models import UserProfile

def generate_unique_account_number():
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if not UserProfile.objects.filter(account_number=account_number).exists():
            return account_number
        
def generate_unique_customer_id():
    while True:
        customer_id = str(random.randint(100000, 999999))
        if not UserProfile.objects.filter(customer_id=customer_id).exists():
            return customer_id