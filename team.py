import requests
from bs4 import BeautifulSoup

#Class for fetching team statistics from CWRU Baseball Athletics website
#Each page contains the statistics for 1 year
#Example website page for 2017-18 season: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
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

    #Saves all statistics as key-value pairs in __team_stats_dictionary
    #Key to each value is seen as the text on the table from the website
    def __fetch_all_team_stats(year):
        webpage = requests.get(__team_statistics_url(year))
        soup = BeautifulSoup(webpage.text, 'html.parser')
        div = soup.find('div', {'class' : 'stats-box half'}):
        table = div.find('table')
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            __team_stats_dictionary[tr.find_all('td')[0].text.strip()] = tr.find_all('td')[1].text.strip

    def fetch_num_of_games:

    def fetch_num_of_at_bats:

    def fetch_num_of_runs:

    def fetch_num_of_hits:

    def fetch_num_of_doubles:

    def fetch_num_of_triples:

    def fetch_num_of_home_runs:

    def fetch_num_of_runs_batted_in:

    def fetch_num_of_extra_base_hits:

    def fetch_num_of_total_bases:

    def fetch_num_of_walks:

    def fetch_num_of_hit_by_pitches:

    def fetch_num_of_strikeouts:

    def fetch_num_of_sacrifice_flies:

    def fetch_num_of_sacrifice_hits:

    def fetch_num_of_hit_into_double_play:

    def fetch_num_of_stolen_bases:

    def fetch_num_of_caught_stealing:

    def fetch_batting_average:

    def fetch_on_base_percentage:

    def fetch_slugging_percentage:

    def fetch_earned_run_average:

    def fetch_num_of_shutouts:

    def fetch_num_of_at_bats_against:

    def fetch_batting_average_against:

    def fetch_home_attendance:

    def fetch_home_attendance_average:
