# CS:GO Matches

Extract upcoming and live CS:GO official matches from (<https://www.hltv.org/matches>).

```python
from scrapping import matches, schemas

match_service = matches.MatchService("https://www.hltv.org/matches/") 

print('Live CS:GO matches')
for match in match_service.get_live_matches():
    print(match)

print('\nUpcoming CS:GO matches')
for match in match_service.get_upcoming_matches():
    print(match)

```

## Result

```text
Live CS:GO matches
url='/matches/2354397/heroic-vs-virtuspro-iem-katowice-2022' teams=[Team(name='Heroic'), Team(name='Virtus.pro')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='LIVE', meta='bo3', rating='3')
url='/matches/2354396/gambit-vs-nip-iem-katowice-2022' teams=[Team(name='Gambit'), Team(name='NIP')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='LIVE', meta='bo3', rating='3')
url='/matches/2354430/fate-vs-skade-a1-gaming-league-season-5' teams=[Team(name='FATE'), Team(name='SKADE')] event=MatchEvent(name='A1 Gaming League Season 5') info=MatchInfo(time='LIVE', meta='bo5', rating='0')

Upcoming CS:GO matches
url='/matches/2354398/astralis-vs-g2-iem-katowice-2022' teams=[Team(name='Astralis'), Team(name='G2')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='19:30', meta='bo3', rating='2')
url='/matches/2354399/natus-vincere-vs-faze-iem-katowice-2022' teams=[Team(name='Natus Vincere'), Team(name='FaZe')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='19:30', meta='bo3', rating='3')
url='/matches/2354501/teamone-vs-atk-mythic-winter-series-2022-cup-2' teams=[Team(name='TeamOne'), Team(name='ATK')] event=MatchEvent(name='Mythic Winter Series 2022 Cup 2') info=MatchInfo(time='22:00', meta='bo3', rating='0')
url='/matches/2354502/party-astronauts-vs-third-impact-mythic-winter-series-2022-cup-2' teams=[Team(name='Party Astronauts'), Team(name='Third Impact')] event=MatchEvent(name='Mythic Winter Series 2022 Cup 2') info=MatchInfo(time='22:00', meta='bo3', rating='0')        
url='/matches/2354095/ecstatic-vs-1shot-esl-challenger-league-season-40-europe' teams=[Team(name='ECSTATIC'), Team(name='1shot')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating='1')
url='/matches/2354096/gamerlegion-vs-wisla-krakow-esl-challenger-league-season-40-europe' teams=[Team(name='GamerLegion'), Team(name='Wisla Krakow')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating='0')    
url='/matches/2354097/skade-vs-saw-esl-challenger-league-season-40-europe' teams=[Team(name='SKADE'), Team(name='SAW')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating='0')
url='/matches/2354098/sinners-vs-finest-esl-challenger-league-season-40-europe' teams=[Team(name='SINNERS'), Team(name='Finest')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating='0')
url='/matches/2354447/x13-vs-chococheck-esl-challenger-league-season-40-north-america' teams=[Team(name='X13'), Team(name='ChocoCheck')] event=MatchEvent(name='ESL Challenger League Season 40 North America') info=MatchInfo(time='02:00', meta='bo3', rating='0')
```
