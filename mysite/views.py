from django.http import HttpResponse
from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploader.models import Document
from django.contrib.auth.decorators import login_required
from progress.models import Message


def home(request):
  messages = Message.objects.all().order_by('-Posted_At')
  return render(request, 'progress/home.html', {'messages': messages  })
  

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