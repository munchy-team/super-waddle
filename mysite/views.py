from django.db import models
from django.http import HttpResponse
from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploader.models import Document
from django.contrib.auth.decorators import login_required
from progress.models import Availability, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from munchyblog.models import HomeBlog
#from munchyblog.models import models
#from munchyblog.models import HomeBlog
##from munchyblog.models import Title
#from munchyblog.models import Date
#from munchyblog.models import Author
##from munchyblog.models import Header1
#from munchyblog.models import Paragraph1
#from munchyblog.models import Second_Paragraph
#from munchyblog.models import Header2
#from munchyblog.models import Paragraph2
#from munchyblog.models import Header2_Second_Paragraph
#from munchyblog.models import Header3
#from munchyblog.models import Paragraph3
#from munchyblog.models import Header3_Second_Paragraph
from django.core.paginator import Paginator
from apps.models import MunchyApp

admin.site.login = login_required(admin.site.login)

def home(request):
    homeblogs = HomeBlog.objects.all().order_by('-Date')

    homeblog_paginator = Paginator(homeblogs, 4)

   # page = homeblog_paginator.get_page(1)

   # context = {
    #    'count' : homeblog_paginator.count,
     ##  }
  #  posttitles = Title.objects.all()
   # dates = Date.objects.all()
   # authors = Author.objects.all()
   ## header1s = Header1.objects.all()
   # paragraph1s = Paragraph1.objects.all()
   # secondparagraphs = Second_Paragraph.objects.all()
   # header2s = Header2.objects.all()
   # paragraph2s = Paragraph2.objects.all()
   # header2secondparagraphs = Header2_Second_Paragraph.objects.all()
   # header3s = Header3.objects.all()
   # paragraph3s = Paragraph3.objects.all()
   # header3secondparagraphs = Header3_Second_Paragraph.objects.all()

    return render(request, 'progress/home3.html', {'homeblogs':homeblogs})#{'posttitles': posttitles, 'dates':dates, 'authors':authors,
                                                  #'header1s':header1s, 'paragraph1s':paragraph1s,'secondparagraphs':secondparagraphs,
                                                  #'header2s':header2s,'paragraph2s':paragraph2s,'header2secondparagraphs':header2secondparagraphs,'header3s':header3s,
                                                  #'paragraph3s':paragraph3s,'header3secondparagraphs':header3secondparagraphs
                                                  #})
                                                  #})
@login_required
def account_holder(request):
    	return render(request, "users.html")


def munchy_blog_post(request):
        homeblogs = HomeBlog.objects.all().order_by('-Date')
        return render(request, "blog_post.html",  {'homeblogs':homeblogs})
def munchy_apps(request):
        munchyapps = MunchyApp.objects.all()
        return render(request, "munchy_apps.html", {'munchyapps':munchyapps})
def realhomepage(request):
  availabilitys = Availability.objects.all()
  messages = Message.objects.all().order_by('-Posted_At')
  return render(request, 'progress/homepage.html', {'messages': messages, 'availabilitys' : availabilitys })

# class MessageDelete(DeleteView):
#    model = Message
#    success_url = reverse_lazy('messages')
  

def firstview(request):
  return HttpResponse('Our first view.py is up at 1:23PM')
def version(request):
  return HttpResponse('this is version 19')

def progress(request):
  return HttpResponse('this is the progress thingy')
def ml(request):
  return HttpResponse('you are logged in')

def test(request):
  html = '<html> <title>this is a test page do whatever you want</title> <h1>THIS MUST WORKS!</h1> <h2>yes this works</h2> <h2><a href="/navigation/"> Go back to the Directory</a> </h2></html>'
  return HttpResponse(html)

def munchy404(request, exception):
  return render(request, 'errorPage404.html')
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

  #html = '<html> <title>Munchy-Site | Navigation</title> <h2>Navigation</h2><p>Or just go back to the <a href="/admin">log in</a> or <a href="/">home</a> page. </p><h3>/Progress</h3> <ul> <li><a href="#">Link 1</a> </li> <li><a href="#">Link 2</a> </li><li><a href="#">Link 3</a> </li></ul> </html>'
  return HttpResponse()
def main(request):
    documents = Document.objects.all()
    return render(request, 'uploader/main.html', { 'documents': documents })

@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploader/uploading.html', {
            'uploaded_file_url': uploaded_file_url
        })


    return render(request, 'uploader/uploading.html')

def dev_tools(request):
    return HttpResponse()

def CSRF_ERROR(request):
  return HttpResponse('bad error hahahahahahahahahahahahah')