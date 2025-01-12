from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewNoteForm, EditNoteForm
from .models import NotesList, Note

def home_view(request):
    ls = NotesList.objects.get(list_name='Test LS')
    ls_notes = ls.notes_set.all()

    return render(request,'my_app/home.html',
                  {'list':ls_notes})

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
    elif request.method == 'GET':
        form = CreateNewNoteForm()
        return render(request, 'my_app/new_note.html', {'form':form})

def edit_note_view(request, list_id, note_id):
    ls = NotesList.objects.get(id=list_id)
    note_to_edit = ls.notes_set.get(id=note_id)
    if request.method == 'GET':
        init_data = {'note_name' : note_to_edit.note_name, 'note_text' : note_to_edit.note_text}
        form = EditNoteForm(initial=init_data)
        return render(request, 'my_app/edit_note.html', {'form':form})

    elif request.method == 'POST':
        form = EditNoteForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['note_name']
            new_text = form.cleaned_data['note_text']
            ls.edit_note_by_id(note_id, new_name, new_text)
            return redirect('home')




