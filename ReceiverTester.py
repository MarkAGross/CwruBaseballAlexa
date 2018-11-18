import unittest
from receiver import receiver
from RequestReceiver import receiver

#draft (not done)
class RequestReceiverTester(unittest.TestCase):

    print ("Testing requests")
    r = receiver()

    def test_team_request_games(self):
        inputstring = "How many games did the team play this year?"
