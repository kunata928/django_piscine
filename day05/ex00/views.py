from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("/Users/pmelodi/PycharmProjects/pythonProject/day05/ex00")
from try_connect import try_connect
# import psycopg2
# from psycopg2 import Error


def create_table(request):
    return HttpResponse(str(try_connect()))