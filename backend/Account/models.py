from django.db import models
from django.contrib.auth.models import AbstractUser 


class Account(AbstractUser): 
    serial_number = models.CharField(max_length=100, unique=True, blank = True, null = True) 
