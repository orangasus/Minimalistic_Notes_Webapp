from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewNoteForm
from .models import NotesList

def home_view(request):
    ls = NotesList.objects.get(list_name='Test LS')
    list_names = [x.list_name for x in NotesList.objects.all()]
    return render(request,'my_app/home.html', {'list': ls})

def create_note_view(request):
    ls = NotesList.objects.get(list_name='Test LS')
    if request.method == 'POST':
        form = CreateNewNoteForm(request.POST)
        if form.is_valid():
            note_name = form.cleaned_data['note_name']
            note_text = form.cleaned_data['note_text']

            ls.notes_set.create(note_name=note_name, note_text=note_text)
            return HttpResponseRedirect('/home/')
    else:
        form = CreateNewNoteForm()
        return render(request, 'my_app/new_note.html', {'form':form})


