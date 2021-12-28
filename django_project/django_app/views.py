from django.shortcuts import render
from django.http import HttpResponse


def invite(request,name):
    # return HttpResponse(f"Hello, {name}!")
    return render(request,"hello/index.html", {
        "name":name.upper()
    })


