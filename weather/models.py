from django.db import models

NULLABLE = {'blank': True, 'null': True}


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название города')
    latitude = models.FloatField(verbose_name='Широта', **NULLABLE)
    longitude = models.FloatField(verbose_name='Долгота', **NULLABLE)

    def __str__(self):
        return self.name  # Возвращает название города в виде строкового представления

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class WeatherForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    temperature = models.FloatField(verbose_name='Температура')
    humidity = models.IntegerField(verbose_name='Влажность')
    wind_speed = models.FloatField(verbose_name='Скорость ветра')
    weather_description = models.CharField(max_length=200, **NULLABLE)
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f"{self.city.name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = 'Прогноз погоды'
        verbose_name_plural = 'Прогнозы погоды'
        ordering = ['-date_time']
