from django.urls import path
from . import views

#

urlpatterns = [
path('munchy',views.munchy),
path('time',views.date),

]



