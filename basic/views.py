from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from basic.models import personaldetail
# Create your views here.
class DetailList(ListView):
    model = personaldetail

class DetailCreate(CreateView):
    model = personaldetail
    fields = ['firstname', 'lastname', 'mobileno']
    success_url = reverse_lazy('basic:detail_list')

class DetailUpdate(UpdateView):
    model = personaldetail
    fields = ['firstname', 'lastname', 'mobileno']
    success_url = reverse_lazy('basic:detail_list')

class DetailDelete(DeleteView):
    model = personaldetail
    success_url = reverse_lazy('basic:detail_list')
    
