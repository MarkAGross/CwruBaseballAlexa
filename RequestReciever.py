import sys

#Class for recieving and interpreting Amazon Alexa requests
class receiver:

    def __init__(self, inputstring):
        self.keywords = ["This", "is", "a", "test"]
        self.data = []
        self.inputstring = inputstring

    def parse_string(self):
        keywordslist = self.inputstring.split("_")
        for i in range(0, len(keywordslist)):
            for j in range(0, len(self.keywords)):
                if keywordslist[i] == self.keywords[j]:
                    self.data.append(keywordslist[i])
                    break

        
        #have that same method add the keywords to the array
        #method to fetch appropriate data (might be lots of copy paste)
