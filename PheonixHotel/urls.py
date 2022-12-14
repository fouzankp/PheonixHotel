"""PheonixHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from MainPage import views
import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Main/', include('MainPage.urls')),
    path("", views.front, name="front"),
    path('rooms/', views.RoomView, name='Rooms'),
    path('rooms/<int:pk>', views.RoomDetail, name='Details'),
    path('checkin/<int:pk>', views.Checkin, name='Checkin'),
    path('checkout/<int:pk>', views.Checkout, name='Checkout'),
    path('Reserve/<int:pk>', views.Reserve, name='Reserve'),
   
]
