import urllib.request
from bs4 import BeautifulSoup
from error import CONNECTION_TO_WEBSITE_ERROR
import datetime

#Class for fetching information and statistics about players and coaches
class team_participant:

    """
    Constructor for team_particpant
    Pulls information from website or throws error if unable to connect to website or pull data
    """

    def __init__(self, year):
        if year == None:
            year = datetime.datetime.now().year

        self.year = year

        self.roster_dictionary_list = []
        self.create_and_set_list_of_all_roster_data(year)

        self.batters_individual_statistics_dictionary_list = []
        self.create_and_set_list_of_all_batter_individual_statistics(year)

        self.pitchers_individual_statistics_dictionary_list = []
        self.create_and_set_list_of_all_pitcher_individual_statistics(year)

        self.players_list = []
        self.create_and_set_players_list(self.roster_dictionary_list, self.batters_individual_statistics_dictionary_list, self.pitchers_individual_statistics_dictionary_list)


    """
    Functions for creating each URL for the input year.
    Note: Does not check that URL is valid
    Input year is upper bound of year range: Example: 2017-18 season URL obtained with an input year of 2018
    """

    def team_roster_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/roster?view=list'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)


    def individual_statistics_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve?view=lineup'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)


    """
    Functions for creating and setting lists of dictionaries containing table data.
    Throws error if there is an error connecting to the website of the specified year
    """

    def create_and_set_list_of_all_roster_data(self, year):
        roster_page_url = self.team_roster_url(year)
        #get all data from roster table
        list_of_table_rows_raw_data = []
        try:
            request = urllib.request.Request(roster_page_url, headers={'User-Agent' : "AlexaSkill"})
            webpage = urllib.request.urlopen(request)
            soup = BeautifulSoup(webpage, 'lxml')
            table = soup.find('table')
            table_rows = table.find_all('tr')
            for table_row in table_rows:
                row_data = table_row.find_all('td')
                row = [item.text for item in row_data]
                row_player_name = table_row.find('th').text
                row.append("Name:" + row_player_name)
                if len(row) > 2: #filters out empty rows and headers
                    list_of_table_rows_raw_data.append(row)
            #change raw data from table to a list of dictionaries, each dictionary being a row of
            #the table with key value pairs of the column name and table value
            list_of_table_rows_refined = []
            for row in list_of_table_rows_raw_data:
                single_row_dictionary = {}
                for element in row:
                    key,value = element.split(":")
                    key = key.strip()
                    key = key.replace('\n',' ')
                    value = value.strip()
                    value = value.replace('\n',' ')
                    single_row_dictionary[key] = value
                list_of_table_rows_refined.append(single_row_dictionary)
            self.roster_dictionary_list = list_of_table_rows_refined
        except urllib.error.HTTPError:
            raise CONNECTION_TO_WEBSITE_ERROR("Cannot connect to roster website")

    def create_and_set_list_of_all_batter_individual_statistics(self, year):
        individual_statistics_url = self.individual_statistics_url(year)
        individual_statistics_batter_table_number = 4
        self.batters_individual_statistics_dictionary_list = self.fetch_all_individual_statistics_table_data(individual_statistics_url, individual_statistics_batter_table_number)

    def create_and_set_list_of_all_pitcher_individual_statistics(self, year):
        individual_statistics_url = self.individual_statistics_url(year)
        individual_statistics_pitcher_table_number = 8
        self.pitchers_individual_statistics_dictionary_list = self.fetch_all_individual_statistics_table_data(individual_statistics_url, individual_statistics_pitcher_table_number)

    def fetch_all_individual_statistics_table_data(self, url, table_number):
        #get all rows to batter stats table
        list_of_player_dictionaries = []
        try:
            request = urllib.request.Request(url, headers={'User-Agent' : "AlexaSkill"})
            webpage = urllib.request.urlopen(request)
            soup = BeautifulSoup(webpage, 'lxml')
            table = soup.find_all('table')[table_number]
            table_rows = table.find_all('tr')
            #get all headers
            headers = []
            table_headers = table_rows[0].find_all('th')
            headers = [header.text for header in table_headers]
            for index in range(len(headers)):
                headers[index] = headers[index].replace('\n','')
                headers[index] = headers[index].upper()
            #get each row / player
            rows = []
            for table_row in table_rows:
                table_data = table_row.find_all('td')
                row = [item.text for item in table_data]
                for index in range(len(row)):
                    row[index] = row[index].replace('\n','')
                    row[index] = row[index].replace('-', '0')
                    row[index] = row[index].strip()
                if len(row) > 0:
                    rows.append(row)
            #create list of players dictionaries, where the keys are col names and values are player stat values
            for row in rows:
                player = {}
                for index in range(len(headers)):
                    player[headers[index]] = row[index]
                list_of_player_dictionaries.append(player)
            return list_of_player_dictionaries
        #if cannot connect to website
        except urllib.error.HTTPError:
            raise CONNECTION_TO_WEBSITE_ERROR("Cannot connect to individual statistics website")


    """
    Functions for creating the players list from the previously set roster, batter and pitcher dictionaries.
    Assumes that roster contains all players.
    """

    def create_and_set_players_list(self, roster_dictionary_list, batter_stats_dictionary_list, pitcher_stats_dictionary_list):
        for roster_dictionary in roster_dictionary_list:
            number_string = roster_dictionary["No."]
            batter_dictionary = self.get_player_batter_dictionary(number_string)
            pitcher_dictionary = self.get_player_pitcher_dictionary(number_string)
            created_player = player(roster_dictionary, batter_dictionary, pitcher_dictionary)
            self.players_list.append(created_player)


    def get_player_batter_dictionary(self, player_number):
        for player in self.batters_individual_statistics_dictionary_list:
            if player['NO.'] == str(player_number):
                return player
        # if player with input number not found
        return None

    def get_player_pitcher_dictionary(self, player_number):
        for player in self.pitchers_individual_statistics_dictionary_list:
            if player['NO.'] == str(player_number):
                return player
        # if player with input number not found
        return None


    """
    Functions for fetching from pulled data.
    Assumes all data already stored in players_list
    """

    def get_player_from_players_list_by_number(self, number):
        for player in self.players_list:
            if player.number == number:
                return player
        #if player with input number not found
        return None

    def fetch_player_name(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.name

    def fetch_player_position(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.player_position

    def fetch_all_players_by_position(self, position_abr):
        list_of_players_for_position = []
        for player in self.players_list:
            if player.player_position == position_abr:
                list_of_players_for_position.append(player)
        if not list_of_players_for_position:
            return None
        else:
            return list_of_players_for_position

    def fetch_player_bats_and_throws(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.bats_and_throws

    def fetch_player_height(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.player_height

    def fetch_player_weight(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.player_weight

    def fetch_player_year(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.player_year

    def fetch_all_players_year(self, year_abr):
        list_of_players_for_academic_year = []
        for player in self.players_list:
            if player.player_year == academic_year_abr:
                list_of_players_for_academic_year.append(player)
        if not list_of_players_for_academic_year:
            return None
        else:
            return list_of_players_for_academic_year

    def fetch_player_hometown_and_high_school(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.player_hometown_and_high_school

    def fetch_batter_games_played(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_games_played

    def fetch_batter_num_of_at_bats(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_at_bats

    def fetch_batter_num_of_runs(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_runs

    def fetch_batter_num_of_hits(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_hits

    def fetch_batter_num_of_doubles(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_doubles

    def fetch_batter_num_of_triples(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_triples

    def fetch_batter_num_of_home_runs(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_home_runs

    def fetch_batter_num_of_runs_batted_in(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_runs_batted_in

    def fetch_batter_num_of_walks(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_walks

    def fetch_batter_num_of_strikeouts(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_strikeouts

    def fetch_batter_num_of_stolen_bases(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_num_of_stolen_bases

    def fetch_batter_batting_average(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_batting_average

    def fetch_batter_on_base_percentage(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_on_base_percentage

    def fetch_batter_slugging_percentage(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.batter_slugging_percentage

    def fetch_pitcher_num_of_appearances(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_appearances

    def fetch_pitcher_num_of_game_starts(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_game_starts

    def fetch_pitcher_num_of_wins(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_wins

    def fetch_pitcher_num_of_losses(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_losses

    def fetch_pitcher_num_of_saves(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_saves

    def fetch_pitcher_num_of_complete_games(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_complete_games

    def fetch_pitcher_num_of_innings_pitched(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_innings_pitched

    def fetch_pitcher_num_of_hits(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_hits

    def fetch_pitcher_num_of_runs(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_runs

    def fetch_pitcher_num_of_earned_runs(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_earned_runs

    def fetch_pitcher_num_of_walks(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_walks

    def fetch_pitcher_num_of_strikeouts(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_strikeouts

    def fetch_pitcher_strikeouts_per_nine_innings(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_strikeouts_per_nine_innings

    def fetch_pitcher_num_of_home_runs(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_num_of_home_runs

    def fetch_pitcher_earned_run_average(self, player_number):
        player = self.get_player_from_players_list_by_number(player_number)
        if player == None:
            return None
        return player.pitcher_earned_run_average

class player:

    def __init__(self, roster_dictionary, batter_dictionary, pitcher_dictionary):
        self.number = None
        self.name = None
        self.player_position = None
        self.bats_and_throws = None
        self.player_height = None
        self.player_weight = None
        self.player_year = None
        self.player_hometown_and_high_school = None
        self.batter_games_played = None
        self.batter_num_of_at_bats = None
        self.batter_num_of_runs = None
        self.batter_num_of_hits = None
        self.batter_num_of_doubles = None
        self.batter_num_of_triples = None
        self.batter_num_of_home_runs = None
        self.batter_num_of_runs_batted_in = None
        self.batter_num_of_walks = None
        self.batter_num_of_strikeouts = None
        self.batter_num_of_stolen_bases= None
        self.batter_batting_average = None
        self.batter_on_base_percentage = None
        self.batter_slugging_percentage = None
        self.pitcher_num_of_appearances = None
        self.pitcher_num_of_game_starts = None
        self.pitcher_num_of_wins = None
        self.pitcher_num_of_losses = None
        self.pitcher_num_of_saves = None
        self.pitcher_num_of_complete_games = None
        self.pitcher_num_of_innings_pitched= None
        self.pitcher_num_of_hits= None
        self.pitcher_num_of_runs = None
        self.pitcher_num_of_earned_runs = None
        self.pitcher_num_of_walks = None
        self.pitcher_num_of_strikeouts = None
        self.pitcher_strikeouts_per_nine_innings = None
        self.pitcher_num_of_home_runs = None
        self.pitcher_earned_run_average = None
        self.initialize_from_roster_dictionary(roster_dictionary)
        self.initialize_from_batter_dictionary(batter_dictionary)
        self.initialze_from_pitcher_dictionary(pitcher_dictionary)

    def initialize_from_roster_dictionary(self, dictionary):
        if dictionary == None:
            return
        if "No." in dictionary:
            self.number = dictionary["No."]
        if "Name" in dictionary:
            self.name = dictionary["Name"]
        if "Pos." in dictionary:
            self.player_position = dictionary["Pos."]
        if "B/T" in dictionary:
            self.bats_and_throws = dictionary["B/T"]
        if "Ht." in dictionary:
            self.player_height = dictionary["Ht."]
        if "Wt." in dictionary:
            self.player_weight = dictionary["Wt."]
        if "Yr." in dictionary:
            self.player_year = dictionary["Yr."]
        if "Hometown/High School" in dictionary:
            self.player_hometown_and_high_school = dictionary["Hometown/High School"]

    def initialize_from_batter_dictionary(self, dictionary):
        if dictionary == None:
            return
        if "G" in dictionary:
            self.batter_games_played = dictionary["G"]
        if "AB" in dictionary:
            self.batter_num_of_at_bats = dictionary["AB"]
        if "R" in dictionary:
            self.batter_num_of_runs = dictionary["R"]
        if "H" in dictionary:
            self.batter_num_of_hits = dictionary["H"]
        if "2B" in dictionary:
            self.batter_num_of_doubles = dictionary["2B"]
        if "3B" in dictionary:
            self.batter_num_of_triples = dictionary["3B"]
        if "HR" in dictionary:
            self.batter_num_of_home_runs = dictionary["HR"]
        if "RBI" in dictionary:
            self.batter_num_of_runs_batted_in = dictionary["RBI"]
        if "BB" in dictionary:
            self.batter_num_of_walks = dictionary["BB"]
        if "K" in dictionary:
            self.batter_num_of_strikeouts = dictionary["K"]
        if "SB" in dictionary:
            self.batter_num_of_stolen_bases= dictionary["SB"]
        if "AVG" in dictionary:
            self.batter_batting_average = dictionary["AVG"]
        if "OBP" in dictionary:
            self.batter_on_base_percentage = dictionary["OBP"]
        if "SLG" in dictionary:
            self.batter_slugging_percentage = dictionary["SLG"]

    def initialze_from_pitcher_dictionary(self,dictionary):
        if dictionary == None:
            return
        if "APP" in dictionary:
            self.pitcher_num_of_appearances = dictionary["APP"]
        if "GS" in dictionary:
            self.pitcher_num_of_game_starts = dictionary["GS"]
        if "W" in dictionary:
            self.pitcher_num_of_wins = dictionary["W"]
        if "L" in dictionary:
            self.pitcher_num_of_losses = dictionary["L"]
        if "SV" in dictionary:
            self.pitcher_num_of_saves = dictionary["SV"]
        if "CG" in dictionary:
            self.pitcher_num_of_complete_games = dictionary["CG"]
        if "IP" in dictionary:
            self.pitcher_num_of_innings_pitched= dictionary["IP"]
        if "H" in dictionary:
            self.pitcher_num_of_hits= dictionary["H"]
        if "R" in dictionary:
            self.pitcher_num_of_runs = dictionary["R"]
        if "ER" in dictionary:
            self.pitcher_num_of_earned_runs = dictionary["ER"]
        if "BB" in dictionary:
            self.pitcher_num_of_walks = dictionary["BB"]
        if "K" in dictionary:
            self.pitcher_num_of_strikeouts = dictionary["K"]
        if "K/9" in dictionary:
            self.pitcher_strikeouts_per_nine_innings = dictionary["K/9"]
        if "HR" in dictionary:
            self.pitcher_num_of_home_runs = dictionary["HR"]
        if "ERA" in dictionary:
            self.pitcher_earned_run_average = dictionary["ERA"]
