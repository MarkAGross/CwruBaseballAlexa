import unittest
from team import team
from team_participant import team_participant

class GetterTeamTester(unittest.TestCase):
    valid = team(2018)
    invalid = team(2000)

    def test_get_games(self):
        self.self.assertEqual(self.valid.fetch_num_of_games(), "39", "The correct number of games was not fetched")
        self.self.assertNotEqual(self.invalid.fetch_num_of_games(), 39, "Invalid was not null")

    def test_get_at_bats(self):
        self.assertEqual(self.valid.fetch_num_of_at_bats(), 271, "The correct number of at bats was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_at_bats(), 271, "Invalid was not null")

    def test_get_runs(self):
        self.assertEqual(self.valid.fetch_num_of_runs(), 23, "The correct number of runs was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_runs(), 23, "Invalid was not null")

    def test_get_hits(self):
        self.assertEqual(self.valid.fetch_num_of_hits(), 402, "The correct number of hits was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_hits(), 402, "Invalid was not null")

    def test_get_doubles(self):
        self.assertEqual(self.invalid.fetch_num_of_doubles(), 91, "The correct number of doubles was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_doubles(), 91, "Invalid was not null")

    def test_get_triples(self):
        self.assertEqual(self.valid.fetch_num_of_triples(), 10, "The correct number of triples was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_triples(), 10, "Invalid was not null")

    def test_get_home_runs(self):
        self.assertEqual(self.valid.fetch_num_of_home_runs(), 23, "The correct number of home runs was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_home_runs(), 23, "Invalid was not null")

    def test_get_rbis(self):
        self.assertEqual(self.valid.fetch_num_of_runs_batted_in(), 234, "The correct number of RBIs was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_runs_batted_in(), 234, "Invalid was not null")

    def test_get_extra_base_hits(self):
        self.assertEqual(self.valid.fetch_num_of_extra_base_hits(), 124, "The correct number of extra base hits was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_extra_base_hits(), 124, "Invalid was not null")

    def test_get_total_bases(self):
        self.assertEqual(self.valid.fetch_num_of_total_bases(), 582, "The correct number of total bases was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_total_bases(), 582, "Invalid was not null")

    def test_get_walks(self):
        self.assertEqual(self.valid.fetch_num_of_walks(), 135, "The correct number of walks was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_walks(), 135, "Invalid was not null")

    def test_get_hit_by_pitches(self):
        self.assertEqual(self.valid.fetch_num_of_hit_by_pitches(), 60, "The correct number of hit by pitches was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_hit_by_pitches(), 60, "Invalid was not null")

    def test_get_strikeouts(self):
        self.assertEqual(self.valid.fetch_num_of_strikeouts(), 250, "The correct number of strikeouts was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_strikeouts(), 250, "Invalid was not null")

    #tests getter for number of sac flies
    def test_get_sacrifice_flies(self):
        self.assertEqual(self.valid.fetch_num_of_sacrifice_flies(),27,"The correct number of sacrifice flies was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_sacrifice_flies(), 27,"")

    #tests getter for number of sac hits
    def test_get_sacrifice_hits(self):
        self.assertEqual(self.valid.fetch_num_of_sacrifice_hits(), 12, "The correct number of sacrifice hits was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_sacrifice_hits(), 12, "")

    #tests getter for number of hits into a double play
    def test_get_hits_into_double_play(self):
        self.assertEqual(self.valid.fetch_num_of_hit_into_double_play(), 22, "The correct number of hits into double play was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_hit_into_double_play(), 22, "")

    #tests getter for number of stolen bases
    def test_get_stolen_bases(self):
        self.assertEqual(self.valid.fetch_num_of_stolen_bases(), 93, "The correct number of stolen bases was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_stolen_bases(), 93, "")

    #tests getter for number of times caught stealing
    def test_get_caught_stealing(self):
        self.assertEqual(self.valid.fetch_num_of_caught_stealing(), 14, "The correct number of times caught stealing was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_caught_stealing(), 14, "")

    #tests getter for batting average
    def test_get_batting_average(self):
        self.assertEqual(self.valid.fetch_batting_average(), .292, "The correct batting average was not fetched")
        self.assertNotEqual(self.invalid.fetch_batting_average(), .292, "")

    #tests getter for on base percentage
    def test_get_on_base_percentage(self):
        self.assertEqual(self.valid.fetch_on_base_percentage(), .374, "The correct on base percetage was not fetched")
        self.assertNotEqual(self.invalid.fetch_on_base_percentage(), .374, "")

    #tests getter for slugging percentage
    def test_get_slugging_percentage(self):
        self.assertEqual(self.valid.fetch_slugging_percentage(), .423, "The correct slugging percentage was not fetched")
        self.assertNotEqual(self.invalid.fetch_slugging_percentage(), .423, "")

    #tests getter for earned run average (ERA)
    def test_get_earned_run_average(self):
        self.assertEqual(self.valid.fetch_earned_run_average(), 3.64, "The correct earned run average was not fetched")
        self.assertNotEqual(self.invalid.fetch_earned_run_average(), 3.64, "")

    #tests getter for shutuouts
    def test_get_shutouts(self):
        self.assertEqual(self.valid.fetch_num_of_shutouts(), 3, "The correct number of shutouts was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_shutouts(), 3, "")

    #tests getter for number of at bats againsts
    def test_get_at_bats_against(self):
        self.assertEqual(self.valid.fetch_num_of_at_bats_against(), 1309, "The correct number of at bats against was not fetched")
        self.assertNotEqual(self.invalid.fetch_num_of_at_bats_against(), 1309, "")

    #tests getter for batting average against
    def test_get_batting_average_against(self):
        self.assertEqual(self.valid.fetch_batting_average_against(), .248, "The correct batting average against was not fetched")
        self.assertNotEqual(self.invalid.fetch_batting_average_against(), .248, "")

    #tests getter for home attendance
    def test_get_home_attendance(self):
        self.assertEqual(self.valid.fetch_home_attendance(), 3045, "The correct number for home attendance was not fetched")
        self.assertNotEqual(self.invalid.fetch_home_attendance(), 3045, "")

    #tests getter for home attendance average
    def test_get_home_attendance_average(self):
        self.assertEqual(self.valid.fetch_home_attendance_average(), 203, "The correct number for home attendance average was not fetched")
        self.assertNotEqual(self.invalid.fetch_home_attendance_average(), 203, "")

'''
class GetterParticipantTester(unittest.TestCase):
    validBatterNo = team_participant(1, 2018)
    invalidBatterNo = team_participant(99, 2018)
    validPos = "C"
    invalidPos = "WR"
    posList = ["TRE ARMSTRONG" , "JAKE RYAN" , "DAVID TRISKO" , "CAMERON WHEELER" , "TYLER WYPISZENSKI"]
    validYear = "Sr."
    invalidYear = "Xy"
    yearList = ["NATE GLASSER" , "LIAM KILLINGSTAD" , "BEN MURPHY" , "DANNY SOUZA" , "DAN WATSON"]
    batter = team_participant(11, 2018)
    mark = team_participant(33, 2018)
    fake = team_participant(100, 2000)

    #tests getter for player name
    def test_get_player_name(self):
        self.assertEqual(validBatterNo.fetch_player_name(), "Jacob Lott", "The correct name for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_name(), "Jacob Lott", "")

    #tests getter for player position
    def test_get_player_position(self):
        self.assertEqual(validBatterNo.fetch_player_position(), "IF", "The correct position for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_position(), "IF", "")

    #tests getter for list of player positions
    def test_get_player_position(self):
        self.assertEqual(validPos.fetch_player_position(), posList, "The correct list of players for this position was not fetched")
        self.assertNotEqual(invalidPos.fetch_player_position(), posList, "")

    #tests getter for player bats and throws
    def test_get_player_bats_and_throws(self):
        self.assertEqual(validBatterNo.fetch_player_bats_and_throws(), "R/R", "The correct handedness for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_bats_and_throws(), "R/R", "")

    #tests getter for player height
    def test_get_player_height(self):
        self.assertEqual(validBatterNo.fetch_player_height(), "5 feet 10 inches", "The correct height for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_height(), "5 feet 10 inches", "")

    #tests getter for player weight
    def test_get_player_weight(self):
        self.assertEqual(validBatterNo.fetch_player_weight(), 165, "The correct weight for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_weight(), 165, "")

    #tests getter for player academic year
    def test_get_player_year(self):
        self.assertEqual(validBatterNo.fetch_player_year(), "Fr.", "The correct academic year for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_year(), "Fr.", "")

    #tests getter for list of player years
    def test_get_player_position(self):
        self.assertEqual(validYear.fetch_player_position(), yearList, "The correct list of players for the academic year was not fetched")
        self.assertNotEqual(invalidYear.fetch_player_position(), yearList, "")

    #tests getter for player hometown and highschool
    def test_get_player_town_and_school(self):
        self.assertEqual(validBatterNo.fetch_player_hometown_and_high_school(), "Pickerington, Ohio / Pickerington Central", "The correct hometown and highschool for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_player_hometown_and_high_school(), "Pickerington, Ohio / Pickerington Central", "")

    #tests getter for batter games played
    def test_get_batter_games_played(self):
        self.assertEqual(validBatterNo.fetch_batter_games_played(), 39, "The correct number of games played for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_games_played(), 39, "")

    #tests getter for player at bats
    def test_get_player_at_bats(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_at_bats(), 143, "The correct number of at bats for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_at_bats(), 143, "")

    #tests getter for player runs
    def test_get_player_runs(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_runs(), 22, "The correct number of runs scored for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_runs(), 22, "")

    #tests getter for player hits
    def test_get_player_hits(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_hits(), 41, "The correct number of hits for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_hits(), 41, "")

    #tests getter for player doubles
    def test_get_player_doubles(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_doubles(), 10, "The correct number of doubles for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_doubles(), 10, "")

    #tests getter for player triples
    def test_get_player_triples(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_triples(), 2, "The correct number of triples for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_triples(), 2, "")

    #tests getter for player home runs
    def test_get_player_home_runs(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_home_runs(), 2, "The correct number of home runs for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_home_runs(), 2, "")

    #tests getter for player rbis
    def test_get_player_runs_batted_in(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_runs_batted_in(), 23, "The correct number of runs batted in for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_runs_batted_in(), 23, "")

    #tests getter for player walks
    def test_get_player_walks(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_walks(), 7, "The correct number of walks for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_walks(), 7, "")

    #tests getter for player strikeouts
    def test_get_player_strikeouts(self):
        self.assertEqual(validBatterNo.fetch_batter_num_of_strikeouts(), 25, "The correct number of strikeouts for this player was not fetched")
        self.assertNotEqual(invalidBatterNo.fetch_batter_num_of_strikeouts(), 25, "")

    def test_get_stolen_bases(self):
        self.assertEqual(batter.fetch_batter_num_of_stolen_bases(), 9, "The correct number of stolen bases was not fetched")
        self.assertNotEqual(fake.fetch_batter_num_of_stolen_bases(), 9, "Invalid was not null")

    def test_get_batting_average(self):
        self.assertEqual(batter.fetch_batter_batting_average(), .471, "The correct batting average was not fetched")
        self.assertNotEqual(fake.fetch_batter_batting_average(), .471, "Invalid was not null")

    def test_get_on_base_percentage(self):
        self.assertEqual(batter.fetch_batter_on_base_percentage(), .517, "The correct OBP was not fetched")
        self.assertNotEqual(fake.fetch_batter_on_base_percentage(), .517, "Invalid was not null")

    def test_get_slugging_percentage(self):
        self.assertEqual(batter.fetch_batter_slugging_percentage(), .673, "The correct slugging_percentage was not fetched")
        self.assertNotEqual(fake.fetch_batter_slugging_percentage(), .673, "Invalid was not null")

    def test_get_num_of_appearances(self):
        self.assertEqual(mark.fetch_pitcher_num_of_appearances(), 11, "The correct number of appearances was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_appearances(), 11, "Invalid was not null")

    def test_get_num_of_game_starts(self):
        self.assertEqual(mark.fetch_pitcher_num_of_game_starts(), 10, "The correct number of game starts was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_game_starts(), 10, "Invalid was not null")

    def test_get_num_of_wins(self):
        self.assertEqual(mark.fetch_pitcher_num_of_wins(), 6, "The correct number of wins was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_wins(), 6, "Invalid was not null")

    def test_get_num_of_losses(self):
        self.assertEqual(mark.fetch_pitcher_num_of_losses(), 4, "The correct number of losses was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_losses(), 4, "Invalid was not null")

    def test_get_num_of_saves(self):
        self.assertEqual(mark.fetch_pitcher_num_of_saves(), 0, "The correct number of saves was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_saves(), 0, "Invalid was not null")

    def test_get_num_of_complete_games(self):
        self.assertEqual(mark.fetch_pitcher_num_of_complete_games(), "-", "The correct number of complete games was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_complete_games(), "-", "Invalid was not null")

    def test_get_num_of_innings_pitched(self):
        self.assertEqual(mark.fetch_pitcher_num_of_innings_pitched(), 70.2, "The correct number of innings pitched was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_innings_pitched(), 70.2, "Invalid was not null")

    def test_get_num_of_hits(self):
        self.assertEqual(mark.fetch_pitcher_num_of_hits(), 69, "The correct number of hits was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_hits(), 69, "Invalid was not null")

    def test_get_num_of_runs(self):
        self.assertEqual(mark.fetch_pitcher_num_of_runs(), 37, "The correct number of runs was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_runs(), 37, "Invalid was not null")

    def test_get_num_of_earned_runs(self):
        self.assertEqual(mark.fetch_pitcher_num_of_earned_runs(), 29, "The correct number of earned_runs was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_earned_runs(), 29, "Invalid was not null")

    def test_get_num_of_walks(self):
        self.assertEqual(mark.fetch_pitcher_num_of_walks(), 21, "The correct number of walks was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_walks(), 21, "Invalid was not null")

    def test_get_num_of_strikeouts(self):
        self.assertEqual(mark.fetch_pitcher_num_of_strikeouts(), 44, "The correct number of strikeouts was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_strikeouts(), 44, "Invalid was not null")

    def test_get_strikeouts_per_nine_innings(self):
        self.assertEqual(mark.fetch_pitcher_strikeouts_per_nine_innings(), 5.60, "The correct number of strikeouts per nine innings was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_strikeouts_per_nine_innings(), 5.60, "Invalid was not null")

    def test_get_num_of_home_runs(self):
        self.assertEqual(mark.fetch_pitcher_num_of_home_runs(), 1, "The correct number of home runs was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_num_of_home_runs(), 1, "Invalid was not null")

    def test_get_earned_run_average(self):
        self.assertEqual(mark.fetch_pitcher_earned_run_average(), 3.69, "The correct earned run average was not fetched")
        self.assertNotEqual(fake.fetch_pitcher_earned_run_average(), 3.69, "Invalid was not null")
'''

if __name__ == '__main__':
    unittest.main()
