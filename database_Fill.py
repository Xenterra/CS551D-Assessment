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
conn.execute('CREATE TABLE allData(uniqueid INTEGER PRIMARY KEY,university STRING,year INTEGER,rank_display INTEGER,score FLOAT,link TEXT,country TEXT,city TEXT,region TEXT,logo TEXT,type TEXT,research_output TEXT,student_faculty_ratio FLOAT,international_students INTEGER,size TEXT,faculty_count INTEGER)')
print("Full data table created successfully");

# open the file to read it into the database
with open('qs-world-university-rankings-2017-to-2022-V2.csv', newline='') as f:
	reader = csv.reader(f, delimiter=",")
	next(reader) # skip the header line
	for row in reader:
		print(row[0],row[1])
		uniqueid = row[0]
		university = row[1]
		year = row[2]
		rank_display = row[3]
		score = row[4]
		link = row[5]
		country = row[6]
		city = row[7]
		region = row[8]
		logo = row[9]
		type = row[10]
		research_output = row[11]
		student_faculty_ratio = row[12]
		international_students = row[13]
		size = row[14]
		faculty_count = row[15]

		cur.execute('INSERT INTO allData VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (uniqueid, university,year,rank_display,score,link,country,city,region,logo,type,research_output,student_faculty_ratio,international_students,size,faculty_count))    
print("data parsed successfully");
conn.commit()
conn.close()