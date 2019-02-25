"""
    Football Season Challenge: code retrieves the total number of
    goal per queried team in a whole season.

    input : key of football team ( arsenal , manutd , everton etc )

    output : total number of goal in whole season

    data : English Premier League 2014/15

"""

import json
import urllib.request
import pandas as pd


class FootballChallenge:
    """
        access and read the data
        
        outputs:  the team codes

    """
    def __init__(self):
        df = pd.DataFrame()

    @classmethod
    def _prepare_data(cls):

        with urllib.request.urlopen(
                "https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json") as url:
            data = json.loads(url.read().decode())
            data = data['rounds']

        match1 = []
        x = 0
        while x < len(data):
            match = data[x]
            y = 0
            while y < len(match['matches']):
                match1.append((match['matches'][y]['team1']['key'],
                               match['matches'][y]['score1']))
                match1.append((match['matches'][y]['team2']['key'],
                               match['matches'][y]['score2']))
                y += 1
            x += 1

        cls.df = pd.DataFrame(match1, columns=['Team', 'Score'])
        team_key = cls.df.Team.unique()
        return cls.df, print(team_key)

    def __init__(self):
        self.df = FootballChallenge._prepare_data()

    """
        Retrieves the total goal count for queried team team code.
        
        input : team code (such as arsenal , manutd , everton)
        
        output : total number of goal for whole season.

    """

    def goal_calculate(self, team_input):

        df = pd.DataFrame(FootballChallenge.df)
        goals = df[df.Team == team_input].Score.sum()
        return goals


