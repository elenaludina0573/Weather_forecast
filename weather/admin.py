from django.contrib import admin

from weather.models import City, WeatherForecast


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature', 'humidity', 'wind_speed', 'date_time']
