import requests
from scrapy.selector import Selector

from ..api.schemas import match, team

class MatchService:
    def __init__(self, url: str) -> None:
        self.url = url
        self.content: Selector = None

    def _request_matches_content(self, reset: bool=False) -> Selector:
        if reset or not self.content:
            response = requests.get(self.url)
            self.content = Selector(text=response.content)
        return self.content

    def _get_match_teams(self, data: Selector) -> list[team.Team]:
        teams_div = data.css('div.matchTeam')
        result = []
        for team_div in teams_div:
            team_name = team_div.css('div.matchTeamName::text').get()
            result.append(team.Team(name=team_name))
        return result

    def _get_match_event(self, data: Selector) -> match.MatchEvent:
        event_name = data.css('div.matchEventName::text').get()
        return match.MatchEvent(
            name=event_name
        )

    def _get_match_info(self, data: Selector) -> match.MatchInfo:
        info = data.css('div.matchInfo')
        time = info.css('div.matchTime::text').get()
        meta = info.css('div.matchMeta::text').get()
        rating = data.attrib['stars']
        return match.MatchInfo(
            time=time,        
            meta=meta,
            rating=rating,
        )

    def _get_match(self, data: Selector) -> match.Match:
        return match.Match(
            url=data.css('a').attrib['href'],
            teams=self._get_match_teams(data),
            event=self._get_match_event(data),
            info=self._get_match_info(data)
        )

    def _check_match_empty(self, data: Selector) -> bool:
        empty = data.css('div.matchInfoEmpty')
        return len(empty) > 0    

    def get_upcoming_matches(self) -> list[match.Match]:
        matches = []
        self.content = self._request_matches_content()    
        upcoming_matches = self.content.css('div.upcomingMatch')
        for upcoming in upcoming_matches:
            if self._check_match_empty(upcoming):
                continue
            match = self._get_match(upcoming)
            matches.append(match)
        return matches

    def get_live_matches(self) -> list[match.Match]:
        matches = []
        self.content = self._request_matches_content()    
        live_matches = self.content.css('div.liveMatch-container')
        for live in live_matches:
            match = self._get_match(live)
            matches.append(match)
        return matches