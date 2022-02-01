from django.shortcuts import render
from django.http import HttpResponse
import datetime
#here to stopme?
def munchy(request):
  return HttpResponse('this is working hahaahhahahaaahahahaahahahahahahah also pay me money ')
  
def date(request):
  now = datetime.datetime.now()
  html = "<html><body>it is %snhtml>"% now
  return HttpResponse(html)
def li(request):
  html = '<html><title>Li did this</title></html>'
  return HttpResponse(html)
