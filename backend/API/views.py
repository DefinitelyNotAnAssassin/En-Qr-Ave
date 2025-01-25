from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from  Account.models import Account
import json

@csrf_exempt
def login(request): 
    data = request.body 
    data = data.decode('utf-8') 
    print(data) 
    json_data = json.loads(data) 
 
    serial_number = json_data.get('serial_number')
    account = get_object_or_404(Account, serial_number = serial_number)
    if account and account.serial_number == serial_number:
        auth_login(request, account)
        refresh = RefreshToken.for_user(account)
        
        return JsonResponse({'status': 'success',
                                'account': {
                                    'firstname': account.first_name,
                                    'lastname': account.last_name,
                                    'email': account.email,
                                    'serial_number': account.serial_number,
                                },
                                'refresh': str(refresh),
                                'access': str(refresh.access_token)})
    else:
        return HttpResponse(status=501)

def verifyAuth(request): 
    return JsonResponse({'status': 'success'}, safe = False)

