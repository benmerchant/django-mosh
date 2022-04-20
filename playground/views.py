from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 11
    y = 42
    return x


def say_hello(request):
    x = calculate
    y = 2
    return render(request, 'hello.html', {'name': 'Benjo'})
    # return HttpResponse('Heyooooo World')
