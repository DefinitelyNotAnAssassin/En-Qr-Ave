from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, AuthenticateUserView

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('authenticate/', AuthenticateUserView.as_view(), name='authenticate'),
] + router.urls