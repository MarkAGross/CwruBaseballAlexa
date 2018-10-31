import unittest

class GetterTeamTester(unittest.TestCase):

    valid = team(2018)
    invalid = team(2000)

    def test_get_games(self):
        assertEquals(valid.fetch_num_of_games(), 39, "The correct number of games was not fetched")
        assertNotEquals(invalid.fetch_num_of_games(), 39, "Invalid was not null")

    def test_get_at_bats(self):
        assertEquals(valid.fetch_num_of_at_bats(), 271, "The correct number of at bats was not fetched")
        assertNotEquals(invalid.fetch_num_of_at_bats(), 271, "Invalid was not null")

    def test_get_runs(self):
        assertEquals(valid.fetch_num_of_runs(), 23, "The correct number of runs was not fetched")
        assertNotEquals(invalid.fetch_num_of_runs(), 23, "Invalid was not null")

    def test_get_hits(self):
        assertEquals(valid.fetch_num_of_hits(), 402, "The correct number of hits was not fetched")
        assertNotEquals(invalid.fetch_num_of_hits(), 402, "Invalid was not null")

    def test_get_doubles(self):
        assertEquals(valid.fetch_num_of_doubles(), 91, "The correct number of doubles was not fetched")
        assertNotEquals(invalid.fetch_num_of_doubles(), 91, "Invalid was not null")

    def test_get_triples(self):
        assertEquals(valid.fetch_num_of_triples(), 10, "The correct number of triples was not fetched")
        assertNotEquals(invalid.fetch_num_of_triples(), 10, "Invalid was not null")

    def test_get_home_runs(self):
        assertEquals(valid.fetch_num_of_home_runs(), 23, "The correct number of home runs was not fetched")
        assertNotEquals(invalid.fetch_num_of_home_runs(), 23, "Invalid was not null")

    def test_get_rbis(self):
        assertEquals(valid.fetch_num_of_runs_batted_in(), 234, "The correct number of RBIs was not fetched")
        assertNotEquals(invalid.fetch_num_of_runs_batted_in(), 234, "Invalid was not null")

    def test_get_extra_base_hits(self):
        assertEquals(valid.fetch_num_of_extra_base_hits(), 124, "The correct number of extra base hits was not fetched")
        assertNotEquals(invalid.fetch_num_of_extra_base_hits(), 124, "Invalid was not null")

    def test_get_total_bases(self):
        assertEquals(valid.fetch_num_of_total_bases(), 582, "The correct number of total bases was not fetched")
        assertNotEquals(invalid.fetch_num_of_total_bases(), 582, "Invalid was not null")

    def test_get_walks(self):
        assertEquals(valid.fetch_num_of_walks(), 135, "The correct number of walks was not fetched")
        assertNotEquals(invalid.fetch_num_of_walks(), 135, "Invalid was not null")

    def test_get_hit_by_pitches(self):
        assertEquals(valid.fetch_num_of_hit_by_pitches(), 60, "The correct number of hit by pitches was not fetched")
        assertNotEquals(invalid.fetch_num_of_hit_by_pitches(), 60, "Invalid was not null")

    def test_get_strikeouts(self):
        assertEquals(valid.fetch_num_of_strikeouts(), 250, "The correct number of strikeouts was not fetched")
        assertNotEquals(invalid.fetch_num_of_strikeouts(), 250, "Invalid was not null")

class GetterParticipantTester(unittest.TestCase):

    batter = team_participant(11, 2018)
    mark = team_participant(33, 2018)
    fake = team_participant(100, 2000)

    def test_get_stolen_bases(self):
        assertEquals(batter.fetch_batter_num_of_stolen_bases(), 9, "The correct number of stolen bases was not fetched")
        assertNotEquals(fake.fetch_batter_num_of_stolen_bases(), 9, "Invalid was not null")

    def test_get_batting_average(self):
        assertEquals(batter.fetch_batter_batting_average(), .471, "The correct batting average was not fetched")
        assertNotEquals(fake.fetch_batter_batting_average(), .471, "Invalid was not null")

    def test_get_on_base_percentage(self):
        assertEquals(batter.fetch_batter_on_base_percentage(), .517, "The correct OBP was not fetched")
        assertNotEquals(fake.fetch_batter_on_base_percentage(), .517, "Invalid was not null")

    def test_get_slugging_percentage(self):
        assertEquals(batter.fetch_batter_slugging_percentage(), .673, "The correct slugging_percentage was not fetched")
        assertNotEquals(fake.fetch_batter_slugging_percentage(), .673, "Invalid was not null")

    def test_get_num_of_appearances(self):
        assertEquals(mark.fetch_pitcher_num_of_appearances(), 11, "The correct number of appearances was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_appearances(), 11, "Invalid was not null")

    def test_get_num_of_game_starts(self):
        assertEquals(mark.fetch_pitcher_num_of_game_starts(), 10, "The correct number of game starts was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_game_starts(), 10, "Invalid was not null")

    def test_get_num_of_wins(self):
        assertEquals(mark.fetch_pitcher_num_of_wins(), 6, "The correct number of wins was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_wins(), 6, "Invalid was not null")

    def test_get_num_of_losses(self):
        assertEquals(mark.fetch_pitcher_num_of_losses(), 4, "The correct number of losses was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_losses(), 4, "Invalid was not null")

    def test_get_num_of_saves(self):
        assertEquals(mark.fetch_pitcher_num_of_saves(), 0, "The correct number of saves was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_saves(), 0, "Invalid was not null")

    def test_get_num_of_complete_games(self):
        assertEquals(mark.fetch_pitcher_num_of_complete_games(), "-", "The correct number of complete games was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_complete_games(), "-", "Invalid was not null")

    def test_get_num_of_innings_pitched(self):
        assertEquals(mark.fetch_pitcher_num_of_innings_pitched(), 70.2, "The correct number of innings pitched was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_innings_pitched(), 70.2, "Invalid was not null")

    def test_get_num_of_hits(self):
        assertEquals(mark.fetch_pitcher_num_of_hits(), 69, "The correct number of hits was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_hits(), 69, "Invalid was not null")

    def test_get_num_of_runs(self):
        assertEquals(mark.fetch_pitcher_num_of_runs(), 37, "The correct number of runs was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_runs(), 37, "Invalid was not null")

    def test_get_num_of_earned_runs(self):
        assertEquals(mark.fetch_pitcher_num_of_earned_runs(), 29, "The correct number of earned_runs was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_earned_runs(), 29, "Invalid was not null")

    def test_get_num_of_walks(self):
        assertEquals(mark.fetch_pitcher_num_of_walks(), 21, "The correct number of walks was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_walks(), 21, "Invalid was not null")

    def test_get_num_of_strikeouts(self):
        assertEquals(mark.fetch_pitcher_num_of_strikeouts(), 44, "The correct number of strikeouts was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_strikeouts(), 44, "Invalid was not null")

    def test_get_strikeouts_per_nine_innings(self):
        assertEquals(mark.fetch_pitcher_strikeouts_per_nine_innings(), 5.60, "The correct number of strikeouts per nine innings was not fetched")
        assertNotEquals(fake.fetch_pitcher_strikeouts_per_nine_innings(), 5.60, "Invalid was not null")

    def test_get_num_of_home_runs(self):
        assertEquals(mark.fetch_pitcher_num_of_home_runs(), 1, "The correct number of home runs was not fetched")
        assertNotEquals(fake.fetch_pitcher_num_of_home_runs(), 1, "Invalid was not null")

    def test_get_earned_run_average(self):
        assertEquals(mark.fetch_pitcher_earned_run_average(), 3.69, "The correct earned run average was not fetched")
        assertNotEquals(fake.fetch_pitcher_earned_run_average(), 3.69, "Invalid was not null")



if __name__ == '__main__':
    unittest.main()

