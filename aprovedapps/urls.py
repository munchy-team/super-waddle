from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('munchy', TemplateView.as_view(template_name="publish.htm")),

]
         