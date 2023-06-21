from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import ClothRoll
from .forms import ClothRollForm


class ClothRollList(ListView):
    model = ClothRoll
    queryset = ClothRoll.objects.all()
    template_name = "pages/warehouse/clothroll/list.html"
    context_object_name = "clothrolls"


class ClothRollDetail(DetailView):
    model = ClothRoll
    queryset = ClothRoll.objects.all()
    template_name = "pages/warehouse/clothroll/detail.html"
    context_object_name = "clothroll"
    pk_url_kwarg = 'pk'


class ClothRollCreate(CreateView):
    model = ClothRoll
    template_name = 'pages/warehouse/clothroll/create.html'
    form_class = ClothRollForm
    success_url = reverse_lazy("clothroll-list")


class ClothRollUpdate(UpdateView):
    model = ClothRoll
    form_class = ClothRollForm
    template_name = "pages/warehouse/clothroll/update.html"
    success_url = reverse_lazy("clothroll-list")
    pk_url_kwarg = "pk"


# class CutClothRoll(DetailView):
#     model = ClothRoll
#     queryset = CutClothRoll.objects.select_related('')

def delete(request, id):
    obj = ClothRoll.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('clothroll-list'))
