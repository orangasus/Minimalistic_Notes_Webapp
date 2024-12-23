from django.db import models

# Create your models here.
class NotesList(models.Model):
    list_name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)


class Note(models.Model):
    list = models.ForeignKey(NotesList, on_delete=models.CASCADE, related_name='notes_set')
    note_name = models.CharField(max_length=200)
    note_text = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
