from logging import PlaceHolder
from random import choices
from django import forms
from .models import Notice, Categoria

choices2 = [('Eventos','Eventos'),('Novedades','Novedades'),('Noticias','Noticias')]
 
choices = Categoria.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('titulo', 'title_tag', 'autor','categoria', 'cuerpo')
#'categoria', 'fecha_publicacion'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agregue el titulo de la Noticia' }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'root', 'type':'hidden'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
        class Meta:
            model = Notice
            fields = ('titulo', 'title_tag', 'autor', 'cuerpo')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }