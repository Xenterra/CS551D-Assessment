from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import psycopg2
import csv
import os
from psycopg2 import Error
from assessment.data.models import TestTable, UniversityList, UniDetails
from django.db import connection

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    resultList = []
    if request.method == "POST":
        #print(request.POST)
        crit = request.POST.get('criteria','')
        sear = request.POST.get('search','')
        #print(crit, sear)
        res = ""
        newValue = []
        context = { }
        if sear == "university":
            for x in UniversityList.objects.filter(university=crit):
                print(x.uniqueid , x.university)
                newValue = [str(x.uniqueid) , str(x.university), str(x.score),str(x.country),str(x.city),str(x.region),str(x.type)]
                resultList.append(newValue)
                context = {
                    "output" : resultList,
                }
        elif sear == "rank_display":
            for x in UniversityList.objects.filter(rank_display=crit):
                print(x.uniqueid , x.university)
                newValue = [str(x.uniqueid) , str(x.university), str(x.score),str(x.country),str(x.city),str(x.region),str(x.type)]
                resultList.append(newValue)
                context = {
                    "output" : resultList,
                }
        elif sear == "country":
            for x in UniversityList.objects.filter(country=crit):
                print(x.uniqueid , x.university)
                newValue = [str(x.uniqueid) , str(x.university), str(x.score),str(x.country),str(x.city),str(x.region),str(x.type)]
                resultList.append(newValue)
                context = {
                    "output" : resultList,
                }
        elif sear == "region":
            for x in UniversityList.objects.filter(region=crit):
                print(x.uniqueid , x.university)
                newValue = [str(x.uniqueid) , str(x.university), str(x.score),str(x.country),str(x.city),str(x.region),str(x.type)]
                resultList.append(newValue)
                context = {
                    "output" : resultList,
                }
        elif sear == "score":
            for x in UniversityList.objects.filter(score=crit):
                print(x.uniqueid , x.university)
                newValue = [str(x.uniqueid) , str(x.university), str(x.score),str(x.country),str(x.city),str(x.region),str(x.type)]
                resultList.append(newValue)
                context = {
                    "output" : resultList,
                }
        print(res)
        return render(request, "search.html", context)
    print(request.GET)
    context = {"output" : resultList,}
    return render(request, "search.html",context)

def selected(request):
    return render(request, "selected.html")

def tester(request):
    res=""
    ## Refill the model database
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

    #Read ALL entries
    objects = UniversityList.objects.all()
    res ='Printing all University entries in the DB : <br>'
    
    for elt in objects:
        res += str(elt.university)+"<br>"
    ##Read a specific entry:
    

    return HttpResponse(res)
