from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, logout, login
from django.contrib.auth import forms as auth_forms


# Admin View
def admin_view(request):
    if not request.user.is_staff and request.user.is_superuser:
        return redirect('index')


# Main index view
def index(request):
    return render(request, 'scriky/index.html')


# Login view        Im Moment nicht verwendet, es werden die internen Views bzw URLs von Django verwendet
def login_user(request):
    login_form = ""  # auth_forms.

    return render(request, 'registration/login.html', {'form': login_form})


# Login view        Im Moment nicht verwendet, es werden die internen Views bzw URLs von Django verwendet
def logout_user(request):
    logout(request)
    # messages.success(request, 'Sie haben sich abgemeldet. 🦄 ')
    return redirect('home')


# User Registration view
def register_user(request):
    if request.method == 'POST':
        register_form = auth_forms.UserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            return redirect('index')

    else:
        register_form = auth_forms.UserCreationForm(request.POST)

    return render(request, 'registration/register.html', {'form': register_form})


# Article create view
def create(request):
    return render(request, 'article/createArticle.html')
