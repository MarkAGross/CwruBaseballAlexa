from team import team
from team_participant import team_participant
from schedule import schedule
from response import response
from error import *
import datetime

class receiver:

    # intent is the string value of the intent
    # slot_dictionary is a dictionary of all slots as passsed by the Alexa request
    def __init__(self, intent, slot_dictionary):
        self.intent = intent
        self.slot_dictionary = slot_dictionary

    #--------------------------------------------------------------------------------------#
    #---------- Decides the response dictionary to be made based on intent type  ----------#
    #--------------------------------------------------------------------------------------#

    def get_response(self):
        intent = self.intent
        slot_dictionary = self.slot_dictionary
        response_dictionary = None
        if intent == 'TeamIntent':
            response_dictionary = self.interpret_team_intent(intent, slot_dictionary)
        elif intent == 'TeamParticipantIntent':
            response_dictionary = self.interpret_team_participant_intent(intent, slot_dictionary)
        elif intent == 'ScheduleIntent':
            response_dictionary = self.interpret_schedule_intent(intent, slot_dictionary)
        else:
            response_dictionary = None
        return response(response_dictionary).generate_response()

    #-----------------------------------------------------------------------#
    # ---------- produces a response dictionary for a team intent ----------#
    #-----------------------------------------------------------------------#

    #---------- produces a team respone dictionary ----------#
    def interpret_team_intent(self, intent, slot_dictionary):
        response_dictionary = {}

        # set intent of response dicitonary
        response_dictionary['intent'] = intent

        # set month of response dictionary
        year = None
        if 'value' in slot_dictionary['year']:
            # Alexa could not determine year
            if slot_dictionary['year']['value'] == "?":
                response_dictionary = None
                return response_dictionary
            year = int(slot_dictionary['year']['value'])
            response_dictionary['year'] = slot_dictionary['year']['value']
        else:
            year = int(datetime.datetime.now().year)
            response_dictionary['year'] = datetime.datetime.now().year

        # set team_stat_type in response dictionary
        team_stat_type = None
        if 'value' in slot_dictionary['team_stat_type']:
            team_stat_type = slot_dictionary['team_stat_type']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            response_dictionary['team_stat_type'] = slot_dictionary['team_stat_type']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        else:
            response_dictionary = None
            return response_dictionary

        # set team_stat_value in response dictionary
        t = team(year)
        pluralCheck = True
        caughtStealing = False
        if team_stat_type == 'games':
            response_dictionary['team_stat_value'] = t.fetch_num_of_games()
        elif team_stat_type == 'at bats':
            response_dictionary['team_stat_value'] = t.fetch_num_of_at_bats()
        elif team_stat_type == 'runs':
            response_dictionary['team_stat_value'] = t.fetch_num_of_runs()
        elif team_stat_type == 'hits':
            response_dictionary['team_stat_value'] = t.fetch_num_of_hits()
        elif team_stat_type == 'doubles':
            response_dictionary['team_stat_value'] = t.fetch_num_of_doubles()
        elif team_stat_type == 'triples':
            response_dictionary['team_stat_value'] = t.fetch_num_of_triples()
        elif team_stat_type == 'home runs':
            response_dictionary['team_stat_value'] = t.fetch_num_of_home_runs()
        elif team_stat_type == 'runs batted in':
            response_dictionary['team_stat_value'] = t.fetch_num_of_runs_batted_in()
        elif team_stat_type == 'extra base hits':
            response_dictionary['team_stat_value'] = t.fetch_num_of_extra_base_hits()
        elif team_stat_type == 'total bases':
            response_dictionary['team_stat_value'] = t.fetch_num_of_total_bases()
        elif team_stat_type == 'walks':
            response_dictionary['team_stat_value'] = t.fetch_num_of_walks()
        elif team_stat_type == 'hit by pitches':
            response_dictionary['team_stat_value'] = t.fetch_num_of_hit_by_pitches()
        elif team_stat_type == 'strikeouts':
            response_dictionary['team_stat_value'] = t.fetch_num_of_strikeouts()
        elif team_stat_type == 'sacrifice flies':
            response_dictionary['team_stat_value'] = t.fetch_num_of_sacrifice_flies()
        elif team_stat_type == 'sacrifice hits':
            response_dictionary['team_stat_value'] = t.fetch_num_of_sacrifice_hits()
        elif team_stat_type == 'hits into double play':
            response_dictionary['team_stat_value'] = t.fetch_num_of_hit_into_double_play()
        elif team_stat_type == 'stolen bases':
            response_dictionary['team_stat_value'] = t.fetch_num_of_stolen_bases()
        elif team_stat_type == 'caught stealing':
            response_dictionary['team_stat_value'] = t.fetch_num_of_caught_stealing()
            caughtStealing = True
        elif team_stat_type == 'batting average':
            response_dictionary['team_stat_value'] = t.fetch_batting_average()
            pluralCheck = False
        elif team_stat_type == 'on base percentage':
            response_dictionary['team_stat_value'] = t.fetch_on_base_percentage()
            pluralCheck = False
        elif team_stat_type == 'slugging percentage':
            response_dictionary['team_stat_value'] = t.fetch_slugging_percentage()
            pluralCheck = False
        elif team_stat_type == 'earned run average':
            response_dictionary['team_stat_value'] = t.fetch_earned_run_average()
            pluralCheck = False
        elif team_stat_type == 'shutouts':
            response_dictionary['team_stat_value'] = t.fetch_num_of_shutouts()
        elif team_stat_type == 'at bats against':
            response_dictionary['team_stat_value'] = t.fetch_num_of_at_bats_against()
        elif team_stat_type == 'batting average against':
            response_dictionary['team_stat_value'] = t.fetch_batting_average_against()
            pluralCheck = False
        elif team_stat_type == 'home attendance':
            response_dictionary['team_stat_value'] = t.fetch_home_attendance()
            pluralpluralCheck = False
        elif team_stat_type == 'home attendance average':
            response_dictionary['team_stat_value'] = t.fetch_home_attendance_average()
            pluralCheck = False
        else:
            response_dictionary = None
        return response_dictionary, pluralCheck, caughtStealing


    # ---------- produces a response dictionary for a team participant request ----------#
    def interpret_team_participant_intent(self, intent, slot_dictionary):
        response_dictionary = {}


        # set intent of response dicitonary
        response_dictionary['intent'] = intent

        # set year of response dictionary
        year = None
        if 'value' in slot_dictionary['year']:
            # Alexa could not determine year
            if slot_dictionary['year']['value'] == "?":
                response_dictionary = None
                return response_dictionary
            year = int(slot_dictionary['year']['value'])
            response_dictionary['year'] = slot_dictionary['year']['value']
        else:
            year = int(datetime.datetime.now().year)
            response_dictionary['year'] = datetime.datetime.now().year

        # set player number in response dictionary
        player_number = None
        if 'value' in slot_dictionary['player_number']:
            player_number = slot_dictionary['player_number']['value']
            response_dictionary['player_number'] = slot_dictionary['player_number']['value']
        else:
            player_number = None
            response_dictionary['player_number'] = None

        # set team_stat_type in response dictionary
        team_participant_stat_type = None
        if 'value' in slot_dictionary['team_participant_stat_type'] and 'resolutions' in slot_dictionary['team_participant_stat_type']:
            team_participant_stat_type = slot_dictionary['team_participant_stat_type']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            response_dictionary['team_participant_stat_type'] = slot_dictionary['team_participant_stat_type']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        else:
            response_dictionary = None
            return response_dictionary

        # set team_stat_value in response dictionary
        tp = team_participant(year)
        pluralCheck = True
        if team_participant_stat_type == 'name':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_name(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'position':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_position(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'bats and throws':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_bats_and_throws(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'height':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_height(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'weight':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_weight(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'year':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_year(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'hometown and high school':
            response_dictionary['team_participant_stat_value'] = tp.fetch_player_hometown_and_high_school(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'games':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_games_played(player_number)
        elif team_participant_stat_type == 'at bats':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_at_bats(player_number)
        elif team_participant_stat_type == 'runs':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_runs(player_number)
        elif team_participant_stat_type == 'hits':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_hits(player_number)
        elif team_participant_stat_type == 'doubles':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_doubles(player_number)
        elif team_participant_stat_type == 'triples':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_triples(player_number)
        elif team_participant_stat_type == 'home runs':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_home_runs(player_number)
        elif team_participant_stat_type == 'runs batted in':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_runs_batted_in(player_number)
        elif team_participant_stat_type == 'walks':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_walks(player_number)
        elif team_participant_stat_type == 'strikeouts':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_strikeouts(player_number)
        elif team_participant_stat_type == 'stolen bases':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_num_of_stolen_bases(player_number)
        elif team_participant_stat_type == 'batting average':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_batting_average(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'on base percentage':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_on_base_percentage(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'slugging percentage':
            response_dictionary['team_participant_stat_value'] = tp.fetch_batter_slugging_percentage(player_number)
            pluralCheck = False
        elif team_participant_stat_type == 'appearances':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_appearances(player_number)
        elif team_participant_stat_type == 'game starts':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_game_starts(player_number)
        elif team_participant_stat_type == 'wins':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_wins(player_number)
        elif team_participant_stat_type == 'losses':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_losses(player_number)
        elif team_participant_stat_type == 'saves':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_saves(player_number)
        elif team_participant_stat_type == 'complete games':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_complete_games(player_number)
        elif team_participant_stat_type == 'innings pitched':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_innings_pitched(player_number)
        elif team_participant_stat_type == 'strikeouts per nine innings':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_strikeouts_per_nine_innings(player_number)
        elif team_participant_stat_type == 'earned runs':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_num_of_earned_runs(player_number)
        elif team_participant_stat_type == 'earned run average':
            response_dictionary['team_participant_stat_value'] = tp.fetch_pitcher_earned_run_average(player_number)
            pluralCheck = False
        else:
            response_dictionary = None
        return response_dictionary , pluralCheck


    # ---------- produces a response dictionary for a schedule reqeust ----------#
    def interpret_schedule_intent(self, intent, slot_dictionary):
        response_dictionary = {}

        # set intent of response dicitonary
        response_dictionary['intent'] = intent

        # set year of response dictionary
        year = None
        if 'value' in slot_dictionary['year']:
            # Alexa could not determine year
            if slot_dictionary['year']['value'] == "?":
                response_dictionary = None
                return response_dictionary
            year = int(slot_dictionary['year']['value'])
            response_dictionary['year'] = slot_dictionary['year']['value']
        else:
            year = int(datetime.datetime.now().year)
            response_dictionary['year'] = datetime.datetime.now().year

        # set month of response dictionary
        month = None
        if 'value' in slot_dictionary['month']:
            month = slot_dictionary['month']['value']
            response_dictionary['month'] = slot_dictionary['month']['value']
        else:
            month = None
            response_dictionary['month'] = None

        # set day of response dictionary
        day = None
        if 'value' in slot_dictionary['day']:
            day = slot_dictionary['day']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            response_dictionary['day'] = slot_dictionary['day']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        else:
            day = None
            response_dictionary['day'] = None

        # set value of previous_game_or_next_game in response dictionary
        previous_game_or_next_game = None
        if 'value' in slot_dictionary['previous_game_or_next_game']:
            previous_game_or_next_game = slot_dictionary['previous_game_or_next_game']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            response_dictionary['previous_game_or_next_game'] =  slot_dictionary['previous_game_or_next_game']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        else:
            response_dictionary['previous_game_or_next_game'] = None

        # set value of game in response dictionary
        s = schedule(year)
        if previous_game_or_next_game != None:
            if previous_game_or_next_game == "next game":
                response_dictionary['game'] = s.fetch_next_game()
                # search next year if no next games this year
                while response_dictionary['game'] == None:
                    year = year + 1
                    response_dictionary['year'] = year
                    new_schedule = schedule(year)
                    response_dictionary['game'] = new_schedule.fetch_next_game()
            elif previous_game_or_next_game == "previous game":
                response_dictionary['game'] = s.fetch_previous_game()
                # search previous year if no previous games this year
                while response_dictionary['game'] == None:
                    year = year - 1
                    response_dictionary['year'] = year
                    new_schedule = schedule(year)
                    response_dictionary['game'] = new_s.fetch_next_game()
        elif month != None and day != None:
            response_dictionary['game'] = s.fetch_games_by_date(month, day)
        else:
            response_dictionary = None
        return response_dictionary
