from fastapi import FastAPI
import services as _services

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the historical events API! Refer to /docs for more info!"}


@app.get("/events")
async def all_events():
    return _services.get_all_events()


@app.get("/events/today")
async def events_of_today():
    return _services.get_events_of_today()


@app.get("/events/{month}")
async def events_of_month(month: str):
    return _services.get_events_of_month(month)


@app.get("/events/{month}/{day}")
async def events_of_day(month: str, day: int):
    return _services.get_events_of_day(month, day)
