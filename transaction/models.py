from django.db import models
from account.models import User

# Create your models here.

class OnlineTransaction(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    account_number = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    TRANCASTION_TYPE_CHOICES = [
        ('D', 'Debit'),
        ('C', 'Credit')
    ]
    transaction_type = models.CharField(max_length=1, choices=TRANCASTION_TYPE_CHOICES)
    transaction_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UpiTransaction(models.Model):
    upi_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    TRANCASTION_TYPE_CHOICES = [
        ('D', 'Debit'),
        ('C', 'Credit')
    ]
    transaction_type = models.CharField(max_length=1, choices=TRANCASTION_TYPE_CHOICES)
    transaction_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LoanDetail(models.Model):
    loan_account_number = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    TENURE_CHOICES = [
        ('1', 'One Year'),
        ('2', 'Two Years'),
        ('3', 'Three Years'),
        ('4', 'Four Years'),
        ('5', 'Five Years'),
    ]
    tenure = models.CharField(max_length=1, choices=TENURE_CHOICES)
    is_approved = models.BooleanField(default=False)
    loan_active = models.BooleanField(default=False)
    always_yes_because_of_signals = models.BooleanField(default=False)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FixedDeposit(models.Model):
    amount = models.DecimalField(max_digits=90, decimal_places=2)
    interest = models.CharField(max_length=255)
    maturity_amount = models.CharField(max_length=255)
    fixed_deposit_number = models.CharField(max_length=255)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    TENURE_CHOICES = [
        ('1', 'One Year'),
        ('2', 'Two Years'),
        ('3', 'Three Years'),
        ('4', 'Four Years'),
        ('5', 'Five Years'),
    ]
    tenure = models.CharField(max_length=1, choices=TENURE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)