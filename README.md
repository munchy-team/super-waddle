 # Developing Django on Repl.it

- Fork this template to get started
- do not start this incomplete code 

- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:
   # help !!!!!!!!!!
   #this exploded did'nt it
   idk me about to get very mad if my work go boom....
   #ok its all gone
   # AQRGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH go back nowwwwwwww#hhhhh
   # wait.
   
   #or is it check
   #no it broke git
   #but i see the folder called blog
   
```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

# didactic-waddle
