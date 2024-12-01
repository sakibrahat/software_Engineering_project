"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# registration/urls.py
from django.contrib import admin

from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.homepage, name='home'),
    path('logout/', views.logoutpage, name='logout')
    

]
