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
    resultList = []
    if request.method == "POST":
        print(request.POST)
        selection = request.POST.get('Selection','')
        #print(selection)
        test  = UniversityList.objects.get(uniqueid=selection)
        test2 = UniDetails.objects.get(uniqueid=selection)
        resultList = [str(test.uniqueid),str(test.university),str(test.rank_display),str(test.score),str(test.country),str(test.year),str(test.city),str(test.region),str(test.type),str(test2.logo), str(test2.link), str(test2.research_output), str(test2.student_faculty_ratio), str(test2.international_students), str(test2.size), str(test2.faculty_count)]
        print(resultList)
        context = {"output" : resultList,}
        return render(request, "selected.html", context)

    return render(request, "selected.html")

def compare(request):
    return render(request, "compare.html")

def tester(request):
    res=''

    ##Read ALL entries
    #objects = UniversityList.objects.all()
    #res ='Printing all University entries in the DB : <br>'
    #for elt in objects:
    #    res += str(elt.university)+"<br>"    

    return HttpResponse(res)
