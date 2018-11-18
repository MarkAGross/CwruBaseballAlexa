import sys

#Class for recieving and interpreting Amazon Alexa requests
class receiver:

    def __init__(self, inputstring):
        self.essentialkeywords = ["team", "player number"]
        self.keywords = ["games", "at bats", "runs", "hits", "doubles", "triples", "home runs", "runs batted in", "extra base hits", "total bases", "walks", "hit by pitches", "strikeouts", "sacrifice flies", "sacrifice hits", "hits into double play", "stolen bases", "caught stealing", "batting average", "on base percentage", "slugging percentage", "earned run average", "shutouts", "at bats against", "batting average against", "home attendance", "home attendance average"]
        self.data = []
        self.inputstring = inputstring
        self.tosend = [len(self.keywords)]

    def parse_string(self):
        for i in range(0, len(self.keywords)):
            if self.keywords[i] in self.inputstring:
                #add in method calls for fetch methods here
                #if essential keywords called, call from those specific classes
                self.data.append(self.keywords[i]) #temporary for proof of concept

    
            

        
        #have that same method add the keywords to the array
        #method to fetch appropriate data (might be lots of copy paste)
