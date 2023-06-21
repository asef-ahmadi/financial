from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import User
from .forms import UserForm


class UserList(ListView):
    model = User
    queryset = User.objects.all()
    template_name = "pages/user/list.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = User
    queryset = User.objects.select_related('payment_card')
    template_name = "pages/user/detail.html"
    context_object_name = "user"
    pk_url_kwarg = 'pk'


class UserCreate(CreateView):
    model = User
    template_name = 'pages/user/create.html'
    form_class = UserForm
    success_url = reverse_lazy("user-list")


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = "pages/user/update.html"
    success_url = reverse_lazy("user-list")
    pk_url_kwarg = "pk"


def delete(request, id):
    post = User.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('user-list'))


class UserDelete(DeleteView):
    model = User
    # template_name_suffix = "_confirm_delete"
    template_name = "pages/user/user_confirm_delete.html"
    success_url = reverse_lazy("user-list")
    pk_url_kwarg = "pk"
