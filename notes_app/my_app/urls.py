from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.sign_up_view, name="signup"),
    path("create_note/", views.create_note_view, name="create_note"),
    path("delete_note/<int:list_id>/<int:note_id>",
         views.delete_note_view, name="delete_note")
]
