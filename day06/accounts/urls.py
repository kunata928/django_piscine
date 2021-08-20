from django.urls import path

from .views import registrate

urlpatterns = [
    path('signup/', registrate, name='signup')
]