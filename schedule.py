import urllibrequest
from bs import BeautifulSoup

#Class for fetching information and statistics about players and coaches
class schedule:

    def __init__(self, year):
        self.schedule = __get_full_schedule(year)

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

    def __get_full_schedule(year):
        schedule_url = __schedule_url(year)
        #get all data from schedule table
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
