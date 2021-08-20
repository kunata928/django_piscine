from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url("django/", views.django, name='django'),
    url("display/", views.display, name='display'),
    url("templates/", views.templates, name='templates')
]