from django.shortcuts import render
from django.http import HttpResponse
import datetime


def date(request):
    now = datetime.datetime.now()
    return render(request,"newyear/index.html" ,{
        "Monday": True
    })
