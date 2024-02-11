from pyexpat import model
from turtle import mode
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import UserProfile, User
from .utils import generate_unique_account_number, generate_unique_customer_id



class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=10, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError('Email already exisits')
        return super().validate(attrs)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, read_only=True)
    account_number = serializers.CharField(max_length=255, read_only=True)
    customer_id = serializers.CharField(max_length=255, read_only=True)
    balance = serializers.CharField(max_length=255, read_only=True)
    upi_id = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'state', 'pincode', 'company', 'account_type', 'salary_account', 'account_number', 'ifsc_code', 'branch_name', 'customer_id', 'upi_id', 'balance', 'user']

    def create(self, validated_data):
        validated_data['account_number'] = generate_unique_account_number()
        validated_data['customer_id'] = generate_unique_customer_id()
        validated_data['upi_id'] = str(validated_data['phone_number']) + '@upi' 
        return super().create(validated_data)