from django.shortcuts import render
from django.http import HttpResponse

tasks = ["apple","microsoft","oracle"]

def lists(request):
    return render(request,"web/index.html",{
      "tasks":tasks  
    })
    

