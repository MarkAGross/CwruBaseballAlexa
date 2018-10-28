import unittest

class GetterTester(unittest.TestCase):

    valid = team(2018)
    invalid = team(2000)

    def test_get_games(self):
        assertEquals(valid.fetch_num_of_games(), 39, "The correct number of games was not fetched")
        assertNotEquals(invalid.fetch_num_of_games(), 39, "")


if __name__ == '__main__':
    unittest.main()

