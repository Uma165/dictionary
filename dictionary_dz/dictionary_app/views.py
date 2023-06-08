from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Word, Definition

class WordListView(ListView):
    model = Word
    template_name = 'dictionary/word_list.html'

class WordDetailView(DetailView):
    model = Word
    template_name = 'dictionary/word_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['definitions'] = Definition.objects.filter(word=self.object)
        return context

class WordCreateView(CreateView):
    model = Word
    fields = ['title']
    template_name = 'dictionary/word_form.html'

class WordUpdateView(UpdateView):
    model = Word
    fields = ['title']
    template_name = 'dictionary/word_form.html'

class WordDeleteView(DeleteView):
    model = Word
    success_url = reverse_lazy('dictionary:word_list')
    template_name = 'dictionary/word_confirm_delete.html'

class WordSearchView(ListView):
    model = Word
    template_name = 'dictionary/word_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Word.objects.filter(Q(title__icontains=query) | Q(definitions__text__icontains=query)).distinct()
        else:
            return Word.objects.all()


