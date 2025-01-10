from django.db import models

# Create your models here.
class NotesList(models.Model):
    list_name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def delete_note_by_id(self, note_id):
        try:
            to_delete = self.notes_set.get(id = note_id)
            to_delete.delete()
            return True
        except:
            return False


class Note(models.Model):
    list = models.ForeignKey(NotesList, on_delete=models.CASCADE, related_name='notes_set')
    note_name = models.CharField(max_length=200)
    note_text = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
