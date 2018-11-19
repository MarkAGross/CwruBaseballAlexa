from team import team
from team_participant import team_participant
from schedule import schedule
from RequestReciever import receiver
from response import response
import sys

inputstring = "how many games has number 29 played in 2018"
r = receiver(inputstring)                                   #create receiver class
data = []
print ("receiver created")
data = r.parse_string()                 #make array with data
resp = response()
if(len(data) == 28):                    #print with respective method based on data size
    resp.teamResponse(data)
elif(len(data) == 33):
    resp.participantResponse(data)
elif(len(data) == 3):
    resp.scheduleResponse(data)
print (" ")
print ("done")
