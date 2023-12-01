from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def home(request):
    return render(request,"base.html")
def result(request):
    return render(request,"index.html")
            

