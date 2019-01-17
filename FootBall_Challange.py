
'''
Hackajob Football Session Challange
input : key of football team ( arsenal , manutd , everton etc )
output : total gaol in whole session
data : English Premier League 2014/15

'''
import json
import urllib.request
import pandas as pd

teamKey = input()

class football_challange:
    
    def __new__(self, teamKey):
        match1=[]
        x=0
        y=0
        # open link and read json 
        with urllib.request.urlopen("https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json") as url:
            data = json.loads(url.read().decode())
            data = data['rounds']
        #json parsing
            while x < len(data) :
                match = data[x]
                y = 0
                while y < len(match['matches']):            
                    match1.append((match['matches'][y]['team1'] ['key'],
                                    match['matches'][y]['score1']))
                    match1.append((match['matches'][y]['team2'] ['key'],
                                    match['matches'][y]['score2']))
                    y +=1
                x += 1
        # DataFream creation and calculation
            df = pd.DataFrame(match1, columns=['Team','Score'])
            goals = df[df.Team == teamKey].Score.sum()
        return goals
#run    
p1=football_challange(teamKey)
print(p1)