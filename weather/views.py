from django.conf import settings
from django.shortcuts import render
from . import forms
import json
import requests
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def weather_forecast(request):
    if request.method == 'POST':
        forecast_form = forms.ForecastForm(request.POST)
        if forecast_form.is_valid():
            city = forecast_form.cleaned_data['city']
            access_key = settings.ACCESS_KEY
            yandex_geocode = settings.YANDEX_GEOCODE
            dadata_token = settings.DADATA_TOKEN
            headers = {
                'X-Yandex-Weather-Key': access_key
            }
            response = requests.get(
                f'https://geocode-maps.yandex.ru/1.x?apikey={yandex_geocode}&format=json&geocode={city}')
            json_response = response.json()
            try:
                # Получаем координаты города из ответа геокодера
                coordinates = \
                json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
                    'pos'].split()
                lat = coordinates[1]  # Широта
                lon = coordinates[0]  # Долгота
            except (IndexError, KeyError):
                return HttpResponse('Город не найден')
            # Формируем параметры запроса к API погоды
            res = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU',
                               headers=headers)
            weather = json.loads(res.text)

            city_info = []

            for day_week in range(7):
                if day_week < len(weather['forecasts']):
                    day_info = {
                        'city': city,
                        'date': weather['forecasts'][day_week]['date'],
                        'icon': weather['forecasts'][day_week]['parts']['day_short']['icon'],
                        'temp': weather['forecasts'][day_week]['parts']['day_short']['temp'],
                        'feels_like': weather['forecasts'][day_week]['parts']['day_short']['feels_like'],
                        'wind_speed': weather['forecasts'][day_week]['parts']['day_short']['wind_speed']
                    }
                    city_info.append(day_info)

            forecast_form = forms.ForecastForm()

            context = {
                'forecast_form': forecast_form,
                'city_info': city_info,
                'city': city,
                'dadata_token': dadata_token,
            }
            return render(request, 'index.html', context=context)
    forecast_form = forms.ForecastForm()
    return render(request, 'index.html', {'forecast_form': forecast_form})