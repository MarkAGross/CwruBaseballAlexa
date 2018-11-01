import urllib.request
from bs4 import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class team_participant:

    def __init__(self, year):
        self.year = year

        self.roster_list = None
        self.get_list_of_all_roster_data(year)

        self.individual_statistics_batters_list = None
        self.get_list_of_all_individual_batter_statistics(year)

        self.individual_statistics_pitchers_list = None
        self.get_list_of_all_individual_pitcher_statistics(year)


    # Produces the expected url for the baseball team roster for the given year
    # Example Format as follows: https://athleticscaseedu/sports/bsb/0-/roster?view=list
    # NOTE: Does not check that the url is valid or the page exists
    def team_roster_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/roster?view=list'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    # Produces the expected url for the baseball individual statistics page for the given a year
    # Example Format as follows: https://athleticscaseedu/sports/bsb/0-/teams/casewesternreserve?view=lineup&r=0&pos=
    # NOTE: Does not check that the url is valid or the page exists
    def individual_statistics_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve?view=lineup'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    #returns a list of each row of the table, each row being represented by a dictionary
    #The dictionary key values are the column headers with the values being the table values
    def get_list_of_all_roster_data(self, year):
        roster_page_url = self.team_roster_url(year)
        #get all data from roster table
        list_of_table_rows_raw_data = []
        request = urllib.request.Request(roster_page_url, headers={'User-Agent' : "AlexaSkill"})
        webpage = urllib.request.urlopen(request)
        soup = BeautifulSoup(webpage, 'lxml')
        table = soup.find('table')
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            table_data = table_row.find_all('td')
            row = [item.text for item in table_data]
            if len(row) != 0:
                list_of_table_rows_raw_data.append(row)
        #change raw data from table to a list of dictionaries, each dictionary being a row of
        #the table with key value pairs of the column name and table value
        list_of_table_rows_refined = []
        for row in list_of_table_rows_raw_data:
            single_row_dictionary = {}
            for element in row:
                element = element.replace('\n','')
                key,value = element.split(":")
                single_row_dictionary[key] = value
            list_of_table_rows_refined.append(single_row_dictionary)
        self.roster_list = list_of_table_rows_refined

    def get_list_of_all_individual_batter_statistics(self, year):
        individual_statistics_url = self.individual_statistics_url(year)
        individual_statistics_batter_table_number = 4
        self.individual_statistics_batters_list = self.fetch_all_table_data(individual_statistics_url, individual_statistics_batter_table_number)

    def get_list_of_all_individual_pitcher_statistics(self, year):
        individual_statistics_url = self.individual_statistics_url(year)
        individual_statistics_pitcher_table_number = 8
        self.individual_statistics_pitchers_list = self.fetch_all_table_data(individual_statistics_url, individual_statistics_pitcher_table_number)

    def fetch_all_table_data(self, url, table_number):
        #get all rows to batter stats table
        list_of_player_dictionaries = []
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


    def get_player_roster_dictionary(self, player_number):
        for player in self.roster_list:
            if player['No.'] == str(player_number):
                return player
        # if player with input number not found
        return {}

    def get_player_batter_dictionary(self, player_number):
        for player in self.individual_statistics_batters_list:
            if player['NO.'] == str(player_number):
                return player
        # if player with input number not found
        return {}

    def get_player_pitcher_dictionary(self, player_number):
        for player in self.individual_statistics_pitchers_list:
            if player['NO.'] == str(player_number):
                return player
        # if player with input number not found
        return {}


    def fetch_player_name(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        print (player)
        return player['No.']

    def fetch_player_position(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['Pos.']

    def fetch_all_players_by_position(self, position_abr):
        list_of_players = []
        for player in self.roster_list:
            if player['Pos.'] == position_abr:
                list_of_players.append(player)
        return list_of_players

    def fetch_player_bats_and_throws(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['B/T']

    def fetch_player_height(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['Ht.']

    def fetch_player_weight(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['Wt.']

    def fetch_player_year(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['Yr.']

    def fetch_all_players_year(self, year_abr):
        list_of_players = []
        for player in self.roster_list:
            if player['Yr.'] == year_abr:
                list_of_players.append(player)
        return list_of_players

    def fetch_player_hometown_and_high_school(self, player_number):
        player = self.get_player_roster_dictionary(player_number)
        return player['Hometown/High School']

    def fetch_batter_games_played(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['G']

    def fetch_batter_num_of_at_bats(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['AB']

    def fetch_batter_num_of_runs(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['R']

    def fetch_batter_num_of_hits(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['H']

    def fetch_batter_num_of_doubles(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['2B']

    def fetch_batter_num_of_triples(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['3B']

    def fetch_batter_num_of_home_runs(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['HR']

    def fetch_batter_num_of_runs_batted_in(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['RBI']

    def fetch_batter_num_of_walks(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['BB']

    def fetch_batter_num_of_strikeouts(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['K']

    def fetch_batter_num_of_stolen_bases(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['SB']

    def fetch_batter_batting_average(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['BA']

    def fetch_batter_on_base_percentage(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['OBP']

    def fetch_batter_slugging_percentage(self, player_number):
        player = self.get_player_batter_dictionary(player_number)
        return player['SLG']

    def fetch_pitcher_num_of_appearances(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['APP']

    def fetch_pitcher_num_of_game_starts(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['GS']

    def fetch_pitcher_num_of_wins(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['W']

    def fetch_pitcher_num_of_losses(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['L']

    def fetch_pitcher_num_of_saves(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['SV']

    def fetch_pitcher_num_of_complete_games(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['CG']

    def fetch_pitcher_num_of_innings_pitched(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['IP']

    def fetch_pitcher_num_of_hits(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['H']

    def fetch_pitcher_num_of_runs(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['R']

    def fetch_pitcher_num_of_earned_runs(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['ER']

    def fetch_pitcher_num_of_walks(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['BB']

    def fetch_pitcher_num_of_strikeouts(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['K']

    def fetch_pitcher_strikeouts_per_nine_innings(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['K/9']

    def fetch_pitcher_num_of_home_runs(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['HR']

    def fetch_pitcher_earned_run_average(self, player_number):
        player = self.get_player_pitcher_dictionary(player_number)
        return player['ERA']
