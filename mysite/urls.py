


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





from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from uploader import views

#from django.conf.urls import url

# from mysite import settings






from . import views


from django.views.generic import TemplateView
admin.site.site_header= "Project Progress Website"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.realhomepage),
    #path('', TemplateView.as_view(template_name="homepage.html"), name="realhomepage"),
    path('old-home', TemplateView.as_view(template_name="Home.html")),
    path('home', views.home),
    path('firstview', TemplateView.as_view(template_name="firstview.html")),
    path('progress', views.progress),
    path('progress/', include('progress.urls')),
    path('test/', views.test),
    path('navigation/', views.navigation),
    path('links/', views.navigation),
   path('veriosn', TemplateView.as_view(template_name="versions.html")),
   path('accounts/', include('allauth.urls')),
    re_path(r'^theuploader/$', views.main, name='main'),
    #url(r'/^$', views.main, name='main'),
    re_path(r'^uploader/media/$', views.simple_upload, name='simple_upload'),
    path('dev-tools', TemplateView.as_view(template_name="dev-tools.html")), 
    path('navigation', TemplateView.as_view(template_name="navigation.html")),
    path('navigation/specific-header', TemplateView.as_view(template_name="specific-header.html")),
    path('ml/', TemplateView.as_view(template_name="logedin.html")),
  path('CSerror', views.CSRF_ERROR),
  path('munchy2', TemplateView.as_view(template_name="logon2.html")),
  path('munchy3', TemplateView.as_view(template_name="logon3.html"))
   # url(r'^upload-tool/$', views.main, name='main'),
  #  url(r'^uploader/media/$', views.simple_upload, name='simple_upload'),
   # url(r'^media/documents/test.txt$', views.main, name='simple_upload'),
   # url(r'^main/$', views.main, name='main'),
   # url(r'^downloads/$', views.simple_upload, name='simple_upload'),

]
if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
   #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 # how can we implement this: https://www.youtube.com/watch?v=v5FWAxi5QqQ look at timestamp 7:18. I dont know how to implement that in html. #no idea help 
  
    
    #path('home/', ) # this wont work i think.
  

    

       
