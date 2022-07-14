from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')


def guests(request):
    return render(request, 'clients.html')    


def door(request):
    return render(request, 'leads.html')        