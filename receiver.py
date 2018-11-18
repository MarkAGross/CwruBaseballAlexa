from RequestReciever import receiver
import sys

inputstring = "games at bats runs hits not in don't pick me"
r = receiver(inputstring)
r.parse_string()
for i in range(len(r.data)):
    print (r.data[i], end = " ")
print (" ")
print ("done")
