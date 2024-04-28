from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add_question(request):
    return HttpResponse("Add Question")

def edit_question(request):
    return HttpResponse("Edit Question")

def add_question_bank(request):
    return HttpResponse("Add Question Bank")

def edit_question_bank(request):
    return HttpResponse("Edit Question Bank")

def add_question_paper(request):
    return HttpResponse("Add Question Paper")

def add_question_paper(request):
    return HttpResponse("Edit Question Paper")