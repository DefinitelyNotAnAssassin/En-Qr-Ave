from django.urls import path 
from API import views

urlpatterns = [ 
               path('login', views.login, name = "login")
               ]