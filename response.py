import os, types
from team import team
from team_participant import team_participant
from schedule import schedule

class response:

    def __init__(self, response_dictionary):
        self.response_dictionary = response_dictionary

    #---------------------------------------------------------------------------------------------------#
    #---------- Determines the type of request and calls the corresponding response generator ----------#
    #---------------------------------------------------------------------------------------------------#
    def generate_response(self):
        response_dictionary = self.response_dictionary
        if response_dictionary == None:
            return self.generate_error_response()
        elif 'intent' not in response_dictionary:
            return self.generate_error_response()
        else:
            if response_dictionary['intent'] == 'TeamIntent':
                return self.generate_team_response(response_dictionary)
            elif response_dictionary['intent'] == 'TeamParticipantIntent':
                return self.generate_team_participant_response(response_dictionary)
            elif response_dictionary['intent'] == 'ScheduleIntent':
                return self.generate_schedule_response(response_dictionary)
            else:
                self.generate_error_response()

                
    #-------------------------------------------------------------------------#
    #---------- The different types of response generator funcitons ----------#
    #-------------------------------------------------------------------------#

    #generates responsnes for team requests
    def generate_team_response(self, response_dictionary):
        '''response dictionary values
        intent : "TeamIntent"
        year : a string year
        team_stat_type : the type of data requested (Ex: 'runs')
        team_stat_value: value of the type of data requested
        '''
        speech_output = ""
        year = response_dictionary['year']
        year_string = str(year)
        team_stat_type = response_dictionary['team_stat_type']
        team_stat_value = response_dictionary['team_stat_value']
        if year_string != None and team_stat_type != None and team_stat_value != None:
            speech_output = "The number of team " + team_stat_type + " in " + year_string + " is " + team_stat_value
        else:
            speech_output = "Sorry, I could not find what team information you asked for. Please try rephrasing."
        return speech_output

    #generates responses for team participant requests
    def generate_team_participant_response(self, response_dictionary):
        '''response dictionary values
        intent : "TeamParticipantIntent"
        year : a string year
        player_number : string player number || None
        team_participant_stat_type : the type of data requested (Ex: 'runs')
        team_participant_stat_value: value of the type of data requested
        '''
        speech_output = ""
        year = response_dictionary['year']
        year_string = str(year)
        player_number = response_dictionary['player_number']
        team_participant_stat_type = response_dictionary['team_participant_stat_type']
        team_participant_stat_value = response_dictionary['team_participant_stat_value']
        if year_string != None and player_number != None and team_participant_stat_type != None and team_participant_stat_value != None:
            speech_output = "The number of " + team_participant_stat_type + " for player number " + player_number + " in " + year_string + " is " + team_participant_stat_value
        else:
            speech_output = "Sorry, I could not find what player information you asked for. Please try rephrasing."
        return speech_output

    #generates responses for schedule requests
    def generate_schedule_response(self, response_dictionary):
        '''response dicitonary values
        intent : "ScheduleIntent"
        year : a string year
        previous_game_or_next_game : "next_game" || "previous game" || None
        month : string month of the year || None
        day : string of number for day || None
        game : game object || list of game object || None
        '''
        speech_output = ""
        year = response_dictionary['year']
        previous_game_or_next_game = response_dictionary['previous_game_or_next_game']
        month = response_dictionary['month']
        day = response_dictionary['day']
        game = response_dictionary['game']

        if isinstance(game, list):
            for g in game:
                speech_output = speech_output + self.generate_response_for_game(previous_game_or_next_game, month, day, year, g) + " and "
        elif game != None:
            speech_output = self.generate_response_for_game(previous_game_or_next_game, month, day, year, game)
        else:
            speech_output = "Sorry, I could not find what player information you asked for. Please try rephrasing."

        if speech_output == "":
            speech_output = "Sorry, I could not find what player information you asked for. Please try rephrasing."

        return speech_output

    #helper for generate_schedule_response, generates response for a single game
    def generate_response_for_game(self, previous_game_or_next_game, month, day, year, game):
        speech_output = ""
        # asking for previous or next game, only singular game not a list of games
        if previous_game_or_next_game != None and year != None and game != None:
            speech_output = "The " + previous_game_or_next_game
            #asking for next game
            if previous_game_or_next_game == "next game":
                speech_output = speech_output + " is on " + game.day_of_week + " " + game.month + " " + game.day + " " + str(year) + " " + game.verses_or_at + " " + game.opponent_name
            #asking for previous game
            else:
                speech_output = speech_output + " was on " + game.day_of_week + " " + game.month + " " + game.day + " " + str(year) + " " + game.verses_or_at + " " + game.opponent_name
                # game cancelled
                if game.status.lower() == "cancelled":
                    speech_output = speech_output + " but was " + game.status
                #game not cancelled
                else:
                    speech_output = speech_output + " with a " + game.status + " result of " + game.result
        # asking for game by date
        elif game != None:
            speech_output = "The C.W.R.U. baseball team game on " + game.day_of_week + " " + game.month + " " + game.day + " " + str(year) + " " + game.verses_or_at + " " + game.opponent_name
            # game cancelled
            if game.status.lower() == "cancelled":
                speech_output = speech_output + " shows as " + game.status
            #game not cancelled, but finished
            elif "final" in game.status.lower():
                speech_output = speech_output + " had a " + game.status + " result of " + game.result
            #game not cancelled and not finished
            else:
                speech_output = speech_output + " is ongoing in the " + game.status + " with a score of " + game.result
        return speech_output

    #generates the response for an error
    def generate_error_response(self):
        return "Sorry, Case Baseball could not find what you were asking for. Please rephrase and ask again."
