import urllib.request
from bs4 import BeautifulSoup
from error import CONNECTION_TO_WEBSITE_ERROR
import datetime
import calendar

#Class for fetching information and statistics about players and coaches
class schedule:

    def __init__(self, year):
        print("Creating schedule Object: " + str(datetime.datetime.now()))
        if year == None:
            year = datetime.datetime.now().year

        self.year = year

        self.url = None
        self.schedule_url(year)

        self.list_of_table_row_dictionaries = None
        self.get_list_of_all_row_dictionaries(self.url)

        self.list_of_games = []
        if self.list_of_table_row_dictionaries != None:
            for dictionary in self.list_of_table_row_dictionaries:
                self.list_of_games.append(game(dictionary))
        print("Finished Creating schedule Object:" + str(datetime.datetime.now()))

    def fetch_games_by_date(self, month, day):
        """ Returns a list of games for the given date

        Args:
            month (string) : full name of the month of the game
            day (int) : day of the month

        Returns:
            list : list of game dictionaries on the input date
        """
        games_for_input_day = []
        for game in self.list_of_games:
            if game.month == month and game.day == day:
                games_for_input_day.append(game)
        if not games_for_input_day:
            return None
        else:
            return games_for_input_day

    def fetch_previous_game(self):
        """ Returns the most recent game that occured on or before the current date

        Returns:
            dictionary : dictionary of the game on the current date or closest previous game to current date
        """
        current = datetime.datetime.now()
        year = current.year
        month_num = int(current.month)
        month = current.strftime("%B")
        day = int(current.day)
        if year != self.year:
            return None
        games = self.fetch_games_by_date(calendar.month_name[month_num], str(day))
        while games == None:
            if month_num > 0 and day > 0:
                day = day - 1
            if month_num > 0 and day <= 0:
                month_num = month_num - 1
                day = 31
            if month_num == 0:
                return None
            games = self.fetch_games_by_date(calendar.month_name[month_num], str(day))
        return games[-1] #gets last and most recent game of the list of games



    # if the schedule and current years are different, returns None
    def fetch_next_game(self):
        """ Returns the next game to occur on or after the current date.
        If the scheudle and current years are different, returns None.

        Returns:
            dictionary : Dictionary of the game on the current date or closest future game to current date.
                         If current year is not the same year as this scheudle object, reurns none.
        """
        current = datetime.datetime.now()
        year = current.year
        month_num = int(current.month)
        month = current.strftime("%B")
        day = int(current.day)
        if year != self.year:
            return None
        games = self.fetch_games_by_date(calendar.month_name[month_num], str(day))
        while games == None:
            if month_num < 13 and day < 31:
                day = day + 1
            if month_num < 13 and day <= 32:
                month_num = month_num + 1
                day = 1
            if month_num == 13:
                return None
            games = self.fetch_games_by_date(calendar.month_name[month_num], str(day))
        return games[0] #gets first game in the list of games. The list of games is for the next day with games


    def schedule_url(self, year):
        """ Produces the expected url for the baseball schedule for the given year.
        Does not check that url is valid.
        Input year is upper bound of year range. Example: 2017-18 season can be obtained with an input year of 2018.

        Args:
            year (integer) : Year of the scheudle.

        Returns:
            str : URL of the schedule for the given year.
        """
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/schedule'
        self.url = (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)


    def get_list_of_all_row_dictionaries(self, url):
        """ Sets list_of_row_dictionaries attribute of schedule class to following data structure:
        A dictionary with the key being the month and value being list of games in the month.
        Each game is a dictionary, the keys and values of which can be found in the funciton make_row_dictionary

        Args:
            URL (str) : URL of the scheudle page.
        """
        final_dictionary = {}
        #get all data from schedule table
        list_of_table_row_dictionaries = []
        try:
            request = urllib.request.Request(url, headers={'User-Agent' : "AlexaSkill"})
            webpage = urllib.request.urlopen(request)
            soup = BeautifulSoup(webpage, 'html.parser')
            table = soup.find('table')
            table_rows = table.find_all('tr')
            month = None
            date = None
            for table_row in table_rows:
                row_dictionary = {}
                self.make_row_dictionary(table_row,row_dictionary)
                #adding month to each game
                if 'month-title' in row_dictionary:
                    month = row_dictionary['month-title']
                elif month != None:
                    row_dictionary['month-title'] = month
                #adding date to each game
                if 'e_date' in row_dictionary and row_dictionary['e_date'] != '':
                    date = row_dictionary['e_date']
                elif 'e_date' in row_dictionary and row_dictionary['e_date'] == '':
                    row_dictionary['e_date'] = date
                if len(row_dictionary) > 2: #filters out empty rows or rows with just the month
                    list_of_table_row_dictionaries.append(row_dictionary)
            self.list_of_table_row_dictionaries = list_of_table_row_dictionaries
        except urllib.error.HTTPError:
            raise CONNECTION_TO_WEBSITE_ERROR("Cannot connect to schedule website")


    def make_row_dictionary(self, html_table_row, dictionary):
        """ Pass in a <tr> element and parts of it placed in the input dicitionary.
        Its key is the <tr> class and the value is the <tr> text.

        Currntly added classes to the dictionary are:
          --KEY--    |  --EXAMPLE VALUE--
        ______________________________
        month-title  | March
        e_date       | Sun. 29
        va           | at
        team-name    | #20 Marietta
        neutralsite  | @ Washington, Pa.
        e_result     | W, 3-2
        e_status     | Final - 11 Innings


        Args:
            html_table_row (str) : HTML of a table row
            dictionary (dictionary) : a dictionary object to append the table row classes to
        """
        if len(html_table_row) == 1:
            if self.is_Month(html_table_row.text):
                dictionary['month-title'] = html_table_row.text
        date = html_table_row.find('td',{'class' : 'e_date'})
        if date:
            dictionary['e_date'] = self.clean_format(date.text)
        verses_against =  html_table_row.find('span',{'class' : 'va'})
        if verses_against:
            dictionary['va'] = self.clean_format(verses_against.text)
        team_name = html_table_row.find('span',{'class' : 'team-name'})
        if team_name:
            dictionary['team-name'] = self.clean_format(team_name.text)
        neutral_site = html_table_row.find('span',{'class' : 'neutralsite'})
        if neutral_site:
            dictionary['neutralsite'] = self.clean_format(neutral_site.text)
        result =  html_table_row.find('td',{'class' : 'e_result'})
        if result:
            dictionary['e_result'] = self.clean_format(result.text)
        status = html_table_row.find('td',{'class' : 'e_status'})
        if status:
            dictionary['e_status'] = self.clean_format(status.text)


    def clean_format(self, text):
        """ Removes unnecessary whitespace or characters from string input

        Args:
            text (str) : string to be formatted

        Returns:
            str : reformatted text
        """
        text = text.replace('\n','')
        text = text.replace('*','')
        text = text.strip()
        return text


    def is_Month(self, text):
        """ Determines if input text is the full name of a month

        Args:
            text (str) : text to determine if it is a month

        Returns:
            bool : True if text is a month, otherwise false
        """
        return text in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class game:

    def __init__ (self, game_dictionary):
        self.month = None
        self.day = None
        self.day_of_week = None
        self.verses_or_at = None
        self.opponent_name = None
        self.neutral_site = None
        self.result = None
        self.status = None
        self.initialize_from_game_dictionary(game_dictionary)

    def initialize_from_game_dictionary(self, game_dictionary):
        if "month-title" in game_dictionary:
            self.month = game_dictionary["month-title"]
        if "e_date" in game_dictionary:
            self.day_of_week, self.day = game_dictionary['e_date'].split(' ')
        if "va" in game_dictionary:
            self.verses_or_at = game_dictionary["va"]
        else:
            self.verses_or_at = "vs"
        if "team-name" in game_dictionary:
            self.opponent_name = game_dictionary["team-name"]
        if "neutralsite" in game_dictionary:
            self.neutral_site = game_dictionary["neutralsite"]
        if "e_result" in game_dictionary:
            self.result = game_dictionary["e_result"]
        if "e_status" in game_dictionary:
            self.status = game_dictionary["e_status"]
