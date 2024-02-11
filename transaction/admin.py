from django.contrib import admin
from .models import UpiTransaction, OnlineTransaction, LoanDetail, FixedDeposit

# Register your models here.

class UpiTransactionAdmin(admin.ModelAdmin):
    list_display = ('upi_id', 'amount', 'transaction_number', 'user')
    search_fields = ('user','transaction_number', 'user_id')

admin.site.register(UpiTransaction, UpiTransactionAdmin)

class OnlineTransactionAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'ifsc_code', 'amount', 'transaction_number', 'name', 'user')
    search_fields = ('transaction_number', 'user', 'account_number')

admin.site.register(OnlineTransaction, OnlineTransactionAdmin)

class LoanDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'loan_account_number', 'amount', 'tenure', 'is_approved', 'start_date', 'end_date')
    search_fields = ('loan_account_number',)

admin.site.register(LoanDetail, LoanDetailAdmin)

class FixedDepositAdmin(admin.ModelAdmin):
    list_display = ('fixed_deposit_number', 'amount', 'interest', 'maturity_amount', 'start_date', 'end_date')
    search_fields = ('fixed_deposit_number',)
    
admin.site.register(FixedDeposit, FixedDepositAdmin)