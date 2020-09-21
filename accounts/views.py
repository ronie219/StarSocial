from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreation



class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreation
