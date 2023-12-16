import logging
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }


        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>

        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. </p>


        <p><a href="/about"> Обо мне </a></p>
        
        <p><a href="/homework3"> домашнее задание к семинару 3 </a></p>
        <p><a href="/homework4"> домашнее задание к семинару 4 </a></p>
    </body>
   
    
    
    </html>
    """
    logger.info(f'Index page accessed: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

        </style>
    </head>
    <body>

        <h1>Обо мне</h1>
        <p>Привет, меня зовут Евгений Базаров. Я являюсь начинающим Python-разработчиком</p>

        <footer>
            <p>Свяжитесь со мной: evgeny-bazarov@yandex.ru</p>
        </footer>
    </body>
    </html>
    """

    logger.info(f'About page accessed: {datetime.now()}')
    return HttpResponse(html)
