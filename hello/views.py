from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def greet(request, name):
    return HttpResponse(f'<h1>Hello, {name.title()}!</h1>')