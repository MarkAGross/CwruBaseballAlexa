import unittest
from receiver import receiver
from RequestReceiver import receiver

#draft (not done)
class RequestReceiverTester(unittest.TestCase):

    print ("Testing requests")

    def test_team_request(self):
        inputstring = "How many games did the team play in 2018?"
        rteam = receiver(inputstring)
        data = []
        data = rteam.parse_string()
        correctout = []
        assertEqual(correctout, data, "The correct number of games team played was not fetched")

    def test_team_participant_request(self):
        inputstring = "How many games has number 29 played in 2018?"
        rpart = receiver(inputstring)
        data = []
        data = rpart.parse_string()
        correctout = [] ##
        assertEqual(correctout, data, "The correct number of games for a specific player was not fetched")

    def test_schedule_request(self):
        inputstring = "What game was played on April 25 2018?"
        rsched = receiver(inputstring)
        data = []
        data = rsched.parse_string()
        correctout = [] ##
        assertEqual(correctout, data, "The correct return game was not fetched")

    def test_no_input_with_year(self):
        inputstring = "This has nothing to do with baseball 2018"
        r = receiver(inputstring)
        data = []
        data = r.parse_string()
        correctout = [] ##
        assertEqual(correctout, data, "More output than just the year was given")

    def test_no_input(self):
        inputstring = "I like spaghetti"
        r = receiver(inputstring)
        data = []
        data = r.parse_string()
        correctout = [] ##
        assertEqual(correctout, data, "Output was given when none should have been")
                

        
        
