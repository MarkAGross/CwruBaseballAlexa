import unittest

class GetterTester(unittest.TestCase):

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















if __name__ == '__main__':
    unittest.main()

