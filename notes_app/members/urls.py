from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.login_view, name='login_user'),
    path('login_user', views.logout_view, name='logout_user'),
    path('signup_user', views.signup_view, name='signup_user')
]
