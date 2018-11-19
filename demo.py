from team import team
from team_participant import team_participant
from schedule import schedule
from RequestReciever import receiver
from response import response
from bs4 import BeautifulSoup
import urllib.request
import sys

inputstring = "how many games has number 29 played in 2018"
r = receiver(inputstring)                                   #create receiver class
data = []
print ("receiver created")
data = r.parse_string()                 #make array with data
print(data)
print(len(data))
resp = response()
print(len(data))
if(len(data) == 27):                    #print with respective method based on data size
    resp.teamResponse(data)
elif(len(data) == 33):
    resp.participantResponse(data)
elif(len(data) == 3):
    resp.scheduleResponse(data)
else:
    print("HERE")

print (" ")
print ("done")
