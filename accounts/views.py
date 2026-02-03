from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def register_page(request):
    return HttpResponse('Register Page')