from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("/Users/pmelodi/PycharmProjects/pythonProject/day05/ex02")
from fill_create_table import create_table_ex02_movies, fill_table_ex02_movies
from collect_data import collect_data_from_table


def init_table_movies(request):
    return HttpResponse(str(create_table_ex02_movies()))


def fill_data(request):
    response = fill_table_ex02_movies()
    # for res in response:
    #     HttpResponse(str(res))
    return HttpResponse(str(response))


def view_table(request):
    record = collect_data_from_table()
    print(record)
    if record:
        return render(request, 'base.html', locals())
    else:
        return HttpResponse("error")
    return
    

# if __name__ == '__main__':
#     view_table()