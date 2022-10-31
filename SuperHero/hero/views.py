from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Article, SuperHero   



class SuperHeroListView(ListView):
    template_name = 'SuperHero/list.html'
    model = SuperHero
    


class SuperHeroDetailView(DetailView):
    template_name = 'SuperHero/detail.html'
    model = SuperHero
    


class SuperHeroCreateView(LoginRequiredMixin,CreateView):
    template_name = 'SuperHero/add.html'
    model = SuperHero
    fields = ['name','description','strengths']


class SuperHeroUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "SuperHero/edit.html"
    model = SuperHero
    fields = '__all__'

class SuperHeroDeleteView(LoginRequiredMixin,DeleteView):
    model = SuperHero
    template_name = 'SuperHero/delete.html'
    success_url = reverse_lazy('SuperHero_list')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "registration/account_add.html"
    model = Article
    fields = ['author','SuperHero','title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
