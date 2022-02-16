from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['email','username','first_name','last_name','is_active']
    filter_horizontal=()
    list_filter=()
    fieldsets=()

# admin.site.register(MyAccountManager)
admin.site.register(Account,AccountAdmin)