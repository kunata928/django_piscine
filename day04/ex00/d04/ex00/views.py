from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ex00(request):
    # return HttpResponse('Response')
    return render(request, "index.html")
    