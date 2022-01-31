from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
  return HttpResponse('This works')

def home(request):
  return HttpResponse('This is the Updates Page')

def firstview(request):
  return HttpResponse('Our first view.py is up at 1:23PM')
def version(requset):
  return HttpResponse('this is version 18')