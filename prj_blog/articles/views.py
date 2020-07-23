from django.http import HttpResponse

articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья", ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го", ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]


# в функции generate_html()
# оформим перечень статей в виде html-списка
def generate_html(articles):
    if len(articles) == 0:
        return '<h1>По вашему запросу не найдено ни одной статьи!</h1>'
    else:
        base_html = '<h1>Статьи по вашему запросу:</h1> <ul>'
        for article in articles:
            list_item = f'<li><ul>' \
                        f'<li><strong>{article[3]}</strong></li>' \
                        f'<li>автор: {article[1]}</li>' \
                        f'<li>год: {article[2]}</li>' \
                        f'<li>теги: {", ".join(article[4])}</li>' \
                        f'</ul></li>'
            base_html += list_item
        base_html += '</ul>'
        return base_html


# на случай, если в адресе не указан год - установим значение year=-1
def dashboard(request, year=-1):
    found_articles = []
    if year == -1:
        # если в адресе не указан год,
        # записываем в found_articles все статьи нашего блога
        found_articles = articles_list
    else:
        for article in articles_list:
            if year == article[2]:
                found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def article_by_id(request, id):
    found_articles = []
    for article in articles_list:
        if id == article[0]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def articles_by_tag(request, tag):
    found_articles = []
    for article in articles_list:
        if tag in article[4]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def search(request):
    if request.method == 'GET':
        name = request.GET['name']  # получите автора статьи из запроса
        year = int(request.GET['year'])  # получите год из запроса
        found_articles = []
        for article in articles_list:
            if name == article[1] and year == article[2]:
            # если автор и год совпадают с запрошенными
                found_articles.append(article)
        beautiful_html = generate_html(found_articles)
        return HttpResponse(beautiful_html)



def articles_by_tag(request, tag):  # добавьте второй параметр
    found_articles = []
    for article in articles_list:
        for i in range(0,len(article[4])):
            if tag == article[4][i]:
                found_articles.append(article)
    
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


from django.http import HttpResponse

articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья", ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го", ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]


# в функции generate_html()
# оформим перечень статей в виде html-списка
def generate_html(articles):
    if len(articles) == 0:
        return '<h1>По вашему запросу не найдено ни одной статьи!</h1>'
    else:
        base_html = '<h1>Статьи по вашему запросу:</h1> <ul>'
        for article in articles:
            list_item = f'<li><ul>' \
                        f'<li><strong>{article[3]}</strong></li>' \
                        f'<li>автор: {article[1]}</li>' \
                        f'<li>год: {article[2]}</li>' \
                        f'<li>теги: {", ".join(article[4])}</li>' \
                        f'</ul></li>'
            base_html += list_item
        base_html += '</ul>'
        return base_html


# на случай, если в адресе не указан год - установим значение year=-1
def dashboard(request, year=-1):
    found_articles = []
    if year == -1:
        # если в адресе не указан год,
        # записываем в found_articles все статьи нашего блога
        found_articles = articles_list
    else:
        for article in articles_list:
            if year == article[2]:
                found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def article_by_id(request, id):
    found_articles = []
    for article in articles_list:
        if id == article[0]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def articles_by_tag(request, tag):
    found_articles = []
    for article in articles_list:
        if tag in article[4]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


html_template = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>My Praktikum Blog</title>
</head>
<body>
    <form action="{where}" method="post">
        Введите ID статьи и имя нового тега<br><br>
        ID статьи: <input type="text" name="id"><br><br>
        Новый тег: <input type="text" name="new_tag"><br><br>
        <input type="submit" value="Добавить тег">
    </form>
</body>
</html>'''


def add_tag(request):
    if request.method == 'GET':
        html = html_template.format(where = request.path)
        resp = HttpResponse(html)
        return resp
    elif request.method == 'POST':
        article_id = int(request.POST['id'])  # получите ID статьи из запроса
        new_tag = request.POST['new_tag']     # получите новый тег из запроса
        # допишите код здесь:
        for article in articles_list:
            if article[0] == article_id:
                article[4].append(new_tag)
        return article_by_id(request, article_id)

from django.http import HttpResponse
from django.shortcuts import render

articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья", ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го", ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]


# в функции generate_html()
# оформим перечень статей в виде html-списка
def generate_html(articles):
    if len(articles) == 0:
        return '<h1>По вашему запросу не найдено ни одной статьи!</h1>'
    else:
        base_html = '<h1>Статьи по вашему запросу:</h1> <ul>'
        for article in articles:
            list_item = f'<li><ul>' \
                        f'<li><strong>{article[3]}</strong></li>' \
                        f'<li>автор: {article[1]}</li>' \
                        f'<li>год: {article[2]}</li>' \
                        f'<li>теги: {", ".join(article[4])}</li>' \
                        f'</ul></li>'
            base_html += list_item
        base_html += '</ul>'
        return base_html


# на случай, если в адресе не указан год - установим значение year=-1
def dashboard(request, year=-1):
    found_articles = []
    if year == -1:
        # если в адресе не указан год,
        # записываем в found_articles все статьи нашего блога
        found_articles = articles_list
    else:
        for article in articles_list:
            if year == article[2]:
                found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def article_by_id(request, id):
    found_articles = []
    for article in articles_list:
        if id == article[0]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def get_articles_by_tag(tag):
    found_articles = []
    for article in articles_list:
        if tag in article[4]:
            found_articles.append(article)
    return found_articles


def articles_by_tag(request, tag):
    beautiful_html = generate_html(get_articles_by_tag(tag))
    return HttpResponse(beautiful_html)


def check_age(request):
    if request.method == 'GET':
        user_age = int(request.GET['age'])  # получить возраст из запроса
        if user_age < 18 :  # если возраст из запроса меньше разрешённого
            return render(request, 'templates/articles/access_denied.html')  # отдать шаблон с информацией о запрете доступа
        else:
            login = request.GET['login']  # сюда значение login из запроса
            tag = request.GET['tag']    # сюда значение tag из запроса
            articles = get_articles_by_tag(tag)
            context = {
                'username' : login,  # сюда логин, который сообщил пользователь
                'age' : user_age,  # сюда возраст, который сообщил пользователь
                'articles' : articles  # сюда список статей, в которых есть нужный тег
            }
            # вместо многоточия укажите имя HTML-шаблона:
            return render(request, 'templates/articles/access_granted.html', context)

from django.http import HttpResponse
from django.shortcuts import render

articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья", ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го", ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]


# в функции generate_html()
# оформим перечень статей в виде html-списка
def generate_html(articles):
    if len(articles) == 0:
        return '<h1>По вашему запросу не найдено ни одной статьи!</h1>'
    else:
        base_html = '<h1>Статьи по вашему запросу:</h1> <ul>'
        for article in articles:
            list_item = f'<li><ul>' \
                        f'<li><strong>{article[3]}</strong></li>' \
                        f'<li>автор: {article[1]}</li>' \
                        f'<li>год: {article[2]}</li>' \
                        f'<li>теги: {", ".join(article[4])}</li>' \
                        f'</ul></li>'
            base_html += list_item
        base_html += '</ul>'
        return base_html


# на случай, если в адресе не указан год - установим значение year=-1
def dashboard(request, year=-1):
    found_articles = []
    if year == -1:
        # если в адресе не указан год,
        # записываем в found_articles все статьи нашего блога
        found_articles = articles_list
    else:
        for article in articles_list:
            if year == article[2]:
                found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def article_by_id(request, id):
    found_articles = []
    for article in articles_list:
        if id == article[0]:
            found_articles.append(article)
    beautiful_html = generate_html(found_articles)
    return HttpResponse(beautiful_html)


def get_articles_by_tag(tag):
    found_articles = []
    for article in articles_list:
        if tag in article[4]:
            found_articles.append(article)
    return found_articles


def articles_by_tag(request, tag):
    beautiful_html = generate_html(get_articles_by_tag(tag))
    return HttpResponse(beautiful_html)


def check_age(request):
    if request.method == 'GET':
        user_age = int(request.GET['age'])
        if user_age < 18:
            return render(request, 'templates/articles/access_denied.html')
        else:
            login = request.GET['login']
            tag = request.GET['tag']
            articles = get_articles_by_tag(tag)
            context = {
                'username': login,
                'age': user_age,
                'articles': articles
            }
            return render(request, 'templates/articles/access_granted.html', context)


def subscribe(request):
    if request.method == 'GET':
        context = {
            'where': request.path
        }
        resp = render(request, 'templates/articles/subscribe_form.html', context)
        return resp
    elif request.method == 'POST':
        # получите имя автора и email из request:
        author = request.POST['author']
        user_email = request.POST['email']

        author_articles = []
        # здесь пройдите циклом по статьям
        # и сложите все статьи автора в список author_articles
        for article in articles_list:
            if author == article[1]:
                #author_articles.append(article[3])
                author_articles.append(article)

        # заполните словарь
        context = {
            'author': author,
            'email': user_email,
            'articles': generate_html(author_articles)
        }

        # передайте в render()
        # шаблон templates/articles/subscribe.html
        # и словарь context
        return render(request, 'templates/articles/subscribe.html', context)
