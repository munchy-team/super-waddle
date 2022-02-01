from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
  html = "<html><title>super website</title><p1>This Works</p1></html>"
  return HttpResponse(html)

def home(request):
  return HttpResponse('This is the Updates Page')

def firstview(request):
  return HttpResponse('Our first view.py is up at 1:23PM')
def version(request):
  return HttpResponse('this is version 19')

def progress(request):
  return HttpResponse('this is the progress thingy')