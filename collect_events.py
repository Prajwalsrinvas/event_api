import datetime as _dt
from typing import Iterator, Dict
import scraper as _scraper
import json


def _date_range(start_date: _dt, end_date: _dt) -> Iterator[_dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)


def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        day = date.day
        if month not in events:
            events[month] = dict()
        print(f"Getting details of events that ocurred on {month} {day}")
        events[month][date.day] = _scraper.events_of_the_day(month, day)
    print("All events details collected!")
    return events


if __name__ == "__main__":
    events = create_events_dict()
    with open('events.json', 'w', encoding='UTF-8') as events_file:
        json.dump(events, events_file, ensure_ascii=False)
    print("events details stored as events.json!")
