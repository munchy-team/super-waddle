\


"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#hello whats up hello hello hello hello hello 
# hello  i am too confused, brain is boiling from failing local code.
# have you looked up guides about this topic ones with code you can copy and paste
# yes none of them work. :((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
# this idea may need to be thrown out because of headache and trouble
# idk i remember doing something like this, and it eventually worked, but now :((((((((((()))))))))))
#yeah no idea but this is a different enviorment for coding and things are diiferent here and we lots of things to learn 
# agreed. i wanted you to look at this warning and see what it tries to say. 
# what?




from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from Uploads import views

#from django.conf.urls import url

# from mysite import settings






from . import views


from django.views.generic import TemplateView
admin.site.site_header= "Project Progress Website V"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('home', views.home),
    path('firstview', views.firstview),
    path('progress', views.progress),
    path('progress/', include('progress.urls')),
    path('test/', views.test),
    path('navigation/', views.navigation),
    path('links/', views.navigation),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^main/$', views.main, name='main'),
    url(r'^downloads/$', views.simple_upload, name='simple_upload'),

]
if settings.DEBUG==True:
   urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
   #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
 # how can we implement this: https://www.youtube.com/watch?v=v5FWAxi5QqQ look at timestamp 7:18. I dont know how to implement that in html. #no idea help 
  
    
    #path('home/', ) # this wont work i think.
  

    

       
