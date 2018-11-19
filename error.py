class CONNECTION_TO_WEBSITE_ERROR(Exception):

    def __init__(self,message):
        self.default_message = "Unable to connect to the website"
        self.message = message
