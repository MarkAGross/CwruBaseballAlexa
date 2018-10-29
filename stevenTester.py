import unittest



class getterTester(unittest.TestCase):

	valid = team(2018)
	invalid = team(2000)
	
	#tests getter for number of sac flies
	def test_get_sacrifice_flies(self):
		assertEquals(valid.fetch_num_of_sacrifice_flies(),27,"The correct number of sacrifice flies was not fetched")
		assertNotEquals(invalid.fetch_num_of_sacrifice_flies(), 27,"")

	#tests getter for number of sac hits
	def test_get_sacrifice_hits(self):
		assertEquals(valid.fetch_num_of_sacrifice_hits(), 12, "The correct number of sacrifice hits was not fetched")
		assertNotEquals(invalid.fetch_num_of_sacrifice_hits(), 12, "")

	#tests getter for number of hits into a double play
	def test_get_hits_into_double_play(self):
		assertEquals(valid.fetch_num_of_hit_into_double_play(), 22, "The correct number of hits into double play was not fetched")
		assertNotEquals(invalid.fetch_num_of_hit_into_double_play(), 22, "")

	#tests getter for number of stolen bases
	def test_get_stolen_bases(self):
		assertEquals(valid.fetch_num_of_stolen_bases(), 93, "The correct number of stolen bases was not fetched")
		assertNotEquals(invalid.fetch_num_of_stolen_bases(), 93, "")
	
	#tests getter for number of times caught stealing
	def test_get_caught_stealing(self):
		assertEquals(valid.fetch_num_of_caught_stealing(), 14, "The correct number of times caught stealing was not fetched")
		assertNotEquals(invalid.fetch_num_of_caught_stealing(), 14, "")
	
	#tests getter for batting average
	def test_get_batting_average(self):
		assertEquals(valid.fetch_batting_average(), .292, "The correct batting average was not fetched")
		assertNotEquals(invalid.fetch_batting_average(), .292, "")

	#tests getter for on base percentage
	def test_get_on_base_percentage(self):
		assertEquals(valid.fetch_on_base_percentage(), .374, "The correct on base percetage was not fetched")
		assertNotEquals(invalid.fetch_on_base_percentage(), .374, "")

	#tests getter for slugging percentage
	def test_get_slugging_percentage(self):
		assertEquals(valid.fetch_slugging_percentage(), .423, "The correct slugging percentage was not fetched")
		assertNotEquals(invalid.fetch_slugging_percentage(), .423, "")

	#tests getter for earned run average (ERA)
	def test_get_earned_run_average(self):
		assertEquals(valid.fetch_earned_run_average(), 3.64, "The correct earned run average was not fetched")
		assertNotEquals(invalid.fetch_earned_run_average(), 3.64, "")

	#tests getter for shutuouts
	def test_get_shutouts(self):
		assertEquals(valid.fetch_num_of_shutouts(), 3, "The correct number of shutouts was not fetched")
		assertNotEquals(invalid.fetch_num_of_shutouts(), 3, "")

	#tests getter for number of at bats againsts
	def test_get_at_bats_against(self):
		assertEquals(valid.fetch_num_of_at_bats_against(), 1309, "The correct number of at bats against was not fetched")
		assertNotEquals(invalid.fetch_num_of_at_bats_against(), 1309, "")

	#tests getter for batting average against
	def test_get_batting_average_against(self):
		assertEquals(valid.fetch_batting_average_against(), .248, "The correct batting average against was not fetched")
		assertNotEquals(invalid.fetch_batting_average_against(), .248, "")

	#tests getter for home attendance
	def test_get_home_attendance(self):
		assertEquals(valid.fetch_home_attendance(), 3045, "The correct number for home attendance was not fetched")
		assertNotEquals(invalid.fetch_home_attendance(), 3045, "")

	#tests getter for home attendance average
	def test_get_home_attendance_average(self):
		assertEquals(valid.fetch_home_attendance_average(), 203, "The correct number for home attendance average was not fetched")
		assertNotEquals(invalid.fetch_home_attendance_average(), 203, "")

	if __name__ == '__main__':
		unittest.main()