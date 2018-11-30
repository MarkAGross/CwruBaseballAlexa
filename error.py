class CONNECTION_TO_WEBSITE_ERROR(Exception):

    def __init__(self,message):
        self.default_message = "Unable to connect to the website"
        self.message = message

class LACK_OF_TEAM_INFORMATION_ERROR(Exception):

    def __init__(self,message):
        self.default_message = "Unable to retrieve sufficent information"
        self.message = message

class LACK_OF_PARTICIPANT_INFORMATION_ERROR(Exception):

    def __init__(self,message):
        self.default_message = "Unable to retrieve sufficent information"
        self.message = message

class UNABLE_TO_INTERPRET_REQUEST(Exception):
    def __init__(self):
        self.default_message = "Unable to interpret the request"
        self.message = "Unable to interpret the request"
