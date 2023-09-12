from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse

def registration(request):
    ERFO=RegistrtionForm()
    d={'ERFO':ERFO}
    if request.method=="POST":
        DRFO=RegistrtionForm(request.POST)
        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))

    return render (request,'registartion.html',d)