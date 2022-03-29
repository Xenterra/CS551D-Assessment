import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('deploy.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
#This will only run when the app is deployed, not when the pages are opened
conn.execute('DROP TABLE IF EXISTS allData')
print("Full data table dropped successfully");

# re-create tables
conn.execute('CREATE TABLE allData(university STRING,year INTEGER,rank_display INTEGER,score FLOAT,link TEXT,country TEXT,city TEXT,region TEXT,logo TEXT,type TEXT,research_output TEXT,student_faculty_ratio FLOAT,international_students INTEGER,size TEXT,faculty_count INTEGER)')
print("Full data table created successfully");

# open the file to read it into the database
with open('qs-world-university-rankings-2017-to-2022-V2.csv', newline='') as f:
	reader = csv.reader(f, delimiter=",")
	next(reader) # skip the header line
	for row in reader:
		print(row[0],row[1])
		university = row[0]
		year = row[1]
		rank_display = row[2]
		score = row[3]
		link = row[4]
		country = row[5]
		city = row[6]
		region = row[7]
		logo = row[8]
		type = row[9]
		research_output = row[10]
		student_faculty_ratio = row[11]
		international_students = row[12]
		size = row[13]
		faculty_count = row[14]

		cur.execute('INSERT INTO allData VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (university,year,rank_display,score,link,country,city,region,logo,type,research_output,student_faculty_ratio,international_students,size,faculty_count))    
print("data parsed successfully");
conn.commit()
conn.close()