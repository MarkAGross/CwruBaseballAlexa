import requests
from bs4 import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class team_participant:

    def __init__(self, year):
        self.team_roster_url = __team_roster_url(year)
        self.individual_statistics_url = __individual_statistics_url(year)

    # Produces the expected url for the baseball team roster for the given year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2017-18/roster?view=list
    # NOTE: Does not check that the url is valid or the page exists
    def __team_roster_url(year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/roster?view=list'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    # Produces the expected url for the baseball individual statistics page for the given a year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve?view=lineup&r=0&pos=
    # NOTE: Does not check that the url is valid or the page exists
    def __individual_statistics_url(year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve?view=lineup&r=0&pos='
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)
