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
