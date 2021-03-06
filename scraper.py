from typing import List
import requests as _requests
from bs4 import BeautifulSoup


# underscores at the start of the identifier would mean that we would not import these functions into another python script


def _generate_url(month: str, day: int) -> str:
    return f'https://www.onthisday.com/day/{month}/{day}'


def _get_page(url: str) -> BeautifulSoup:
    page = _requests.get(url)
    return BeautifulSoup(page.content, 'lxml')


def events_of_the_day(month: str, day: int) -> List[str]:
    """
    Returns the events of the day
    """
    url = _generate_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all('li', class_='event')
    return [event.text for event in raw_events]
