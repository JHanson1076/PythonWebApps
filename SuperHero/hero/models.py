from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse_lazy

class SuperHero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    strength = models.CharField(max_length=200,default='anything')
    weak = models.CharField(max_length=200,default='anything')
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description} - {self.strength} - {self.weak}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])


class Article (models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    SuperHero = models.ForeignKey(SuperHero, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()       

   

 