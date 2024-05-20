from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView
from .views import CustomUserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/users/me/', CustomUserViewSet.as_view({'get': 'me'}), name='user-me'),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', RedirectView.as_view(url='/admin/')),

    path('api/sales/', include('Sales.urls')),
    path('api/manufacturing/', include('Manufacturing.urls')),
    path('api/inventory/', include('Inventory.urls')),
]