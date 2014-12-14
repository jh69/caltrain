#!/usr/bin/python

import sys, csv, datetime, time

if len(sys.argv) == 1:
	print "specify a destination number. btw holiday schedules are not supported bc im lazy" \
	"\n01 = sf, 02 = 22nd street, 03 = bayshore" \
	"\n04 = south sf, 05 = san bruno, 06 = millbrae, 07 = broadway, 08 = burlingame" \
	"\n09 = san mateo, 10 = hayward park, 11 = hillsdale, 12 = belmont, 13 = san carlos" \
	"\n14 = redwood city, 15 = atherton, 16 = menlo park, 17 = palo alto, 19 = cal ave" \
	"\n20 = san antonio, 21 = mountain view, 22 = sunnyvale, 23 = lawrence" \
	"\n24 = santa clara, 25 = college park, 26 = san jose, 27 = tamien, 28 = capitol" \
	"\n29 = blossom hill, 30 = morgan hill, 31 = san martin, 32 = gilroy"
	exit()

if datetime.datetime.today().weekday() > 5:
	dayofweek = "Weekday"
elif datetime.datetime.today().weekday() == 5:
	dayofweek = "Saturday"
elif datetime.datetime.today().weekday() == 6:
	dayofweek = "Sunday"

currtime = time.strftime("%H:%M:00")
homestop = "21" #mv
destination = sys.argv[1]
stops = []
todaysstops = []
todaysstopsdeparting = []
todaysstopsboth = []
listoftrips = []
stopsatdestination = []
sortedlist = []
bounddir = ""

if int(destination) > int(homestop):
	bounddir = "2"
elif int(destination) < int(homestop):
	bounddir = "1"
else:
	print "some shit is fucked with your destinations. try again."
	exit()
	

print "It is", currtime[:5], "on a", dayofweek + \
". Next trains leaving for", destination, "are at:"

# get the whole damn timetable file

f = open("stop_times.txt", 'r')
reader = csv.reader(f)
for row in reader:
	stops.append(row)
f.close()

#get just today's timetable, throw it in todaysstops

for row in stops:
	#print row
	if dayofweek in row[0]:
		todaysstops.append(row)

#then find only trips with the destination stop present

for row in todaysstops:
	if "70" + destination + bounddir in row[3]:
		stopsatdestination.append(row)	
		listoftrips.append(row[0])

stopsatdestination = []

# grab entire trip schedule for trips that stop at the destination

for row in todaysstops:
	i = 0
	while i < len(listoftrips):
		if listoftrips[i] == row[0]:
			stopsatdestination.append(row)
		i = i + 1

# list stops at home stop + times for trips that match

for row in stopsatdestination:
	#print row
	if "70" + homestop + bounddir in row[3]:
		todaysstopsboth.append(row[1])

# sort the list of times by time, only display ones that are > current time

sortedlist = sorted(todaysstopsboth)
i = 0
while i < len(sortedlist):
	if currtime < sortedlist[i]:
		print sortedlist[i][:5],
	i = i + 1
