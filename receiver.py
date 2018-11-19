from RequestReciever import receiver
import sys

inputstring = "how many games has number 29 played in 2018"
r = receiver(inputstring)
print ("receiver created")
r.parse_string()
print (" ")
print ("done")
