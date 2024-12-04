"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from app1 import views
from app1.views import buy_pet, payment, admin_add_pet, admin_panel, admin_remove_pet
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.homepage, name='home'),
    path('logout/', views.logoutpage, name='logout'),
    path('user/', views.userpage, name='user'),
    path('service/', views.servicepage, name='service'),
    path('newservices/', views.servicespage, name='newservices'),
    path('Buying/', views.buying_page, name='Buying'),
    path('Buying/make_payment.html', views.make_payment, name='make_payment'),
    path('Adoption/', views.Adoption, name='Adoption'),
    path('pricing/', views.pricing, name='pricing'),

    #new code:

    path('buy/', buy_pet, name='buy_pet'),
    path('payment/', payment, name='payment'),
    path('admin/add_pet/', admin_add_pet, name='admin_add_pet'),
    path('admin/panel/', admin_panel, name='admin_panel'),
    path('admin/remove_pet/<int:pet_id>/', admin_remove_pet, name='admin_remove_pet'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)