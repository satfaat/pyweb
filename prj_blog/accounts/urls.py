from django.urls import path
from . import views
from accounts import views as acc_views

urlpatterns = [
    path('sign-up', acc_views.sign_up),
    path('sign-in', acc_views.sign_in),
    path('my-account', acc_views.my_account),
    path('friends/<str:user>', acc_views.get_friends)
]
