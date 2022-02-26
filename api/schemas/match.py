from pydantic import BaseModel

from . import team

class MatchInfo(BaseModel):
    time: str
    meta: str
    rating: str | None

class MatchEvent(BaseModel):
    name: str        

class Match(BaseModel):
    url: str | None
    teams: list[team.Team]
    event: MatchEvent
    info: MatchInfo
