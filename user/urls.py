"""
URL configuration for ChristmasStore project.

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
from django.urls import path
from django.shortcuts import render 
from .views import home,login,register,logout,single_product,add_to_cart,cart_view


urlpatterns = [
    path('', home,name="home"),
    path('login/', login,name="login"),
    path('register/', register,name="register"),
    path('logout/', logout,name="logout"),
    path('single-product/<int:product>', single_product,name="single-product"),
    path('add_to_cart/<int:product>', add_to_cart,name="add_to_cart"),
    path('cart_view/', cart_view,name="cart_view"),
]
