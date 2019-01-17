## ESPN Sports API Class

This project is a Python library for ESPN's hidden Sports API. This class makes it easy to get scores and information 
about ongoing, past and upcoming games, teams, stats, players, etc.

### Dependencies

1. Python `requests` library

### Usage

Usage is very simple.

- Import the class.

    `import espn_scoreboard`

- Create an instance of the ESPNScoreboard class. The constructor takes 2 parameters. The first is the sport name and 
the second is the league name.

    `scoreboard = espn_scoreboard.ESPNScoreboard("basketball", "mens-college-basketball")`
    
    The following is a list of sports and leagues that are supported by the API:
   
   ``` 
    Sport           Leagues
    -----           -------
    football        college-football, nfl
    basketball      nba, wnba, womens-college-basketball, mens-college-basketball
    baseball        mlb
    hockey          nhl
    soccer          eng.1, usa.1
    ```
    
- Call the `get_scoreboard` function to get the scoreboard for a specific date. The parameter for the function is a date 
in the form `YYYYMMDD`, or a Python datetime object.

    `scores = scoreboard.get_scoreboard('20190116')`
    
### More Information

For more information about what the API actually returns, and a brief description of each item, refer to: 
https://gist.github.com/quantum0813/6aa87103b46e84ef8ab29b2bb66905d6