
from django.shortcuts import render
from django.http import HttpResponse



def data(request):
    return HttpResponse("<h1>DATA в Django проекте</h1>")

def test(request):
    return HttpResponse("<h1>TEST в Django проекте</h1>")