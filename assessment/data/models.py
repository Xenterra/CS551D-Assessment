from django.db import models

# Create your models here.
class UniversityList(models.Model):
	uniqueid = models.IntegerField(primary_key=True)
	university = models.CharField(max_length=30)
	year = models.IntegerField()
	rank_display= models.CharField(max_length=30)
	score = models.CharField(max_length=6)
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	region = models.CharField(max_length=30)
	type = models.CharField(max_length=30)

	class Meta:
		db_table = "universitylist"


class UniDetails(models.Model):
	uniqueid = models.IntegerField(primary_key=True)
	logo = models.CharField(max_length=30)
	link = models.CharField(max_length=30)
	research_output = models.CharField(max_length=30)
	student_faculty_ratio = models.CharField(max_length=30)
	international_students = models.CharField(max_length=30)
	size = models.CharField(max_length=30)
	faculty_count = models.IntegerField()
	
	class Meta:
		db_table = "unidetails"

class TestTable(models.Model):
	first_name = models.CharField(max_length=50, primary_key=True)
	age = models.IntegerField()

	class Meta:
		db_table = "testtable"