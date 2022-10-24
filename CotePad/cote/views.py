from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Article, Cote   



class CoteListView(ListView):
    template_name = 'cote/list.html'
    model = Cote
    


class CoteDetailView(DetailView):
    template_name = 'cote/detail.html'
    model = Cote
    


class CoteCreateView(LoginRequiredMixin,CreateView):
    template_name = 'cote/add.html'
    model = Cote
    fields = ['name','description','strengths']


class CoteUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "cote/edit.html"
    model = Cote
    fields = '__all__'

class CoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cote
    template_name = 'cote/delete.html'
    success_url = reverse_lazy('cote_list')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "registration/account_add.html"
    model = Article
    fields = ['author','cote','title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)