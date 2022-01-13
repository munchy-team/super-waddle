from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hel.") # this does work question is the views in progress