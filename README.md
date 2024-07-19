# 

Прогноз погоды

Техническое задание:
```
Сделать web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

 - *Вывод данных (прогноза погоды) должен быть в удобно читаемом формате. 

 - Веб фреймворк можно использовать любой.

 - api для погоды:* https://open-meteo.com/ *(можно использовать какое-нибудь другое, если вам удобнее)*

будет плюсом если:

- написаны тесты
- всё это помещено в докер контейнер
- сделаны автодополнение (подсказки) при вводе города
- при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
- будет сохраняться история поиска для каждого пользователя, и будет API, показывающее сколько раз вводили какой город

что будет оцениваться:

- корректность работы
- удобство использования
- качество кода

в [README.md](http://readme.md/) просьба указать что из выше перечисленного было сделанно, пару слов о использованных технологиях, и как это всё запустит
```

Реализовала следующее:

Приложение, он же сайт, который может спрогнозировать погоду введенного города в формочку.

Для создания этого сайта я использовал ЯП Python на его фреймворке Django, подключил API ключи Яндекса и сервиса dadata, но о нем чуть позже.
Ключи яндекса были необходимы для поиска данных прогноза погоды в определенном регионе.
Вводя в поле формы название города и нажатию кнопки я получаю прогноз на 7 дней.

Из дополнительного - я реализовал автодополнение с использованием API ключа сервиса dadata.ru
Он позволяет по минимально введенным данным в поле отобразить какое-то значение, которое, возможно, хотел ввести пользователь.


Запуск проекта

Инструкция предназначена для windows и git bash и windows<br/>

1. Клонируйте репозиторий и откройте его в любом удобном для вас редакторе:

```
git clone https://github.com/Kiepon/forecast-weather.git
```

2. Установите виртуальное окружение:
```

Git bash:

python -m venv your_venv

Windows:

python -m venv your_venv
``` 

3. Активируйте виртуальное окружение:
```
Git bash:
source venv/Scripts/activate

Windows:
your_venv/Scripts/activate

```

4. Установите зависимости из файла requirements.txt:
```

Windows and git bash:
pip install -r requirements.txt
```

4. Сделайте миграции:
```

Git bash and windows:
python manage.py migrate
```

5. Используйте команду createsuperuser для создания администратора в админ панели:
```

git bash and windows:
python manage.py createsuperuser
```

6. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```