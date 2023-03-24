from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NotesForm
# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"