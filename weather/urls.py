from weather.views import index
from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('', views.weather_forecast, name='weather'),
]