from django.urls import path, include

urlpatterns = [
    path('ex00/', include('ex00.urls')),
    path('ex02/', include('ex02.urls')),
]
