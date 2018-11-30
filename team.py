import urllib.request
from bs4 import BeautifulSoup
from error import CONNECTION_TO_WEBSITE_ERROR
import datetime

#Class for fetching team statistics from CWRU Baseball Athletics website
#Each page contains the statistics for 1 year
#Example website page for 2017-18 season: https://athletics.case.edu/sports/bsb/2017-18/teams/casewesternreserve
class team:

    def __init__(self, year):
        print ("Creating team Object: " + str(datetime.datetime.now()))
        if year == None:
            year = datetime.datetime.now().year

        self.year = year

        self.team_stats_url = None
        self.get_team_stats_url(year)

        self.team_stats_dictionary = None
        self.fetch_all_team_stats(year)
        print ("Finished Creating team Object: " + str(datetime.datetime.now()))

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
        try:
            request = urllib.request.Request(self.team_stats_url, headers={'User-Agent' : "AlexaSkill"})
            webpage = urllib.request.urlopen(request)
            soup = BeautifulSoup(webpage, 'html.parser')
            table = soup.find_all('table')[2]
            table_rows = table.find_all('tr')
            for table_row in table_rows:
                table_data = table_row.find_all('td')
                row = [item.text.strip() for item in table_data]
                if len(row) != 0:
                    key = (row[0])
                    value = (row[1])
                    self.team_stats_dictionary[key] = value
        except urllib.error.HTTPError:
            raise CONNECTION_TO_WEBSITE_ERROR("Cannot connect to team statistics website")


    def fetch_num_of_games(self):
        if "Games" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Games"]
        else: return None

    def fetch_num_of_at_bats(self):
        if "At Bats" in self.team_stats_dictionary:
            return self.team_stats_dictionary["At Bats"]
        else: return None

    def fetch_num_of_runs(self):
        if "Runs" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Runs"]
        else: return None

    def fetch_num_of_hits(self):
        if "Hits" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Hits"]
        else: return None

    def fetch_num_of_doubles(self):
        if "Doubles" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Doubles"]
        else: return None

    def fetch_num_of_triples(self):
        if "Triples" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Triples"]
        else: return None

    def fetch_num_of_home_runs(self):
        if "Home Runs" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Home Runs"]
        else: return None

    def fetch_num_of_runs_batted_in(self):
        if "Runs Batted In" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Runs Batted In"]
        else: return None

    def fetch_num_of_extra_base_hits(self):
        if "Extra Base Hits" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Extra Base Hits"]
        else: return None

    def fetch_num_of_total_bases(self):
        if "Total Bases" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Total Bases"]
        else: return None

    def fetch_num_of_walks(self):
        if "Walks" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Walks"]
        else: return None

    def fetch_num_of_hit_by_pitches(self):
        if "Hit by pitch" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Hit by pitch"]
        else: return None

    def fetch_num_of_strikeouts(self):
        if "Strikeouts" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Strikeouts"]
        else: return None

    def fetch_num_of_sacrifice_flies(self):
        if "Sacrifice Flies" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Sacrifice Flies"]
        else: return None

    def fetch_num_of_sacrifice_hits(self):
        if "Sacrifice Hits" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Sacrifice Hits"]
        else: return None

    def fetch_num_of_hit_into_double_play(self):
        if "Hit into double play" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Hit into double play"]
        else: return None

    def fetch_num_of_stolen_bases(self):
        if "Stolen Bases" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Stolen Bases"]
        else: return None

    def fetch_num_of_caught_stealing(self):
        if "Caught Stealing" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Caught Stealing"]
        else: return None

    def fetch_batting_average(self):
        if "Batting Average" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Batting Average"]
        else: return None

    def fetch_on_base_percentage(self):
        if "On Base Percentage" in self.team_stats_dictionary:
            return self.team_stats_dictionary["On Base Percentage"]
        else: return None

    def fetch_slugging_percentage(self):
        if "Slugging Percentage" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Slugging Percentage"]
        else: return None

    def fetch_earned_run_average(self):
        if "Earned Run Average" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Earned Run Average"]
        else: return None

    def fetch_num_of_shutouts(self):
        if "Shutouts" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Shutouts"]
        else: return None

    def fetch_num_of_at_bats_against(self):
        if "At Bats Against" in self.team_stats_dictionary:
            return self.team_stats_dictionary["At Bats Against"]
        else: return None

    def fetch_batting_average_against(self):
        if "Batting Average Against" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Batting Average Against"]
        else: return None

    def fetch_home_attendance(self):
        if "Home Attendance" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Home Attendance"]
        else: return None

    def fetch_home_attendance_average(self):
        if "Home Attendance average" in self.team_stats_dictionary:
            return self.team_stats_dictionary["Home Attendance average"]
        else: return None
