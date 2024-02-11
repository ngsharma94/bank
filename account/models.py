from random import choices
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = None

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    ACCOUNT_TYPE_CHOICES = [
        ('SA', 'Savings Account'),
        ('CA', 'Current Account'),
        ('CC', 'Credit Card')
    ]
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES)

    ACCOUNT_HOLDER_TYPE_CHOICES = [
        ('G', 'General'),
        ('S', 'Supervisor')
    ]
    account_holder_type = models.CharField(max_length=1, choices=ACCOUNT_HOLDER_TYPE_CHOICES)

    SALARY_ACCOUNT_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    salary_account = models.CharField(max_length=1, choices=SALARY_ACCOUNT_CHOICES)

    account_number = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    upi_id = models.CharField(max_length=255)

    balance = models.CharField(max_length=255)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
