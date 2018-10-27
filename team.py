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
        return __team_stats_dictionary["Games"]

    def fetch_num_of_at_bats:
        return __team_stats_dictionary["At Bats"]

    def fetch_num_of_runs:
        return __team_stats_dictionary["Runs"]

    def fetch_num_of_hits:
        return __team_stats_dictionary["Hits"]

    def fetch_num_of_doubles:
        return __team_stats_dictionary["Doubles"]

    def fetch_num_of_triples:
        return __team_stats_dictionary["Triples"]

    def fetch_num_of_home_runs:
        return __team_stats_dictionary["Home Runs"]

    def fetch_num_of_runs_batted_in:
        return __team_stats_dictionary["Runs Batted In"]

    def fetch_num_of_extra_base_hits:
        return __team_stats_dictionary["Extra Base Hits"]

    def fetch_num_of_total_bases:
        return __team_stats_dictionary["Total Bases"]

    def fetch_num_of_walks:
        return __team_stats_dictionary["Walks"]

    def fetch_num_of_hit_by_pitches:
        return __team_stats_dictionary["Hit by pitch"]

    def fetch_num_of_strikeouts:
        return __team_stats_dictionary["Strikeouts"]

    def fetch_num_of_sacrifice_flies:
        return __team_stats_dictionary["Sacrifice Flies"]

    def fetch_num_of_sacrifice_hits:
        return __team_stats_dictionary["Sacrifice Hits"]

    def fetch_num_of_hit_into_double_play:
        return __team_stats_dictionary["Hit into double play"]

    def fetch_num_of_stolen_bases:
        return __team_stats_dictionary["Stolen Bases"]

    def fetch_num_of_caught_stealing:
        return __team_stats_dictionary["Caught Stealing"]

    def fetch_batting_average:
        return __team_stats_dictionary["Batting Average"]

    def fetch_on_base_percentage:
        return __team_stats_dictionary["On Base Percentage"]

    def fetch_slugging_percentage:
        return __team_stats_dictionary["Slugging Percentage"]

    def fetch_earned_run_average:
        return __team_stats_dictionary["Earned Run Average"]

    def fetch_num_of_shutouts:
        return __team_stats_dictionary["Shutouts"]

    def fetch_num_of_at_bats_against:
        return __team_stats_dictionary["At Bats Against"]

    def fetch_batting_average_against:
        return __team_stats_dictionary["Batting Average Against"]

    def fetch_home_attendance:
        return __team_stats_dictionary["Home Attendance"]

    def fetch_home_attendance_average:
        return __team_stats_dictionary["Home Attendance average"]
