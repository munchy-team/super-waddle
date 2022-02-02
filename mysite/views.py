from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
  html = '<!-- <html><title>Munchy-Site | Super Website</title><p1><a href=/admin>Log in here</a>--> <h3 style=font-family:"Calibri";>       Home:</h3> <ul><li><form action="/admin">    <input type="submit" value="Log In" /></form></li><li><form action="https://munchy-site.herokuapp.com">    <input type="submit" value="Go to Super Website" /></form></li><li><form action="https://munchy-site.herokuapp.com/admin">    <input type="submit" value="Go to Super Website Log In" /></form></li><li><form action="https://replit.com">    <input type="submit" value="Go to Replit" /></form></li><li><form action="https://github.com/cs947939/didactic-waddle.git">    <input type="submit" value="Go to GitHub" /></form></li><li><form action="https://heroku.com">    <input type="submit" value="Go to Heroku" /></form></li><li><form action="https://data.heroku.com">    <input type="submit" value="Go to Heroku Data" /></form><li><form action="https://stackoverflow.com">    <input type="submit" value="Go to Stack Overflow" /></form></li><li><form action="https://w3schools.com">    <input type="submit" value="Go to W3 Schools" /></form></li><li><form action="https://www.djangoproject.com/">    <input type="submit" value="Go to Django Docs 4.0" /></form></li><li><form action="https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types">    <input type="submit" value="Go to Django Model Types" /></form></li></li><li><form action="/navigation">    <input type="submit" value="Go to Navigation Menu" /></form></li></li></ul> </p1></html>'
  return HttpResponse(html)

def home(request):
  return HttpResponse('This is the Updates Page')

def firstview(request):
  return HttpResponse('Our first view.py is up at 1:23PM')
def version(request):
  return HttpResponse('this is version 19')

def progress(request):
  return HttpResponse('this is the progress thingy')

def test(request):
  html = '<html> <title>this is a test page do whatever you want</title> <h1>THIS MUST WORKS!</h1> <h2>yes this works</h2> <h2><a href="https://droopylostmachinecode.codingproject101010101.repl.co/navigation/"> Go back to the Directory</a> </h2></html>'
  return HttpResponse(html)
#HEY TYPE YOUR PW IN COMMAND PROMPT
#okay
# over ride the warning!
  #done try now 
  #grrr
  #yeah 
  #stupid innternet
  #ready to send 
  # go ahead 
  # give me an idea for a ss presentation. 
  #about what 
  # ss
  # do one on japan
  # what are the issues on japan 
  #aging population
  #wait i will see. 
  # we should make a sign up page.
  # also i got to connect the links
def navigation(request):

  html = '<html> <title>Munchy-Site | Navigation</title> <h2>Navigation</h2><p>Or just go back to the <a href="/admin">log in</a> or <a href="/">home</a> page. </p><h3>/Progress</h3> <ul> <li><a href="#">Link 1</a> </li> <li><a href="#">Link 2</a> </li><li><a href="#">Link 3</a> </li></ul> </html>'
  return HttpResponse(html)

