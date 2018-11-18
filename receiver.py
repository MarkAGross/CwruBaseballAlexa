from RequestReciever import receiver
import sys

inputstring = "how many games has number 39 played in 2018"
r = receiver(inputstring)
r.parse_string()
for i in range(len(r.data)):
    print (r.data[i], end = " ")
print (" ")
print ("done")
