
from RequestReciever import receiver
from response import response



inputstring = "games 2018"
inputstring2 = "doubles 29 2018"
inputstring3 = "previous game"
inputstring4 = ""


r = receiver(inputstring)                                   #create receiver class
data = []

data = r.parse_string()                 #make array with data

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

data2 = r2.parse_string()                 #make array with data

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

data3 = r3.parse_string()                 #make array with data
#print(data3)
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

data4 = r4.parse_string()                 #make array with data

resp4 = response()
if(len(data4) == 28):                    #print with respective method based on data size
    resp.teamResponse(data4)
elif(len(data4) == 33):
    resp.participantResponse(data4)
elif(len(data4) == 3):
    resp.scheduleResponse(data4)
else:
    print("Missed array length")


print (" ")
print ("done")
