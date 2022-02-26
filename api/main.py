from fastapi import FastAPI
from .routes import matches

app = FastAPI()
app.include_router(matches.router)


@app.get('/')
async def root():
    return {'message': 'CSGO live and upcoming matches'}