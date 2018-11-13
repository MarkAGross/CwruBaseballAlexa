from RequestReciever import receiver
import sys

inputstring = "This is not a test"
r = receiver(inputstring)
r.parse_string()
for i in range(len(r.data)):
    print (r.data[i])
print ("done")
