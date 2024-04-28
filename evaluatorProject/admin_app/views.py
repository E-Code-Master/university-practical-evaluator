from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import SignupForm

def home(request):
    return HttpResponse("Hello World!")

def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created succesfully")
        else:
            messages.error(request, "Error")
    else:
        form = SignupForm()
    return render(request, "registration/register.html", {'form': form})

def add_user(request):
    return HttpResponse("Add User")

def edit_user(request):
    return HttpResponse("Edit User")

def add_bulk_users(request):
    return HttpResponse("Bulk Upload for User")

def add_university(request):
    return HttpResponse("Add University")

def edit_university(request):
    return HttpResponse("Edit University")

def add_college(request):
    return HttpResponse("Add College")

def edit_college(request):
    return HttpResponse("Edit College")

def create_classroom(request):
    return HttpResponse("Create Classroom")

def update_classroom(request):
    return HttpResponse("Update Classroom")

def schedule_exam(request):
    return HttpResponse("Schedule Exam")

def update_exam(request):
    return HttpResponse("Update Exam")