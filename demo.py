from team import team
from team_participant import team_participant
from schedule import schedule

t = team(2018)
tp = team_participant(2018)
s = schedule(2018)

print ('Team batting average is ' + t.fetch_batting_average())
print ('ERA for number 33 is ' + tp.fetch_pitcher_earned_run_average(33))
print ('Game on March 10th 2018 is ' )
print (s.fetch_games_by_date('March', 10))
