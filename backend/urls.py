"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ticketing.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

# Registering ViewSets with the router
router = routers.DefaultRouter()
router.register('event', EventViewSet)
router.register('booking', BookingViewSet)
router.register('monitoring', MonitoringViewSet)

# Defining URL patterns
urlpatterns = [
    path('', include(router.urls)),   
    path('admin/', admin.site.urls),   
    path('login/', LoginView.as_view(), name='login'),   
    path('logout/', LogoutView.as_view(), name='logout'),   
    path('create-order/', CreateOrder.as_view(), name='create-order'),  
    path('payment/', PaymentCapture.as_view(), name='payment'),  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  