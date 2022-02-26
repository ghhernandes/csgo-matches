from fastapi import APIRouter

from ..schemas import match
from ...scrapping.matches import MatchService
#from ... import db

router = APIRouter(
    prefix='/matches',
    tags=['matches']
)

@router.get('/live')
async def live_matches():
    match_service = MatchService("https://www.hltv.org/matches/")
    live_matches = match_service.get_live_matches()
    return live_matches