from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from testing import views as testing_views


#

urlpatterns = [
path('munchy',views.munchy),
path('time',views.date),
path('li',views.li),

]



