import requests
from bs4 import BeautifulSoup

class team:

    # Produces the expected url for the baseball team statistics page given the year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
    # NOTE: Does not check that the url is valid or the page exists
    def __team_statistics_url(year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)
