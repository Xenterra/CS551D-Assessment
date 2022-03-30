from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import psycopg2
from psycopg2 import Error

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def selected(request):
    return render(request, "selected.html")