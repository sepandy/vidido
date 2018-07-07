from django.shortcuts import render
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    from_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'