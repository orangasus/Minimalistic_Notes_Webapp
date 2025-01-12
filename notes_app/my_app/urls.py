from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("create_note/", views.create_note_view, name="create_note"),
    path("delete_note/<int:list_id>/<int:note_id>",
         views.delete_note_view, name="delete_note"),
    path("edit_note/<int:list_id>/<int:note_id>", views.edit_note_view, name="edit_note")
]
