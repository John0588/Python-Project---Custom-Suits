"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from customSuits.views import home
from customSuits.views import about
from customSuits.views import services
from customSuits.views import contactUs
from customSuits.views import signIn
from customSuits.views import signUp

from customSuits.views import item
from customSuits.views import cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contactUs/', contactUs, name='contactUs'),
    path('signIn/', signIn, name='signIn'),
    path('signUp/', signUp, name='signUp'),
    path('cart/', cart, name='cart'),
    path('item/', item, name='item'),
    path('maps/', contactUs, name='maps')
]
