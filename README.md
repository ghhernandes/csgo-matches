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
id=0 url='' teams=[Team(name='G2'), Team(name='FURIA')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='LIVE', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='FATE'), Team(name='SKADE')] event=MatchEvent(name='A1 Gaming League Season 5') info=MatchInfo(time='LIVE', meta='bo5', rating=None)

Upcoming CS:GO matches
id=0 url='' teams=[Team(name='Heroic'), Team(name='Virtus.pro')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='16:20', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='Gambit'), Team(name='NIP')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='16:30', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='Natus Vincere'), Team(name='FaZe')] event=MatchEvent(name='IEM Katowice 2022') info=MatchInfo(time='19:30', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='TeamOne'), Team(name='ATK')] event=MatchEvent(name='Mythic Winter Series 2022 Cup 2') info=MatchInfo(time='22:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='Party Astronauts'), Team(name='Third Impact')] event=MatchEvent(name='Mythic Winter Series 2022 Cup 2') info=MatchInfo(time='22:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='ECSTATIC'), Team(name='1shot')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='GamerLegion'), Team(name='Wisla Krakow')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='SKADE'), Team(name='SAW')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='SINNERS'), Team(name='Finest')] event=MatchEvent(name='ESL Challenger League Season 40 Europe') info=MatchInfo(time='19:00', meta='bo3', rating=None)
id=0 url='' teams=[Team(name='X13'), Team(name='ChocoCheck')] event=MatchEvent(name='ESL Challenger League Season 40 North America') info=MatchInfo(time='02:00', meta='bo3', rating=None)
```
