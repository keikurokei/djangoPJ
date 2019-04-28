from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', 
        TemplateView.as_view(template_name='hello.html'),
        name='hello'),
     url(r'^index/$', views.index, name='index'),       
]