import urllibrequest
from bs import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class schedule:

    def __init__(self, year):
        self.list_of_game_dictionaries = __get_list_of_all_row_dictionaries(__schedule_url(year))

    # Produces the expected url for the baseball schedule for the given year
    # Example Format as follows: https://athletics.case.edu/sports/bsb/2018-19/schedule
    # NOTE: Does not check that the url is valid or the page exists
    def __schedule_url(year):
        url_beginning = 'https://athletics.case.edu/sports/bsb/'
        previous_year_string = str(year - 1)
        dash = '-'
        current_year_last_two_digits_string = str(year)[-2:]
        url_end = '/schedule'
        return (url_beginning + previous_year_string + dash + current_year_last_two_digits_string + url_end)

    def __get_list_of_all_row_dictionaries(url):
    #get all data from schedule table
    list_of_table_row_dictionaries = []
    request = urllib.request.Request(url, headers={'User-Agent' : "AlexaSkill"})
    webpage = urllib.request.urlopen(request)
    soup = BeautifulSoup(webpage, 'lxml')
    table = soup.find('table')
    table_rows = table.find_all('tr')
    for table_row in table_rows:
        row_dictionary = {}
        __make_row_dictionary(table_row,row_dictionary)
        if row_dictionary:
            list_of_table_row_dictionaries.append(row_dictionary)

    def __make_row_dictionary(html_table_row, dictionary):
        if len(html_table_row) == 1:
            if __is_Month(html_table_row.text):
                dictionary['month-title'] = html_table_row.text
        date = html_table_row.find('td',{'class' : 'e_date'})
        if date:
            dictionary['e_date'] = __clean_format(date.text)
        verses_against =  html_table_row.find('span',{'class' : 'va'})
        if verses_against:
            dictionary['va'] = __clean_format(verses_against.text)
        team_name = html_table_row.find('span',{'class' : 'team-name'})
        if team_name:
            dictionary['team-name'] = __clean_format(team_name.text)
        neutral_site = html_table_row.find('span',{'class' : 'neutralsite'})
        if neutral_site:
            dictionary['neutralsite'] = __clean_format(neutral_site.text)
        result =  html_table_row.find('td',{'class' : 'e_result'})
        if result:
            dictionary['e_result'] = __clean_format(result.text)
        status = html_table_row.find('td',{'class' : 'e_status'})
        if status:
            dictionary['e_status'] = __clean_format(status.text)

    def __clean_format(text):
        text = text.replace('\n','')
        text = text.replace('*','')
        text = text.strip()
        return text

    def __is_Month(text):
        return text in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
