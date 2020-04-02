from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def mark(request):
    return HttpResponse('<h1> Your mark is 0 </h1>')

def count(request):
    return render(request, 'mycount.html')
