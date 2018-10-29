import urllibrequest
from bs import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class team_participant:

    def __init__(self, year):
        selfroster_list = __get_list_of_all_roster_data(year)
        selfindividual_statistics_batters_list = __get_list_of_all_individual_batter_statistics(year)
        selfindividual_statistics_pitchers_list = __get_list_of_all_individual_pitcher_statistics(year)


    # Produces the expected url for the baseball team roster for the given year
    # Example Format as follows: https://athleticscaseedu/sports/bsb/0-/roster?view=list
    # NOTE: Does not check that the url is valid or the page exists
    def __team_roster_url(year):
        url_beginning = 'https://athleticscaseedu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/roster?view=list'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    # Produces the expected url for the baseball individual statistics page for the given a year
    # Example Format as follows: https://athleticscaseedu/sports/bsb/0-/teams/casewesternreserve?view=lineup&r=0&pos=
    # NOTE: Does not check that the url is valid or the page exists
    def __individual_statistics_url(year):
        url_beginning = 'https://athleticscaseedu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/teams/casewesternreserve?view=lineup'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    #returns a list of each row of the table, each row being represented by a dictionary
    #The dictionary key values are the column headers with the values being the table values
    def __get_list_of_all_roster_data(year):
        roster_page_url = __team_roster_url(year)
        #get all data from roster table
        list_of_table_rows_raw_data = []
        request = urllibrequestRequest(roster_page_url, headers={'User-Agent' : "AlexaSkill"})
        webpage = urllibrequesturlopen(request)
        soup = BeautifulSoup(webpage, 'lxml')
        table = soupfind('table')
        table_rows = tablefind_all('tr')
        for table_row in table_rows:
            table_data = table_rowfind_all('td')
            row = [itemtext for item in table_data]
            if len(row) != 0:
                list_of_table_rows_raw_dataappend(row)
        #change raw data from table to a list of dictionaries, each dictionary being a row of
        #the table with key value pairs of the column name and table value
        list_of_table_rows_refined = []
        for row in list_of_table_rows_raw_data:
            single_row_dictionary = {}
            for element in row:
                element = elementreplace('\n','')
                key,value = elementsplit(":")
                single_row_dictionary[key] = value
            list_of_table_rows_refinedappend(single_row_dictionary)
        return list_of_table_rows_refined

    def __get_list_of_all_individual_batter_statistics(year):
        individual_statistics_url = __individual_statistics_url(year)
        individual_statistics_batter_table_number = 4
        __fetch_all_table_data(individual_statistics_url, individual_statistics_batter_table_number)

    def __get_list_of_all_individual_pitcher_statistics(year):
        individual_statistics_url = __individual_statistics_url(year)
        individual_statistics_pitcher_table_number = 8
        __fetch_all_table_data(individual_statistics_url, individual_statistics_pitcher_table_number)


    def __fetch_all_table_data(url, table_number):
        #get all rows to batter stats table
        list_of_player_dictionaries = []
        request = urllibrequestRequest(url, headers={'User-Agent' : "AlexaSkill"})
        webpage = urllibrequesturlopen(request)
        soup = BeautifulSoup(webpage, 'lxml')
        table = soupfind_all('table')[table_number]
        table_rows = tablefind_all('tr')
        #get all headers
        headers = []
        table_headers = table_rows[0]find_all('th')
        headers = [headertext for header in table_headers]
        for index in range(len(headers)):
            headers[index] = headers[index]replace('\n','')
            headers[index] = headers[index]upper()
        #get each row / player
        rows = []
        for table_row in table_rows:
            table_data = table_rowfind_all('td')
            row = [itemtext for item in table_data]
            for index in range(len(row)):
                row[index] = row[index]replace('\n','')
                row[index] = row[index]replace('-', '0')
                row[index] = row[index]strip()
            if len(row) > 0:
                rowsappend(row)
        #create list of players dictionaries, where the keys are col names and values are player stat values
        for row in rows:
            player = {}
            for index in range(len(headers)):
                player[headers[index]] = row[index]
            list_of_player_dictionariesappend(player)
        return list_of_player_dictionaries

    def fetch_player_name(player_number):

    def fetch_player_position(player_number):

    def fetch_all_players_by_position(player_number):

    def fetch_player_bats_and_throws(player_number):

    def fetch_player_height(player_number):

    def fetch_player_weight(player_number):

    def fetch_player_year(player_number):

    def fetch_all_players_year(player_number):

    def fetch_player_hometown_and_high_school(player_number):

    def fetch_batter_games_played(player_number):

    def fetch_batter_num_of_at_bats(player_number):

    def fetch_batter_num_of_runs(player_number):

    def fetch_batter_num_of_hits(player_number):

    def fetch_batter_num_of_doubles(player_number):

    def fetch_batter_num_of_triples(player_number):

    def fetch_batter_num_of_home_runs(player_number):

    def fetch_batter_num_of_runs_batted_in(player_number):

    def fetch_batter_num_of_walks(player_number):

    def fetch_batter_num_of_strikeouts(player_number):

    def fetch_batter_num_of_stolen_bases(player_number):

    def fetch_batter_batting_average(player_number):

    def fetch_batter_on_base_percentage(player_number):

    def fetch_batter_slugging_percentage(player_number):

    def fetch_pitcher_num_of_appearances(player_number):

    def fetch_pitcher_num_of_game_starts(player_number):

    def fetch_pitcher_num_of_wins(player_number):

    def fetch_pitcher_num_of_losses(player_number):

    def fetch_pitcher_num_of_saves(player_number):

    def fetch_pitcher_num_of_complete_games(player_number):

    def fetch_pitcher_num_of_innings_pitched(player_number):

    def fetch_pitcher_num_of_hits(player_number):

    def fetch_pitcher_num_of_runs(player_number):

    def fetch_pitcher_num_of_earned_runs(player_number):

    def fetch_pitcher_num_of_walks(player_number):

    def fetch_pitcher_num_of_strikeouts(player_number):

    def fetch_pitcher_strikeouts_per_nine_innings(player_number):

    def fetch_pitcher_num_of_home_runs(player_number):

    def fetch_pitcher_earned_run_average(player_number):
