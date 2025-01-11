from django import forms

class CreateNewNoteForm(forms.Form):
    note_name = forms.CharField(label='Name', max_length=100)
    note_text = forms.CharField(label='Text')

class EditNoteForm(forms.Form):
    note_name = forms.CharField(label='Name', max_length=100)
    note_text = forms.CharField(label='Text')