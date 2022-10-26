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

   

 