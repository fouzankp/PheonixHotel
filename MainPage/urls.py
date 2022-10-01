from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.first_view),
    path('Rooms/', views.second_view),
]
