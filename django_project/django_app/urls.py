from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>",views.invite,name="invite")
    # path("",views.invite,name="invite")
    
]
