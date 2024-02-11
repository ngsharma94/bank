from django.contrib import admin
from .models import User, UserProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'date_joined', 'last_login', 'is_superuser', 'is_staff')
    list_filter = ('email',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #  ('Permissions', {'fields': ('is_admin',)}),
    # )
    search_fields = ('email',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'city', 'state', 'account_type', 'branch_name', 'user')
    search_fields = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, ProfileAdmin)
