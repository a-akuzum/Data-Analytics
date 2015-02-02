import sqlite3
conn = sqlite3.connect('project2.db')

filename= "solarareadata.txt"
inputFile = open(filename, 'r')


c = conn.cursor()

######################################################
# Create tables
######################################################
c.execute('DROP TABLE IF EXISTS Sites')
c.execute('''CREATE TABLE Sites
             (siteID INTEGER PRIMARY KEY AUTOINCREMENT, siteName TEXT, siteAddress TEXT, siteCity TEXT)''')

c.execute('DROP TABLE IF EXISTS Panels')
c.execute('''CREATE TABLE Panels
             (panelID INTEGER PRIMARY KEY AUTOINCREMENT, siteID INTEGER, panelNumber INTEGER)''')
             
c.execute('DROP TABLE IF EXISTS Watts')
c.execute('''CREATE TABLE Watts
             (PanelWattsID INTEGER PRIMARY KEY AUTOINCREMENT, panelID INTEGER, panelWatts TEXT, dateTime TEXT)''')

#c.execute('DROP TABLE IF EXISTS Sensors')             
#c.execute('''CREATE TABLE Sensors
#             (sensorID INTEGER PRIMARY KEY AUTOINCREMENT, siteID INTEGER, panelID INTEGER, sensorNumber INTEGER)''')

c.execute('DROP TABLE IF EXISTS SensorReadings')
c.execute('''CREATE TABLE SensorReadings
             (readingID INTEGER PRIMARY KEY AUTOINCREMENT, sensorID INTEGER, sensorTemp INTEGER, sensorIrrad INTEGER, dateTime TEXT)''')
             
######################################################

             
for line in inputFile:
	if 'PanelWatts' in line:
		continue
	print line
	
	fields = line.split(',')
	siteName = fields[0]
	siteAddress = fields[1]
	siteCity = fields[2]
	panelNumber = fields[3]
	panelWatts = fields[4]
	sensorNumber = fields[5]
	sensorTemp = fields[6]
	sensorIrrad = fields[7]
	date = fields[8]
	time = fields[9]

	
	# NW-Vista,100AeroSt,Boerne,1,0,10,40,3,2000-01-01,00:00
	sqlQuery = "SELECT siteName FROM Sites"
	c.execute(sqlQuery)
	resultSiteNames = c.fetchall()
	found = False
	
	for s in resultSiteNames:
		if siteName in s:
			found = True
	
	# Insert a row of data
	if not found :
		sqlQuery = "INSERT INTO Sites VALUES (NULL,\""+siteName+"\",\""+siteAddress+"\",\""+siteCity+"\")"
		print sqlQuery
		c.execute(sqlQuery)

	# Get SiteID from Table SiteName
	sqlQuery = "SELECT siteID FROM Sites WHERE siteName=\""+siteName+"\""
	c.execute(sqlQuery)
	res=c.fetchone()
	print res[0]		# siteID of siteName
	siteID = res[0]

	sqlQuery = "SELECT panelNumber FROM Panels WHERE siteID = "+str(siteID)
	c.execute(sqlQuery)
	resultPanelNums = c.fetchall()
	found = False
	
	for p in resultPanelNums:
		print "p[0]"+ str(p[0])
		print "panelnum: "+ panelNumber
		if panelNumber == str(p[0]):
			found = True
	
	# insert into Panels Table	
	if not found:
		sqlQuery = "INSERT INTO Panels VALUES (NULL,"+str(siteID)+","+panelNumber+")"
		print sqlQuery
		c.execute(sqlQuery)

	#Watts Table (panelID INTEGER, panelWatts TEXT)
	sqlQuery = "SELECT panelID FROM Panels WHERE siteID = "+str(siteID)+" and panelNumber = "+ str(panelNumber)
	c.execute(sqlQuery)
	resPanelID = c.fetchone()

	panelID = resPanelID[0]
	print "current PanelID found from last: "+str(panelID)


##################################################

	sqlQuery = "SELECT panelWatts FROM Watts WHERE panelWatts = "+str(panelWatts)+" and panelID = "+ str(panelID)
	c.execute(sqlQuery)
	resultPanelWatts = c.fetchone()
	print "q= " +sqlQuery

	found=False

	if resultPanelWatts is None :
		found=False	
	else:
		print "resultPanelWatts: "+ str(resultPanelWatts[0])
		found = True
	
	# insert into Watts Table if panelWatts is not inserted into the table before
	if not found:
		sqlQuery = "INSERT INTO Watts VALUES (NULL,"+str(resPanelID[0])+","+str(panelWatts)+",\""+date+" "+ time+"\")"
		print "Panels Watts Insert Querry: "+ sqlQuery
		c.execute(sqlQuery)

######################################################
	sensorID = 0	
	# Calculate SensorID using SensorNumber, PanelID
	if (int(sensorNumber) / 10) % 2 == 0:
		sensorID = panelID*2
	else:
		sensorID = (panelID*2) -1

	# Insert Into  SensorReadings table
#(readingID INTEGER PRIMARY KEY AUTOINCREMENT, sensorID INTEGER, sensorTemp INTEGER, sensorIrrad INTEGER, dateTime TEXT)
	sqlQuery = "INSERT INTO SensorReadings VALUES (NULL,"+str(sensorID)+","+str(sensorTemp)+","+str(sensorIrrad)+",\""+date+" "+ time+"\")"
	print "SensorReadingQ = "+ sqlQuery
	c.execute(sqlQuery)

######################################################


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

######################################################THE END######################################################
'''

# 2.sorunun 1'u
# What is the average monthly temperature for each of the four sites

# SELECT avg(sensorTemp) FROM SensorReadings GROUP BY sensorID
#import math
#mySiteID = math.ceil( float(sensorID) / 8)

################ Monthly average for site 1, (3 months)#####################################
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01'
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';


################ Monthly average for site 2, (3 months)#####################################
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';



################ Monthly average for site 3, (3 months)#####################################
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';



################ Monthly average for site 4, (3 months)#####################################
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT avg(sensorTemp) AS Site1Average FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';



#############################################################################################################################
2.2 				 (!!!!!! sensorID leri degistir !!!!!!!!!!! )
( site #1 )
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';


( site #2 )
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';

( site #3 )
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';

( site #4 )
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT dateTime, max(sensorIrrad) FROM SensorReadings WHERE sensorID>=1 and sensorID <= 8 and dateTime BETWEEN '2000-03-01' and '2000-04-01';


#############################################################################################################################
# 2.sorunun 3'u   (!!!!!! panelID leri degistir !!!!!!!!!!! )
( site#1 )
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-03-01' and '2000-04-01';


( site#2 )
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-03-01' and '2000-04-01';

( site#3 )
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-03-01' and '2000-04-01';

( site#4 )
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-02-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-02-01' and '2000-03-01';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-03-01' and '2000-04-01';





(	site#1, per day == per month, because readings are taken the first day of each month )

SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-01-02';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-01-02';
SELECT sum(panelWatts) FROM Watts WHERE panelID>=1 and panelID <= 4 and dateTime BETWEEN '2000-01-01' and '2000-01-02';




sqlQuery = 
c.execute(sqlQuery)
res = c.fetchone()
res[0]			------> plot this value;


'''
