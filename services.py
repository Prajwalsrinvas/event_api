from typing import Dict
import json as _json
from fastapi import HTTPException
import datetime as _dt


def get_all_events() -> Dict:
    with open('events.json', encoding='UTF-8') as events_file:
        data = _json.load(events_file)

    return data


def get_events_of_month(month) -> Dict:
    month = month.lower()
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        raise HTTPException(status_code=404, detail="Wrong month!")


def get_events_of_day(month: str, day: int) -> Dict:
    month = month.lower()
    day = str(day)
    events = get_all_events()
    try:
        month_events = events[month][day]
        return month_events
    except KeyError:
        if not events.get(month):
            raise HTTPException(status_code=404, detail="Wrong month!")
        elif not events[month].get(day):
            raise HTTPException(status_code=404, detail="Wrong day!")
        else:
            raise HTTPException(
                status_code=404, detail=" Something went wrong!")


def get_events_of_today() -> Dict:
    today = _dt.date.today()
    month = today.strftime("%B").lower()
    day = today.day
    return [{'current_day': day, 'current_month': month, 'current_year': today.year}]+get_events_of_day(month, day)
