from rest_framework import viewsets 
from rest_framework.decorators import action
from Account.models import Account   
from Account.serializers import AccountSerializer 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView


def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class AuthenticateUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if 'refreshToken' in request.data:
            # Handle token refresh
            try:
                refresh = RefreshToken(request.data['refreshToken'])
                return Response({
                    'status': 'success',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'status': 'failed', 'error': str(e)}, 
                            status=status.HTTP_401_UNAUTHORIZED)

        # Handle initial login
        serial_number = request.data.get('serialNumber')
        user = get_object_or_404(Account, serial_number=serial_number)
        tokens = generate_tokens(user)
        return Response({
            'status': 'success',
            'tokens': tokens,
            'user': AccountSerializer(user).data
        }, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'status': 'failed'}, 
                        status=status.HTTP_401_UNAUTHORIZED)
        
        user_data = AccountSerializer(request.user).data
        return Response({
            'status': 'success',
            'user': user_data
        }, status=status.HTTP_200_OK)
    

class AccountViewSet(viewsets.ModelViewSet): 
    queryset = Account.objects.all() 
    serializer_class = AccountSerializer 
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], authentication_classes=[JWTAuthentication])
    def get_account_info(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)