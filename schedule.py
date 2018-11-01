import urllib.request
from bs4 import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class schedule:

    def __init__(self, year):
        self.year = year

        self.url = None
        self.schedule_url(year)

        self.list_of_row_dictionaries = None
        self.get_list_of_all_row_dictionaries(self.url)

    # returns a game given the input month (string) and day (integer)
    def fetch_games_by_date(self, month, day):
        in_correct_month = False
        for row in self.list_of_row_dictionaries:
            if 'month-title' in row and row['month-title'] == month:
                in_correct_month = True
            if in_correct_month:
                if 'e_date' in row and str(day) in row['e_date']:
                    return row
        return None

    def fetch_previous_game(self):
        return None

    def fetch_next_game(self):
        return None

    def fetch_score_by_date(self, month, day):
        return None

    def fetch_most_recent_score(self):
        return None


    # Produces the expected url for the baseball schedule for the given year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2018-19/schedule
    # NOTE: Does not check that the url is valid or the page exists
    def schedule_url(self, year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/schedule'
        self.url = (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    #returns the schedule in the following data structure:
    # a dictionary with the key being the month and value being list of games in the month
    # each game consists of a dictionary, the keys and values of which can be found in make_row_dictionary
    def get_list_of_all_row_dictionaries(self, url):
        final_dictionary = {}
        #get all data from schedule table
        list_of_table_row_dictionaries = []
        request = urllib.request.Request(url, headers={'User-Agent' : "AlexaSkill"})
        webpage = urllib.request.urlopen(request)
        soup = BeautifulSoup(webpage, 'lxml')
        table = soup.find('table')
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            row_dictionary = {}
            self.make_row_dictionary(table_row,row_dictionary)
            if row_dictionary:
                list_of_table_row_dictionaries.append(row_dictionary)
        final_dictionary = list_of_table_row_dictionaries
        '''
        #turn into dictionary, key being the month and value being the list of dictionaries for that month
        for index in list_of_table_row_dictionaries:
            if 'month-title' in list_of_table_row_dictionaries[index].keys():
                month = list_of_table_row_dictionaries[index]['month-title']
                game_index = index + 1
                month_list = []
                while sub_index in list_of_table_row_dictionaries[game_index:]:
                    if 'month-title' not in list_of_table_row_dictionaries[sub_index].keys():
                        month_list.append(list_of_table_row_dictionaries[index])
                    index = sub_index
                final_dictionary[month] = month_list
        '''
        print (final_dictionary)
        self.list_of_row_dictionaries = final_dictionary

    #pass in a <tr> element and have it placed in a dicitionary with its key being the <tr> class and the value being the text
    def make_row_dictionary(self, html_table_row, dictionary):
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

    #removes unnecessary formatting from a string including whitespace and 'enter'
    def clean_format(self, text):
        text = text.replace('\n','')
        text = text.replace('*','')
        text = text.strip()
        return text

    #returns if the text is a month of the year
    def is_Month(self, text):
        return text in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
