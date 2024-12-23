from django.contrib import admin
from isort.profiles import django

from .models import NotesList, Note

# Register your models here.
admin.site.register(Note)
admin.site.register(NotesList)

