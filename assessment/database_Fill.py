import csv
import os
from pathlib import Path
from django.db import models
from assessment.data.models import UniversityList, UniDetails

UniversityList.objects.all().delete()
UniDetails.objects.all().delete()

# Refill the model database
UniversityList.objects.all().delete()
with open('qs-world-university-rankings-2017-to-2022-V2.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
    	uList = UniversityList.objects.create(
        print(uniqueid + "complete"),
    	uniqueid = row[0],
    	university = row[1],
    	year = row[2],
    	rank_display= row[3],
    	score = row[4],
    	country = row[6],
    	city = row[7],
    	region = row[8],
    	type = row[10],
    	)
    	uList.save()
        
    print("Universtiy List Complete")

UniDetails.objects.all().delete()
with open('qs-world-university-rankings-2017-to-2022-V2.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        uList2 = UniDetails.objects.create(
        uniqueid = row[0],
        link = row[5],
        logo = row[9],
        research_output = row[11],
        student_faculty_ratio = row[12],
        international_students = row[13],
        size= row[14],
        faculty_count = row[15],
        )
        print("Entry for", str(row[0]), "complete")
        uList2.save()
    print("Details List Complete")