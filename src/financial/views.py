from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Reciept
from .forms import RecieptForm
from django.urls import reverse_lazy


class RecieptList(ListView):
    queryset = Reciept.objects.all()
    template_name = "pages/financial/reciept/list.html"
    context_object_name = "reciepts"


class RecieptDetail(DetailView):
    queryset = Reciept.objects.select_related('to_accounts', 'from_accounts')
    template_name = "pages/financial/reciept/detail.html"
    context_object_name = "reciept"
    pk_url_kwarg = 'pk'


class RecieptCreate(CreateView):
    model = Reciept
    template_name = 'pages/financial/reciept/create.html'
    form_class = RecieptForm
    success_url = reverse_lazy("reciept-list")
