from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notice, Categoria
from django.urls import reverse_lazy
from .forms import NoticeForm, UpdateForm

class HomeNotice(ListView):
    model = Notice
    template_name = 'home.html'
    ordering = ['-id']

class DetailNotice(DetailView):
    model = Notice
    template_name = 'Detail_notice.html'

class CreateNotice(CreateView):
    model = Notice
    template_name = 'addNotice.html'
    #fields = '__all__'
    form_class = NoticeForm

class CreateCategoria(CreateView):
    model = Categoria
    template_name = 'addCategoria.html'
    fields = '__all__'


class UpdateNotice(UpdateView):
    model = Notice
    template_name = 'UpdateNotice.html'
    #fields = '__all__'
    form_class = UpdateForm

class DeleteNotice(DeleteView):
    model = Notice
    template_name = 'DeleteNotice.html'
    success_url = reverse_lazy('home')