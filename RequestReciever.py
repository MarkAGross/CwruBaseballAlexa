import sys

#Class for recieving and interpreting Amazon Alexa requests
class receiver:

    def __init__(self):
        self.keywords = ["This", "is", "a", "test"]

    def parse_string(inputstring):
        self.data = []
        keywordslist = inputstring.split("_")
        for i in range(0, len(keywordslist)):
            for j in range(0, len(keywords)):
                if keywordslist[i] == keywords[j]:
                    input.append(keywordslist[i])
                    break
        return data

    if __name__ == "__main__":
        inputstring = str(sys.argv)
        self.parse_string(inputstring)
        for i in range(len(input)):
            print (input[i])
        print ("done")
        #have that same method add the keywords to the array
        #method to fetch appropriate data (might be lots of copy paste)
