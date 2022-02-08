from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from staff_management.views import UserViewSet, TeamViewSet
from client_management.views import ClientViewSet
from contract_management.views import ContractViewSet
from event_management.views import EventViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
