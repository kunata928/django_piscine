from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url("init/", views.init_table_movies),
    url("populate/", views.fill_data),
    url("display/", views.view_table),
]