from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Account.models import Account 



admin.site.register(Account, UserAdmin) 