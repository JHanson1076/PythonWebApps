from django.db import models
from django.urls.base import reverse_lazy

class Cote(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    strength = models.CharField(max_length=200,default='anything')
    weak = models.CharField(max_length=200,default='anything')
    image = models.CharField(max_length=200)
# Create your models here.

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description} - {self.strength} - {self.weak}'

    def get_absolute_url(self):
        return reverse_lazy('cote_detail', args=[str(self.id)])