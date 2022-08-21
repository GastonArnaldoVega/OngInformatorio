from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Categoria(models.Model):
    name = models.CharField(max_length=250)
        
    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('home')


class Notice(models.Model):
    titulo = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=255, default='Noticia Nueva')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=250, default='Noticias')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('home')