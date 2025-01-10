from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewNoteForm
from .models import NotesList, Note

def home_view(request):
    ls = NotesList.objects.get(list_name='Test LS')
    ls_notes = ls.notes_set.all()

    return render(request,'my_app/home.html',
                  {'list':ls_notes})

def sign_up_view(request):
    pass

def login_view(request):
    pass

def delete_note_view(request, note_id, list_id):
    if request.method == 'POST':
        ls = NotesList.objects.get(id=list_id)
        ls.delete_note_by_id(note_id)
        return redirect('home')

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


