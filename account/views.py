# from django.shortcuts import redirect, render

# from .forms import CreateUserForm



# def register(request):

#     form = CreateUserForm()

#     if request.method == 'POST':

#         form = CreateUserForm(request.POST)

#         if form.is_valid():

#             form.save()

#             return redirect()
#     context ={'form':form}

#     return render(request, 'account/registration/register.html', context=context)

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('store')
    else:
        form = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': form})

