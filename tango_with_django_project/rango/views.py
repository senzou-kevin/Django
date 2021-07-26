from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    aboutpage = "<a href='/rango/About/'>About</a>"
    return HttpResponse("Rango says hey there partner!"+aboutpage)


def about(request):
    indexpage = '<a href=\'/rango/\'>Index</a>'
    return HttpResponse("Rango says here is the about page. "+indexpage)
