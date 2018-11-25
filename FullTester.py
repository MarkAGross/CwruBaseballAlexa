import unittest
from error import CONNECTION_TO_WEBSITE_ERROR
from team import team
from team_participant import team_participant
from schedule import schedule
from schedule import game
from response import response
import datetime

class TestTeam(unittest.TestCase):

    print ("Testing team")
    valid_2018_team = team(2018)

    def text_no_specified_year(self):
        self.assertEqual(team(None).year, datetime.datetime.now().year, "The current year was not used when no year specified")

    def test_invalid_team_year(self):
        with self.assertRaises(CONNECTION_TO_WEBSITE_ERROR): team(9999)

    def test_valid_team_year(self):
        self.assertEqual(team(2015).year, 2015, "The correct year was fetched")

    def test_fetch_num_of_games(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_games(), "39", "The correct number of games was not fetched")

    def test_fetch_num_of_at_bats(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_at_bats(), "1376", "The correct number of at bats was not fetched")

    def test_fetch_num_of_runs(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_runs(), "271", "The correct number of runs was not fetched")

    def test_fetch_num_of_hits(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_hits(), "402", "The correct number of hits was not fetched")

    def test_fetch_num_of_doubles(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_doubles(), "91", "The correct number of doubles was not fetched")

    def test_fetch_num_of_triples(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_triples(), "10", "The correct number of triples was not fetched")

    def test_fetch_num_of_home_runs(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_home_runs(), "23", "The correct number of home runs was not fetched")

    def test_fetch_num_of_runs_batted_in(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_runs_batted_in(), "234", "The correct number of RBIs was not fetched")

    def test_fetch_num_of_extra_base_hits(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_extra_base_hits(), "124", "The correct number of extra base hits was not fetched")

    def test_fetch_num_of_total_bases(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_total_bases(), "582", "The correct number of total bases was not fetched")

    def test_fetch_num_of_walks(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_walks(), "135", "The correct number of walks was not fetched")

    def test_fetch_num_of_hit_by_pitches(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_hit_by_pitches(), "60", "The correct number of hit by pitches was not fetched")

    def test_fetch_num_of_strikeouts(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_strikeouts(), "250", "The correct number of strikeouts was not fetched")

    #tests getter for number of sac flies
    def test_fetch_num_of_sacrifice_flies(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_sacrifice_flies(),"27","The correct number of sacrifice flies was not fetched")

    #tests getter for number of sac hits
    def test_fetch_num_of_sacrifice_hits(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_sacrifice_hits(), "12", "The correct number of sacrifice hits was not fetched")

    #tests getter for number of hits into a double play
    def test_fetch_num_of_hits_into_double_play(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_hit_into_double_play(), "22", "The correct number of hits into double play was not fetched")

    #tests getter for number of stolen bases
    def test_fetch_num_of_stolen_bases(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_stolen_bases(), "93", "The correct number of stolen bases was not fetched")

    #tests getter for number of times caught stealing
    def test_fetch_num_of_caught_stealing(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_caught_stealing(), "14", "The correct number of times caught stealing was not fetched")

    #tests getter for batting average
    def test_fetch_num_of_batting_average(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_batting_average(), ".292", "The correct batting average was not fetched")

    #tests getter for on base percentage
    def test_fetch_on_base_percentage(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_on_base_percentage(), ".374", "The correct on base percetage was not fetched")

    #tests getter for slugging percentage
    def test_fetch_slugging_percentage(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_slugging_percentage(), ".423", "The correct slugging percentage was not fetched")

    #tests getter for earned run average (ERA)
    def test_fetch_earned_run_average(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_earned_run_average(), "3.64", "The correct earned run average was not fetched")

    #tests getter for shutuouts
    def test_fetch_num_of__shutouts(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_shutouts(), "3", "The correct number of shutouts was not fetched")

    #tests getter for number of at bats againsts
    def test_fetch_num_of_at_bats_against(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_num_of_at_bats_against(), "1309", "The correct number of at bats against was not fetched")

    #tests getter for batting average against
    def test_fetch_batting_average_against(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_batting_average_against(), ".248", "The correct batting average against was not fetched")

    #tests getter for home attendance
    def test_fetch_home_attendance(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_home_attendance(), "3045", "The correct number for home attendance was not fetched")

    #tests getter for home attendance average
    def test_fetch_home_attendance_average(self):
        self.assertEqual(self.__class__.valid_2018_team.fetch_home_attendance_average(), "203", "The correct number for home attendance average was not fetched")

class TestTeamParticipant(unittest.TestCase):
    print ("Testing team_participant")
    valid_2018_team_participant = team_participant(2018)
    player_2018_jacob_lott = {
        'No.' : '1', 'Name' : 'Jacob Lott', 'Pos.' : 'IF', 'B/T' : 'R/R', 'Ht.' : '5-10', 'Wt.' : '165', 'Yr.' : 'Fr.', 'Hometown/High School' : 'Pickerington, Ohio / Pickerington Central',
        'G' : '39', 'AB' : '143', 'R' : '22', 'H' : '41', '2B' : '10', '3B' : '2', 'HR' : '2', 'RBI' : '23', 'BB' : '7', 'K' : '25', 'SB' : '5', 'CS' : '2', 'AVG' : '.287', 'OBP' : '.318', 'SLG' : '.427'
        }
    player_2018_mark_gross = {
        'No.' : '33', 'Name' : 'Mark Gross', 'Pos.' : 'RHP', 'B/T' : 'L/R', 'Ht.' : '6-3', 'Wt.' : '200', 'Yr.' : 'Jr.', 'Hometown/High School' : 'Butler, Pa. / Butler Area Senior',
        'APP' : '11', 'GS' : '10', 'W' : '6', 'L' : '4', 'SV' : '0', 'CG' : '0', 'IP' : '70.2', 'H' : '69', 'R' : '37', 'ER' : '29', 'BB' : '21', 'K' : '44', 'K/9' : '5.60', 'HR' : '1', 'ERA' : '3.69'
        }
    player_2018_scott_kutschke = {
        'No.' : '38', 'Name' : 'Scott Kutschke', 'Pos.' : 'LHP', 'B/T' : 'L/L', 'Ht.' : '6-5', 'Wt.' : '195', 'Yr.' : 'So.', 'Hometown/High School' : 'Morton Grove, Ill. / Notre Dame Prep',
        'APP' : '14', 'GS' : '0', 'W' : '4', 'L' : '1', 'SV' : '1', 'CG' : '0', 'IP' : '30.2', 'H' : '35', 'R' : '15', 'ER' : '11', 'BB' : '14', 'K' : '24', 'K/9' : '7.04', 'HR' : '2', 'ERA' : '3.23'
        }

    def test_no_specified_team_participant_year(self):
        self.assertEqual(team_participant(None).year, datetime.datetime.now().year, "The current year was not used when no year specified")

    def test_invalid_team_participant_year(self):
        with self.assertRaises(CONNECTION_TO_WEBSITE_ERROR): team_participant(9999)

    def test_valid_team_participant_year(self):
        tp = team_participant(2015)
        self.assertEqual(tp.year, 2015, "The correct year was fetched")

    def test_valid_team_fetch_invalid_player_num(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_name('9999'), None, "Invalid player number did not fetch a value of None")

    #tests fetching of player name
    def test_fetch_player_name(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_name('1'), self.__class__.player_2018_jacob_lott['Name'], "Name for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_name('33'), self.__class__.player_2018_mark_gross['Name'], "Name for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_name('38'), self.__class__.player_2018_scott_kutschke['Name'], "Name for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player position
    def test_fetch_player_position(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_position('1'), self.__class__.player_2018_jacob_lott['Pos.'], "Position for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_position('33'), self.__class__.player_2018_mark_gross['Pos.'], "Position for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_position('38'), self.__class__.player_2018_scott_kutschke['Pos.'], "Position for number  " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player bats and throws
    def test_fetch_player_bats_and_throws(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_bats_and_throws('1'), self.__class__.player_2018_jacob_lott['B/T'], "Bats and Throws for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_bats_and_throws('33'), self.__class__.player_2018_mark_gross['B/T'], "Bats and Throws for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_bats_and_throws('38'), self.__class__.player_2018_scott_kutschke['B/T'], "Bats and Throws for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player height
    def test_fetch_player_height(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_height('1'), self.__class__.player_2018_jacob_lott['Ht.'], "Height for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_height('33'), self.__class__.player_2018_mark_gross['Ht.'], "Height for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_height('38'), self.__class__.player_2018_scott_kutschke['Ht.'], "Height for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player weight
    def test_fetch_player_weight(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_weight('1'), self.__class__.player_2018_jacob_lott['Wt.'], "Weight for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_weight('33'), self.__class__.player_2018_mark_gross['Wt.'], "Weight for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_weight('38'), self.__class__.player_2018_scott_kutschke['Wt.'], "Weight for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player academic year
    def test_fetch_player_year(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_year('1'), self.__class__.player_2018_jacob_lott['Yr.'], "Academic year for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_year('33'), self.__class__.player_2018_mark_gross['Yr.'], "Academic year for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_year('38'), self.__class__.player_2018_scott_kutschke['Yr.'], "Academic year for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of player hometown and highschool
    def test_fetch_player_town_and_school(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_hometown_and_high_school('1'), self.__class__.player_2018_jacob_lott['Hometown/High School'], "Hometown and high school for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_hometown_and_high_school('33'), self.__class__.player_2018_mark_gross['Hometown/High School'], "Hometown and high school for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_player_hometown_and_high_school('38'), self.__class__.player_2018_scott_kutschke['Hometown/High School'], "Hometown and high school for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")


    #tests fetching of batter games played
    def test_fetch_batter_games_played(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_games_played('1'), self.__class__.player_2018_jacob_lott['G'], "Batter games played for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_games_played('33'), None, "Batter games played for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_games_played('38'), None, "Batter games played for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")


    #tests fetching of batter at bats
    def test_fetch_batter_num_of_at_bats(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_at_bats('1'), self.__class__.player_2018_jacob_lott['AB'], "Batter number of at bats for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_at_bats('33'), None, "Batter number of at bats for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_at_bats('38'), None, "Batter number of at bats for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter runs
    def test_fetch_batter_num_of_runs(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs('1'), self.__class__.player_2018_jacob_lott['R'], "Batter number of runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs('33'), None, "Batter number of runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs('38'), None, "Batter number of runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter hits
    def test_fetch_batter_num_of_hits(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_hits('1'), self.__class__.player_2018_jacob_lott['H'], "Batter number of runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_hits('33'), None, "Batter number of runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_hits('38'), None, "Batter number of runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter doubles
    def test_fetch_batter_num_of_doubles(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_doubles('1'), self.__class__.player_2018_jacob_lott['2B'], "Batter number of doubles for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_doubles('33'), None, "Batter number of doubles for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_doubles('38'), None, "Batter number of doubles for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter triples
    def test_fetch_batter_num_of_triples(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_triples('1'), self.__class__.player_2018_jacob_lott['3B'], "Batter number of triples for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_triples('33'), None, "Batter number of triples for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_triples('38'), None, "Batter number of triples for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter home runs
    def test_fetch_batter_num_of_home_runs(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_home_runs('1'), self.__class__.player_2018_jacob_lott['HR'], "Batter number of home runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_home_runs('33'), None, "Batter number of home runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_home_runs('38'), None, "Batter number of home runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter rbis
    def test_fetch_batter_num_of_runs_batted_in(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs_batted_in('1'), self.__class__.player_2018_jacob_lott['RBI'], "Batter number of RBIs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs_batted_in('33'), None, "Batter number of RBIs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs_batted_in('38'), None, "Batter number of RBIs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter walks
    def test_fetch_batter_num_of_walks(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_walks('1'), self.__class__.player_2018_jacob_lott['BB'], "Batter number of RBIs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs_batted_in('33'), None, "Batter number of RBIs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_runs_batted_in('38'), None, "Batter number of RBIs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter strikeouts
    def test_fetch_batter_num_of_strikeouts(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_strikeouts('1'), self.__class__.player_2018_jacob_lott['K'], "Batter number of strkeouts for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_strikeouts('33'), None, "Batter number of strikeouts for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_strikeouts('38'), None, "Batter number of strikeouts for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter stolen bases
    def test_fetch_batter_num_of_stolen_bases(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_stolen_bases('1'), self.__class__.player_2018_jacob_lott['SB'], "Batter number of stolen bases for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_stolen_bases('33'), None, "Batter number of stolen bases for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_num_of_stolen_bases('38'), None, "Batter number of stolen bases for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter batting average
    def test_fetch_batter_batting_average(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_batting_average('1'), self.__class__.player_2018_jacob_lott['AVG'], "Batter batting average for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_batting_average('33'), None, "Batter batting average for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_batting_average('38'), None, "Batter batting average for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter on base percentage
    def test_fetch_batter_on_base_percentage(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_on_base_percentage('1'), self.__class__.player_2018_jacob_lott['OBP'], "Batter on base percentage for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_on_base_percentage('33'), None, "Batter on base percentage for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_on_base_percentage('38'), None, "Batter on base percentage for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of batter slugging percentage
    def test_fetch_batter_slugging_percentage(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_slugging_percentage('1'), self.__class__.player_2018_jacob_lott['SLG'], "Batter slugging percentage for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_slugging_percentage('33'), None, "Batter slugging percentage for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_batter_slugging_percentage('38'), None, "Batter slugging percentage for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of pitcher game appearances
    def test_fetch_pitcher_num_of_appearances(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_appearances('1'), None, "Pitcher appearances for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_appearances('33'), self.__class__.player_2018_mark_gross['APP'], "Pitcher appearances for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_appearances('38'), self.__class__.player_2018_scott_kutschke['APP'], "Pitcher appearances for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher game starts
    def test_fetch_pitcher_num_of_game_starts(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_game_starts('1'), None, "Pitcher number of game starts for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_game_starts('33'), self.__class__.player_2018_mark_gross['GS'], "Pitcher number of game starts for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_game_starts('38'), self.__class__.player_2018_scott_kutschke['GS'], "Pitcher number of game starts for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher wins
    def test_fetch_pitcher_num_of_wins(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_wins('1'), None, "Pitcher number of wins for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_wins('33'), self.__class__.player_2018_mark_gross['W'], "Pitcher number of wins for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_wins('38'), self.__class__.player_2018_scott_kutschke['W'], "Pitcher number of wins for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher losses
    def test_fetch_pitcher_num_of_losses(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_losses('1'), None, "Pitcher number of losses for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_losses('33'), self.__class__.player_2018_mark_gross['L'], "Pitcher number of losses for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_losses('38'), self.__class__.player_2018_scott_kutschke['L'], "Pitcher number of losses for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher saves
    def test_fetch_pitcher_num_of_saves(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_saves('1'), None, "Pitcher number of saves for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_saves('33'), self.__class__.player_2018_mark_gross['SV'], "Pitcher number of saves for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_saves('38'), self.__class__.player_2018_scott_kutschke['SV'], "Pitcher number of saves for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher complete games thrown
    def test_fetch_pitcher_num_of_complete_games(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_complete_games('1'), None, "Pitcher number of complete games for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_complete_games('33'), self.__class__.player_2018_mark_gross['CG'], "Pitcher number of complete games for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_complete_games('38'), self.__class__.player_2018_scott_kutschke['CG'], "Pitcher number of complete games for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher innings pitched
    def test_fetch_pitcher_num_of_innings_pitched(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_innings_pitched('1'), None, "Pitcher number of innings pitched for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_innings_pitched('33'), self.__class__.player_2018_mark_gross['IP'], "Pitcher number of innings pitched for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_innings_pitched('38'), self.__class__.player_2018_scott_kutschke['IP'], "Pitcher number of innings pitched for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher hits given up
    def test_fetch_pitcher_num_of_hits(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_hits('1'), None, "Pitcher number of hits for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_hits('33'), self.__class__.player_2018_mark_gross['H'], "Pitcher number of hits for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_hits('38'), self.__class__.player_2018_scott_kutschke['H'], "Pitcher number of hits for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")


    #tests fetching of piitcher runs given up
    def test_get_num_of_runs(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_runs('1'), None, "Pitcher number of runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_runs('33'), self.__class__.player_2018_mark_gross['R'], "Pitcher number of runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_runs('38'), self.__class__.player_2018_scott_kutschke['R'], "Pitcher number of runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher earned runs given up
    def test_fetch_pitcher_num_of_earned_runs(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_earned_runs('1'), None, "Pitcher number of earned runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_earned_runs('33'), self.__class__.player_2018_mark_gross['ER'], "Pitcher number of earned runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_earned_runs('38'), self.__class__.player_2018_scott_kutschke['ER'], "Pitcher number of earned runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher walks given up
    def test_fetch_pitcher_num_of_walks(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_walks('1'), None, "Pitcher number of walks for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_walks('33'), self.__class__.player_2018_mark_gross['BB'], "Pitcher number of walks for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_walks('38'), self.__class__.player_2018_scott_kutschke['BB'], "Pitcher number of walks for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher strikouts thrown
    def test_fetch_pitcher_num_of_strikeouts(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_strikeouts('1'), None, "Pitcher number of stikeouts for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_strikeouts('33'), self.__class__.player_2018_mark_gross['K'], "Pitcher number of strikeouts for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_strikeouts('38'), self.__class__.player_2018_scott_kutschke['K'], "Pitcher number of strikeouts for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher average number of strikeouts thrown per nine innings
    def test_fetch_pitcher_strikeouts_per_nine_innings(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_strikeouts_per_nine_innings('1'), None, "Pitcher number of strikeouts per nine innings for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_strikeouts_per_nine_innings('33'), self.__class__.player_2018_mark_gross['K/9'], "Pitcher number of stikeouts per nine innings for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_strikeouts_per_nine_innings('38'), self.__class__.player_2018_scott_kutschke['K/9'], "Pitcher number of strikeouts per nine innings for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher number of home runs given up
    def test_fetch_pitcher_num_of_home_runs(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_home_runs('1'), None, "Pitcher number of home runs for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_home_runs('33'), self.__class__.player_2018_mark_gross['HR'], "Pitcher number of home runs for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_num_of_home_runs('38'), self.__class__.player_2018_scott_kutschke['HR'], "Pitcher number of home runs for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

    #tests fetching of piitcher earned run average
    def test_fetch_pitcher_earned_run_average(self):
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_earned_run_average('1'), None, "Pitcher earned run average for number " + self.__class__.player_2018_jacob_lott['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_earned_run_average('33'), self.__class__.player_2018_mark_gross['ERA'], "Pitcher earned run average for number " + self.__class__.player_2018_mark_gross['No.'] + " not correcctly fetched")
        self.assertEqual(self.__class__.valid_2018_team_participant.fetch_pitcher_earned_run_average('38'), self.__class__.player_2018_scott_kutschke['ERA'], "Pitcher earned run average for number " + self.__class__.player_2018_scott_kutschke['No.'] + " not correcctly fetched")

class TestSchedule(unittest.TestCase):
    print ("Testing schedule")
    valid_2018_schedule = schedule(2018)
    valid_2018_wooster_game = {'month' : 'April', 'day' : '25', 'day_of_week' : 'Wed.', 'verses_or_at' : 'vs', 'opponent_name' : '#2 Wooster', 'neutralsite' : None , 'result' : 'L, 11-6', 'status' : 'Final'}
    valid_2018_washington_and_jefferson_game = {'month' : 'March', 'day' : '4', 'day_of_week' : 'Sun.', 'verses_or_at' : 'at', 'opponent_name' : '#4 Washington & Jefferson', 'neutralsite' : None , 'result' : 'L, 8-2', 'status' : 'Final'}
    valid_2018_allegheny_game = {'month' : 'March', 'day' : '4', 'day_of_week' : 'Sun.', 'verses_or_at' : 'vs.', 'opponent_name' : 'Allegheny','neutralsite' : '@ Washington, Pa.' , 'result' : 'W, 4-3', 'status' : 'Final'}


    def test_no_specified_scheudle_year(self):
        self.assertEqual(schedule(None).year, datetime.datetime.now().year, "The currrent year not used when no year speecified")

    def test_invalid_schedule_year(self):
        with self.assertRaises(CONNECTION_TO_WEBSITE_ERROR): schedule(9999)

    def test_valid_schedule_year(self):
        self.assertEqual(team(2015).year, 2015, "The correct year was fetched")

    def test_fetch_games_by_date_no_games(self):
        games_for_day = self.__class__.valid_2018_schedule.fetch_games_by_date("March", "2")
        self.assertEqual(games_for_day, None, "Incorrectly fetched games for date that no games occured")

    def test_fetch_games_by_date_invalid_month(self):
        games_for_day = self.__class__.valid_2018_schedule.fetch_games_by_date("blahblahblah", "2")
        self.assertEqual(games_for_day, None, "Incorrectly fetched games for invalid month date")

    def test_fetch_games_by_date_invalid_day(self):
        games_for_day = self.__class__.valid_2018_schedule.fetch_games_by_date("March", "blah")
        self.assertEqual(games_for_day, None, "Incorrectly fetched games for invalid day date")

    def test_fetch_games_by_date_single_game(self):
        games_for_day = self.__class__.valid_2018_schedule.fetch_games_by_date('April', '25')
        self.assertEqual(len(games_for_day), 1, "Fetched incorrect number of games for date")
        game = games_for_day[0]
        self.assertEqual(game.month,  self.__class__.valid_2018_wooster_game['month'], "Fetched game month incorrectly")
        self.assertEqual(game.day, self.__class__.valid_2018_wooster_game['day'], "Fetched game day incorrectly")
        self.assertEqual(game.day_of_week, self.__class__.valid_2018_wooster_game['day_of_week'], "Fetched game day of week incorrectly")
        self.assertEqual(game.verses_or_at,  self.__class__.valid_2018_wooster_game['verses_or_at'], "Fetched game vs or at incorrectly")
        self.assertEqual(game.opponent_name, self.__class__.valid_2018_wooster_game['opponent_name'], "Fetched game opponent name incorrectly")
        self.assertEqual(game.neutral_site, self.__class__.valid_2018_wooster_game['neutralsite'], "Fetched game neutral site incorrectly")
        self.assertEqual(game.result,  self.__class__.valid_2018_wooster_game['result'], "Fetched game result incorrectly")
        self.assertEqual(game.status, self.__class__.valid_2018_wooster_game['status'], "Fetched game status incorrectly")

    def test_fetch_games_by_date_multiple_games(self):
        games_for_day = self.__class__.valid_2018_schedule.fetch_games_by_date('March', '4')
        self.assertEqual(len(games_for_day), 2, "Fetched incorrect number of games for date")
        game_one = games_for_day[0]
        game_two = games_for_day[1]
        self.assertEqual(game_one.month,  self.__class__.valid_2018_washington_and_jefferson_game['month'], "Fetched game month incorrectly")
        self.assertEqual(game_one.day, self.__class__.valid_2018_washington_and_jefferson_game['day'], "Fetched game day incorrectly")
        self.assertEqual(game_one.day_of_week, self.__class__.valid_2018_washington_and_jefferson_game['day_of_week'], "Fetched game day of week incorrectly")
        self.assertEqual(game_one.verses_or_at,  self.__class__.valid_2018_washington_and_jefferson_game['verses_or_at'], "Fetched game vs or at incorrectly")
        self.assertEqual(game_one.opponent_name, self.__class__.valid_2018_washington_and_jefferson_game['opponent_name'], "Fetched game opponent name incorrectly")
        self.assertEqual(game_one.neutral_site, self.__class__.valid_2018_washington_and_jefferson_game['neutralsite'], "Fetched game neutral site incorrectly")
        self.assertEqual(game_one.result,  self.__class__.valid_2018_washington_and_jefferson_game['result'], "Fetched game result incorrectly")
        self.assertEqual(game_one.status, self.__class__.valid_2018_washington_and_jefferson_game['status'], "Fetched game status incorrectly")

        self.assertEqual(game_two.month,  self.__class__.valid_2018_allegheny_game['month'], "Fetched game month incorrectly")
        self.assertEqual(game_two.day, self.__class__.valid_2018_allegheny_game['day'], "Fetched game day incorrectly")
        self.assertEqual(game_two.day_of_week, self.__class__.valid_2018_allegheny_game['day_of_week'], "Fetched game day of week incorrectly")
        self.assertEqual(game_two.verses_or_at,  self.__class__.valid_2018_allegheny_game['verses_or_at'], "Fetched game vs or at incorrectly")
        self.assertEqual(game_two.opponent_name, self.__class__.valid_2018_allegheny_game['opponent_name'], "Fetched game opponent name incorrectly")
        self.assertEqual(game_two.neutral_site, self.__class__.valid_2018_allegheny_game['neutralsite'], "Fetched game neutral site incorrectly")
        self.assertEqual(game_two.result,  self.__class__.valid_2018_allegheny_game['result'], "Fetched game result incorrectly")
        self.assertEqual(game_two.status, self.__class__.valid_2018_allegheny_game['status'], "Fetched game status incorrectly")


class TestResponse(unittest.TestCase):
    print("Testing responses ")
  

    def test_valid_team_stat_response(self):
        validTeamStat = [None] * 28
        validTeamStat[2] = "15"
        validTeamStat[26] = "2018"
        resp = response()
        self.assertEqual(resp.teamResponse(validTeamStat), 'The CWRU Baseball team has 15 Runs in 2018')


    def test_valid_participant_stat_response(self):
        validPlayerStat = [None] * 33
        validPlayerStat[7] = 39
        validPlayerStat[31] = 29
        validPlayerStat[32] = "2018"
        resp = response()
        self.assertEqual(resp.participantResponse(validPlayerStat), 'Player No.29 has 39 Games played in 2018')


    def test_valid_schedule_response(self):
        data = []
        gameObj = game(data)
        gameObj.month = "April"
        gameObj.day = 25
        gameObj.opponent_name = "#2 Wooster"
        gameObj.result = "L, 11-6"
        validSchedule = [None] * 3
        validSchedule[1] = gameObj
        validSchedule[2] = "2018"
        resp = response()

        #print(validSchedule)
        self.assertEqual(resp.scheduleResponse(validSchedule), 'CWRU baseball team played #2 Wooster on the 25 of April, and the result was L, 11-6.')

if __name__ == '__main__':
    unittest.main()
