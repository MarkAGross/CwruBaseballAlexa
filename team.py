import urllib.request
from bs4 import BeautifulSoup

#Class for fetching team statistics from CWRU Baseball Athletics website
#Each page contains the statistics for 1 year
#Example website page for 2017-18 season: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
class team:

    def __init__(self, year):
        self.team_stats_url = None
        self.get_team_stats_url(year)

        self.team_stats_dictionary = None
        self.fetch_all_team_stats(year)

    # Produces the expected url for the baseball team statistics page given the year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
    # NOTE: Does not check that the url is valid or the page exists
    def get_team_stats_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve'
        self.team_stats_url = (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)


    #Saves all statistics as key-value pairs in team_stats_dictionary
    #Key to each value is seen as the text on the table from the website
    def fetch_all_team_stats(self, year):
        self.team_stats_dictionary = {}
        request = urllib.request.Request(self.team_stats_url, headers={'User-Agent' : "AlexaSkill"})
        webpage = urllib.request.urlopen(request)
        soup = BeautifulSoup(webpage, 'lxml')
        table = soup.find_all('table')[2]
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            table_data = table_row.find_all('td')
            row = [item.text.strip() for item in table_data]
            if len(row) != 0:
                key = (row[0])
                value = (row[1])
                self.team_stats_dictionary[key] = value

    def fetch_num_of_games(self):
        return self.team_stats_dictionary["Games"]

    def fetch_num_of_at_bats(self):
        return self.team_stats_dictionary["At Bats"]

    def fetch_num_of_runs(self):
        return self.team_stats_dictionary["Runs"]

    def fetch_num_of_hits(self):
        return self.team_stats_dictionary["Hits"]

    def fetch_num_of_doubles(self):
        return self.team_stats_dictionary["Doubles"]

    def fetch_num_of_triples(self):
        return self.team_stats_dictionary["Triples"]

    def fetch_num_of_home_runs(self):
        return self.team_stats_dictionary["Home Runs"]

    def fetch_num_of_runs_batted_in(self):
        return self.team_stats_dictionary["Runs Batted In"]

    def fetch_num_of_extra_base_hits(self):
        return self.team_stats_dictionary["Extra Base Hits"]

    def fetch_num_of_total_bases(self):
        return self.team_stats_dictionary["Total Bases"]

    def fetch_num_of_walks(self):
        return self.team_stats_dictionary["Walks"]

    def fetch_num_of_hit_by_pitches(self):
        return self.team_stats_dictionary["Hit by pitch"]

    def fetch_num_of_strikeouts(self):
        return self.team_stats_dictionary["Strikeouts"]

    def fetch_num_of_sacrifice_flies(self):
        return self.team_stats_dictionary["Sacrifice Flies"]

    def fetch_num_of_sacrifice_hits(self):
        return self.team_stats_dictionary["Sacrifice Hits"]

    def fetch_num_of_hit_into_double_play(self):
        return self.team_stats_dictionary["Hit into double play"]

    def fetch_num_of_stolen_bases(self):
        return self.team_stats_dictionary["Stolen Bases"]

    def fetch_num_of_caught_stealing(self):
        return self.team_stats_dictionary["Caught Stealing"]

    def fetch_batting_average(self):
        return self.team_stats_dictionary["Batting Average"]

    def fetch_on_base_percentage(self):
        return self.team_stats_dictionary["On Base Percentage"]

    def fetch_slugging_percentage(self):
        return self.team_stats_dictionary["Slugging Percentage"]

    def fetch_earned_run_average(self):
        return self.team_stats_dictionary["Earned Run Average"]

    def fetch_num_of_shutouts(self):
        return self.team_stats_dictionary["Shutouts"]

    def fetch_num_of_at_bats_against(self):
        return self.team_stats_dictionary["At Bats Against"]

    def fetch_batting_average_against(self):
        return self.team_stats_dictionary["Batting Average Against"]

    def fetch_home_attendance(self):
        return self.team_stats_dictionary["Home Attendance"]

    def fetch_home_attendance_average(self):
        return self.team_stats_dictionary["Home Attendance average"]
