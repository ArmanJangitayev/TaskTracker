from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
