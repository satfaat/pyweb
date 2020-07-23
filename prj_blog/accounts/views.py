from django.http import HttpResponse


def sign_up(request):
    return HttpResponse('<h1>Страница регистрации</h1>')


def sign_in(request):
    return HttpResponse('<h1>Страница авторизации</h1>')


def my_account(request):
    return HttpResponse('<h1>Данные вашего аккаунта</h1>')


friends = {
    'Роби Тобинсон': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин', 'Твентин Карантино'],
    'Металлий Вутко': ['Металлий Вутко'],
    'Лео Месси': ['Металлий Вутко'],
    'Бен Франклин': ['Металлий Вутко', 'Лео Месси', 'Твентин Карантино', 'Elina Shake', 'Айви Яптанго'],
    'Твентин Карантино': ['Бен Франклин'],
    'Elina Shake': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин'],
    'Айви Яптанго': ['Бен Франклин', 'Твентин Карантино', 'Elina Shake']
}


def get_friends(request, user):
    user_friends = friends[user]  # список друзей пользователя user
    friends_count = len(user_friends)  # длина этого списка
    if friends_count == 1:
        return HttpResponse(f'У пользователя {user} один друг: {user_friends[0]}.')
    elif 2 <= friends_count <= 4 :  # если количество друзей от 2 до 4 включительно, то
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друга: {friends_string}.')
    elif friends_count > 4 :  # если количество друзей более 4, то
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друзей: {friends_string}.')
    else:
        return HttpResponse(f'У пользователя {user} нет друзей :(')
