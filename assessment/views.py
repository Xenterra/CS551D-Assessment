from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import csv
import os
from assessment.data.models import TestTable, UniversityList, UniDetails
from django.db import connection

# Create your views here.
def index(request):
    if request.method == "POST":
        resultList1=[]
        resultList2=[]
        finalList=[]
        count=[]
        for x in UniversityList.objects.all():
            newValue1 = [str(x.uniqueid),str(x.university),str(x.rank_display),str(x.score),str(x.country),str(x.year),str(x.city),str(x.region),str(x.type)]
            resultList1.append(newValue1)
            count.append(int(x.uniqueid))
        for y in UniDetails.objects.all():
            newValue2 = [str(y.logo), str(y.link), str(y.research_output), str(y.student_faculty_ratio), str(y.international_students), str(y.size), str(y.faculty_count)]
            resultList2.append(newValue2)

        for z in count:
            finalList.append(resultList1[z-1]+resultList2[z-1])

        print(finalList[0])
        print(finalList[1])
        context = { "output1"   : finalList,
                    "lock"      : ["x"],}

        return render(request, "index.html", context)
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
        dataPull  = UniversityList.objects.get(uniqueid=selection)
        dataPull2 = UniDetails.objects.get(uniqueid=selection)
        resultList = [str(dataPull.uniqueid),str(dataPull.university),str(dataPull.rank_display),str(dataPull.score),str(dataPull.country),str(dataPull.year),str(dataPull.city),str(dataPull.region),str(dataPull.type),str(dataPull2.logo), str(dataPull2.link), str(dataPull2.research_output), str(dataPull2.student_faculty_ratio), str(dataPull2.international_students), str(dataPull2.size), str(dataPull2.faculty_count)]
        #print(resultList)
        context = {"output" : resultList,}
        return render(request, "selected.html", context)

    return render(request, "selected.html")

def compare(request):
    if request.method == "POST":
        uni1 = request.POST.get('uni1','')
        uni2 = request.POST.get('uni2','')
        if (uni1 != "" and uni2 != ""):
            dataPull  = UniversityList.objects.get(uniqueid=uni1)
            dataPull2 = UniDetails.objects.get(uniqueid=uni1)
            resultList1 = [str(dataPull.uniqueid),str(dataPull.university),str(dataPull.rank_display),str(dataPull.score),str(dataPull.country),str(dataPull.year),str(dataPull.city),str(dataPull.region),str(dataPull.type),str(dataPull2.logo), str(dataPull2.link), str(dataPull2.research_output), str(dataPull2.student_faculty_ratio), str(dataPull2.international_students), str(dataPull2.size), str(dataPull2.faculty_count)]
            dataPull  = UniversityList.objects.get(uniqueid=uni2)
            dataPull2 = UniDetails.objects.get(uniqueid=uni2)
            resultList2 = [str(dataPull.uniqueid),str(dataPull.university),str(dataPull.rank_display),str(dataPull.score),str(dataPull.country),str(dataPull.year),str(dataPull.city),str(dataPull.region),str(dataPull.type),str(dataPull2.logo), str(dataPull2.link), str(dataPull2.research_output), str(dataPull2.student_faculty_ratio), str(dataPull2.international_students), str(dataPull2.size), str(dataPull2.faculty_count)]
            context = {
                "output1" : resultList1,
                "output2" : resultList2,
                "lock"      : ["x"],
            }
            return render(request, "compare.html", context)
        else:
            return render(request, "compare.html")
    return render(request, "compare.html")

def tester(request):
    res=''

    ##Read ALL entries
    #objects = UniversityList.objects.all()
    #res ='Printing all University entries in the DB : <br>'
    #for elt in objects:
    #    res += str(elt.university)+"<br>"    

    return HttpResponse(res)
