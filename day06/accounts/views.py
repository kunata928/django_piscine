from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegistrateForm

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('signup')
#     template_name = 'signup.html'

def registrate(request):
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('#')
    else:
        form = RegistrateForm()
    return render(request, 'signup.html', {'form':form})
#     form_class = UserCreationForm
#     success_url = reverse_lazy('signup')
#     template_name = 'signup.html'