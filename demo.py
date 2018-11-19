from team import team
from team_participant import team_participant
from schedule import schedule
from RequestReciever import receiver
from response import response
from bs4 import BeautifulSoup
import urllib.request
import sys
import datetime
import calendar

inputstring = "how many games has number 29 played in 2018"
inputstring2 = "How many runs did the team get in 2018"
inputstring3 = "What is the next game played"
inputstring4 = "This has nothing to do with baseball 2018"
inputstring5 = "I like spaghetti"

r = receiver(inputstring)                                   #create receiver class
data = []
print ("receiver created")
data = r.parse_string()                 #make array with data
print(data)
print(len(data))
resp = response()
if(len(data) == 28):                    #print with respective method based on data size
    resp.teamResponse(data)
elif(len(data) == 33):
    resp.participantResponse(data)
elif(len(data) == 3):
    resp.scheduleResponse(data)
else:
    print("Missed array length")



r2 = receiver(inputstring2)                                   #create receiver class
data2 = []
print ("receiver created")
data2 = r2.parse_string()                 #make array with data
print(data2)
print(len(data2))
resp2 = response()
if(len(data2) == 28):                    #print with respective method based on data size
    resp.teamResponse(data2)
elif(len(data2) == 33):
    resp.participantResponse(data2)
elif(len(data2) == 3):
    resp.scheduleResponse(data2)
else:
    print("Missed array length")

r3 = receiver(inputstring3)                                   #create receiver class
data3 = []
print ("receiver created")
data3 = r3.parse_string()                 #make array with data
print(data3)
print(len(data3))
resp3 = response()
if(len(data3) == 28):                    #print with respective method based on data size
    resp.teamResponse(data2)
elif(len(data3) == 33):
    resp.participantResponse(data2)
elif(len(data3) == 3):
    resp.scheduleResponse(data3)
else:
    print("Missed array length")

r4 = receiver(inputstring4)                                   #create receiver class
data4 = []
print ("receiver created")
data4 = r4.parse_string()                 #make array with data
print(data4)
print(len(data4))
resp4 = response()
if(len(data4) == 28):                    #print with respective method based on data size
    resp.teamResponse(data4)
elif(len(data4) == 33):
    resp.participantResponse(data4)
elif(len(data4) == 3):
    resp.scheduleResponse(data4)
else:
    print("Missed array length")

r5 = receiver(inputstring5)                                   #create receiver class
data5 = []
print ("receiver created")
data5 = r5.parse_string()                 #make array with data
print(data5)
print(len(data5))
resp5 = response()
if(len(data5) == 28):                    #print with respective method based on data size
    resp.teamResponse(data5)
elif(len(data5) == 33):
    resp.participantResponse(data5)
elif(len(data5) == 3):
    resp.scheduleResponse(data5)
else:
    print("Missed array length")

print (" ")
print ("done")
