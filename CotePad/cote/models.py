from django.db import models

class Cote(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    strength = models.CharField(max_length=200,default='anything')
    weak = models.CharField(max_length=200,default='anything')
    image = models.CharField(max_length=200)
# Create your models here.

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description} - {self.strength} - {self.weak}'