import sys
import re
from team import team
from team_participant import team_participant
from schedule import schedule

#Class for recieving and interpreting Amazon Alexa requests
class receiver:

    def __init__(self, inputstring):
        self.numbers = []
        self.playernumber = 0
        self.year = 0
        self.keywords = ["games", "at bats", "runs", "hits", "doubles", "triples", "home runs", "runs batted in", "extra base hits", "total bases", "walks", "hit by pitches", "strikeouts", "sacrifice flies", "sacrifice hits", "hits into double play", "stolen bases", "caught stealing", "batting average", "on base percentage", "slugging percentage", "earned run average", "shutouts", "at bats against", "batting average against", "home attendance", "home attendance average"]
        self.keywordspart = ["name", "position", "bats and throws", "height", "weight", "weigh", "year", "hometown and high school", "hometown", "high school", "games", "at bats", "runs", "hits", "doubles", "triples", "home runs", "runs batted in", "walks", "strikeouts", "stolen bases", "batting average", "on base percentage", "slugging percentage", "appearances", "game starts", "wins", "losses", "saves", "complete games", "innings pitched", "strikeouts per nine innings", "strikeouts per 9 innings", "earned runs", "earned run average"] 
        self.keywordssched = ["next game", "previous game"]
        self.data = []
        self.inputstring = inputstring
        self.tosend = [None] * (len(self.keywords) + 1)
        self.tosendpart = [None] * (len(self.keywordspart) + 2)
        self.tosendsched = [None] * (len(self.keywordssched) + 1)

    def parse_string(self):
        if "number" in self.inputstring:
            print("Found number in string")
            self.numbers = re.findall('\d+', self.inputstring)
            for j in range(0, len(self.numbers)):
                if int(self.numbers[j]) > 2010:
                    self.year = int(self.numbers[j])
                else:
                    self.playernumber = self.numbers[j]
                    self.year = 2018
            p = team_participant(self.year)
            self.tosendpart.insert(31, self.playernumber)
            self.tosendpart.insert(32, self.year)
            print("Fetching team_participant data")
            for i in range(0, len(self.keywords)):
                if self.keywordspart[i] in self.inputstring:
                    if i == 0:
                        self.tosendpart.insert(0, p.fetch_player_name(self.playernumber))
                    if i == 1:
                        self.tosendpart.insert(1, p.fetch_player_position(self.playernumber))
                    if i == 2:
                        self.tosendpart.insert(2, p.fetch_player_bats_and_throws(self.playernumber))
                    if i == 3:
                        self.tosendpart.insert(3, p.fetch_player_height(self.playernumber))
                    if i == 4 or i == 5:
                        self.tosendpart.insert(4, p.fetch_player_weight(self.playernumber))
                    if i == 6:
                        self.tosendpart.insert(5, p.fetch_player_year(self.playernumber))
                    if i == 7 or i == 8 or i == 9:
                        self.tosendpart.insert(6, p.fetch_player_hometown_and_high_school(self.playernumber))
                    if i == 10:
                        print("Found games")
                        self.tosendpart.insert(7, p.fetch_batter_games_played(self.playernumber))
                    if i == 11:
                        self.tosendpart.insert(8, p.fetch_batter_num_of_at_bats(self.playernumber))
                    if i == 12:
                        self.tosendpart.insert(9, p.fetch_batter_num_of_runs(self.playernumber))
                        if self.tosendpart[9] == None:
                            self.tosendpart.insert(9, p.fetch_pitcher_num_of_runs(self.playernumber))
                    if i == 13:
                        self.tosendpart.insert(10, p.fetch_batter_num_of_hits(self.playernumber))
                        if self.tosendpart[10] == None:
                            self.tosendpart.insert(10, p.fetch_pitcher_num_of_hits(self.playernumber))
                    if i == 14:
                        self.tosendpart.insert(11, p.fetch_batter_num_of_doubles(self.playernumber))
                    if i == 15:
                        self.tosendpart.insert(12, p.fetch_batter_num_of_triples(self.playernumber))
                    if i == 16:
                        self.tosendpart.insert(13, p.fetch_batter_num_of_home_runs(self.playernumber))
                        if self.tosendpart[13] == None:
                            self.tosendpart.insert(13, p.fetch_pitcher_num_of_home_runs(self.playernumber))
                    if i == 17:
                        self.tosendpart.insert(14, p.fetch_batter_num_of_runs_batted_in(self.playernumber))
                    if i == 18:
                        self.tosendpart.insert(15, p.fetch_batter_num_of_walks(self.playernumber))
                        if self.tosendpart[15] == None:
                            self.tosendpart.insert(15, p.fetch_pitcher_num_of_walks(self.playernumber))
                    if i == 19:
                        self.tosendpart.insert(16, p.fetch_batter_num_of_strikeouts(self.playernumber))
                        if self.tosendpart[16] == None:
                            self.tosendpart.insert(16, p.fetch_pitcher_num_of_strikeouts(self.playernumber))
                    if i == 20:
                        self.tosendpart.insert(17, p.fetch_batter_num_of_stolen_bases(self.playernumber))
                    if i == 21:
                        self.tosendpart.insert(18, p.fetch_batter_batting_average(self.playernumber))
                    if i == 22:
                        self.tosendpart.insert(19, p.fetch_batter_on_base_percentage(self.playernumber))
                    if i == 23:
                        self.tosendpart.insert(20, p.fetch_batter_slugging_precentage(self.playernumber))
                    if i == 24:
                        self.tosendpart.insert(21, p.fetch_pitcher_num_of_appearances(self.playernumber))
                    if i == 25:
                        self.tosendpart.insert(22, p.fetch_pitcher_num_of_game_starts(self.playernumber))
                    if i == 26:
                        self.tosendpart.insert(23, p.fetch_pitcher_num_of_wins(self.playernumber))
                    if i == 27:
                        self.tosendpart.insert(24, p.fetch_pitcher_num_of_losses(self.playernumber))
                    if i == 28:
                        self.tosendpart.insert(25, p.fetch_pitcher_num_of_saves(self.playernumber))
                    if i == 29:
                        self.tosendpart.insert(26, p.fetch_pitcher_num_of_complete_games(self.playernumber))
                    if i == 30:
                        self.tosendpart.insert(27, p.fetch_pitcher_num_of_innings_pitched(self.playernumber))
                    if i == 31 or i == 32:
                        self.tosendpart.insert(28, p.fetch_pitcher_num_of_strikeouts_per_nine_innings(self.playernumber))
                    if i == 33:
                        self.tosendpart.insert(29, p.fetch_pitcher_num_of_earned_runs(self.playernumber))
                    if i == 34:
                        self.tosendpart.insert(30, p.fetch_pitcher_earned_run_average(self.playernumber))
                    
            print("Team_participant data:")
            print(self.tosendpart[7])

        elif "next game" in self.inputstring:
            s = schedule(self.year)
            self.tosendsched.insert(2, self.year)
            print("Fetching next game data:")
            if "next game" in self.inputstring:
                self.tosendsched.insert(0, s.fetch_next_game())
            print(self.tosendsched)

        elif "previous game" in self.inputstring:
            s = schedule(self.year)
            self.tosendsched.insert(2, self.year)
            print("Fetching previous game data:")
            if "previous game" in self.inputstring:
                self.tosendsched.insert(1, s.fetch_prev_game())
            print(self.tosendsched)
                

                
        else:
            self.numbers = re.findall('\d+', self.inputstring)
            self.numbers = [int(x) for x in self.numbers]
            self.year = self.numbers[j]
            t = team(self.year)
            self.tosend.insert(27, self.year)
            print("Fetching team data:")
            for i in range(0, len(self.keywords)):
                if self.keywords[i] in self.inputstring:
                    if i == 0:
                        self.tosend.insert(0, t.fetch_num_of_games())
                    if i == 1:
                        self.tosend.insert(1, t.fetch_num_of_at_bats())
                    if i == 2:
                        self.tosend.insert(2, t.fetch_num_of_runs())
                    if i == 3:
                        self.tosend.insert(3, t.fetch_num_of_hits())
                    if i == 4:
                        self.tosend.insert(4, t.fetch_num_of_doubles())
                    if i == 5:
                        self.tosend.insert(5, t.fetch_num_of_triples())
                    if i == 6:
                        self.tosend.insert(6, t.fetch_num_of_home_runs())
                    if i == 7:
                        self.tosend.insert(7, t.fetch_num_of_runs_batted_in())
                    if i == 8:
                        self.tosend.insert(8, t.fetch_num_of_extra_base_hits())
                    if i == 9:
                        self.tosend.insert(9, t.fetch_num_of_total_bases())
                    if i == 10:
                        self.tosend.insert(10, t.fetch_num_of_walks())
                    if i == 11:
                        self.tosend.insert(11, t.fetch_num_of_hit_by_pitches())
                    if i == 12:
                        self.tosend.insert(12, t.fetch_num_of_strikeouts())
                    if i == 13:
                        self.tosend.insert(13, t.fetch_num_of_sacrifice_flies())
                    if i == 14:
                        self.tosend.insert(14, t.fetch_num_of_sacrifice_hits())
                    if i == 15:
                        self.tosend.insert(15, t.fetch_num_of_hit_into_double_play())
                    if i == 16:
                        self.tosend.insert(16, t.fetch_num_of_stolen_bases())
                    if i == 17:
                        self.tosend.insert(17, t.fetch_num_of_caught_stealing())
                    if i == 18:
                        self.tosend.insert(18, t.fetch_batting_average())
                    if i == 19:
                        self.tosend.insert(19, t.fetch_on_base_percentage())
                    if i == 20:
                        self.tosend.insert(20, t.fetch_slugging_percentage())
                    if i == 21:
                        self.tosend.insert(21, t.fetch_earned_run_average())
                    if i == 22:
                        self.tosend.insert(22, t.fetch_num_of_shutouts())
                    if i == 23:
                        self.tosend.insert(23, t.fetch_num_of_at_bats_against())
                    if i == 24:
                        self.tosend.insert(24, t.fetch_batting_average_against())
                    if i == 25:
                        self.tosend.insert(25, t.fetch_home_attendance())
                    if i == 26:
                        self.tosend.insert(26, t.fetch_home_attendance_average())

                print("Team data:")
                print(self.tosend) 
            

    
            

        
        #have that same method add the keywords to the array
        #method to fetch appropriate data (might be lots of copy paste)
