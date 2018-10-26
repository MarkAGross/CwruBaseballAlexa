import requests
from bs4 import BeautifulSoup

class team:

    __team_stats_dictionary = {}

    # Produces the expected url for the baseball team statistics page given the year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
    # NOTE: Does not check that the url is valid or the page exists
    def __team_stats_url(year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    def __fetch_all_team_stats(year):
        webpage = requests.get(__team_statistics_url(year))
        soup = BeautifulSoup(webpage.text, 'html.parser')
        div = soup.find('div', {'class' : 'stats-box half'}):
        table = div.find('table')
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            __team_stats_dictionary[tr.find_all('td')[0].text.strip()] = tr.find_all('td')[1].text.strip
