from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("create_note/", views.create_note_view, name="create_note")
]
