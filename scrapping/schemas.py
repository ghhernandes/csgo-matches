from pydantic import BaseModel

class Team(BaseModel):
    name: str

class MatchInfo(BaseModel):
    time: str
    meta: str
    rating: str | None

class MatchEvent(BaseModel):
    name: str        

class Match(BaseModel):
    url: str | None
    teams: list[Team]
    event: MatchEvent
    info: MatchInfo
