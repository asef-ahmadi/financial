from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Reciept


class RecieptList(ListView):
    queryset = Reciept.objects.all()
    template_name = "pages/financial/reciept/list.html"
    context_object_name = "reciepts"
