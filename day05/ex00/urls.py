from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url("init/", views.create_table),
]