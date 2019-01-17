import espn_scoreboard

"""
This example gets a scoreboard for NCAA men's college basketball for January 3, 2019 and prints out the scores for each 
event that happened on that day.
"""

scoreboard = espn_scoreboard.ESPNScoreboard("basketball", "mens-college-basketball")
scores = scoreboard.get_scoreboard("20190103")

for event in scores["events"]:
    for competition in event.competitions:
        competitors = competition.competitors

        team1 = competitors[0]
        team2 = competitors[1]

        print(team1.team.display_name + ' ' + team1.score + ' ' + team2.team.display_name + ' ' + team2.score)