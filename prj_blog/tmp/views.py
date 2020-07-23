from django.http import HttpResponse


def index(request):
    html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>My Praktikum Blog</title>
</head>
<body>
    <h1>Главная страница нашего проекта</h1>
    <p>Привет, <b>студент</b>!</p>
    <p>Начинаем работать с Django-тренажёром.</p>
</body>
</html>'''

    # создаём объект типа HttpResponse
    resp = HttpResponse(html)

    # и возвращаем его
    return resp
