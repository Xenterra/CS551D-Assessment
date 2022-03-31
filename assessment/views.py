from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import psycopg2
import csv
import os
from psycopg2 import Error
from assessment.data.models import TestTable, UniversityList, UniDetails

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == "POST":
        print("POST TEST")
        return render(request, "search.html")
    return render(request, "search.html")

def selected(request):
    return render(request, "selected.html")

def tester(request):
    #UniversityList.objects.all().delete()
    #
    #with open('qs-world-university-rankings-2017-to-2022-V2.csv', newline='') as f:
    #    reader = csv.reader(f, delimiter=",")
    #    next(reader) # skip the header line
    #    for row in reader:
    #    	uList = UniversityList.objects.create(
    #    	uniqueid = row[0],
    #    	university = row[1],
    #    	year = row[2],
    #    	rank_display= row[3],
    #    	score = row[4],
    #    	country = row[6],
    #    	city = row[7],
    #    	region = row[8],
    #    	type = row[10],
    #    	)
    #    	uList.save()
    res=""
    #Read ALL entries
    objects = UniversityList.objects.all()
    res ='Printing all Dreamreal entries in the DB : <br>'
    
    for elt in objects:
        res += str(elt.university)+"<br>"
    ##Read a specific entry:
    #sorex = UniversityList.objects.get(uniqueid = "3")
    #res += 'Printing One entry <br>'
    #res += sorex.university

    return HttpResponse(res)
