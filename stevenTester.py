import unittest



class getterTester(unittest.TestCase):

	valid = team(2018)
	invalid = team(2000)

	def test_sacrifice_flies(self):
		self.assertEquals(valid.fetch_num_of_sacrifice_flies(),27,"The correct number of sacrifice flies was not fetched")
		self.assertNotEquals(invalid.fetch_num_of_sacrifice_flies(), 27,"")
