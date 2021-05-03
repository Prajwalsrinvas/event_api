# Events API

An API created using FastAPI to provide us information on important events that have occurred on a given day, month or throughout the year.

## endpoints

- [/](https://events-fastapi.herokuapp.com/) : acts as homepage
- [/events](https://events-fastapi.herokuapp.com/events) : returns all events information 
- [/events/today](https://events-fastapi.herokuapp.com/events/today) : returns events that occurred on current month and day
- [/events/{month}](https://events-fastapi.herokuapp.com/events/november) : returns events that occurred on particular month, ex: /months/november
- [/events/{month}/{day}](https://events-fastapi.herokuapp.com/events/november/6) : returns events that occurred on particular day and month, ex: /events/november/6
- [/docs](https://events-fastapi.herokuapp.com/docs) : API documentation automatically created by FastAPI using [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [/redoc](https://events-fastapi.herokuapp.com/redoc): API documentation automatically created by FastAPI using [redoc](https://github.com/Redocly/redoc)

## Screenshots

### Homepage

![home](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/1.home.png)

### Documentation

![docs](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/2.docs.png)

### All events

![all events](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/3.events.png)

### Events that occurred on today's date

![today events](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/4.events_today.png)

### Events that occurred on a particular month

![monthly events](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/5.events_november.png)

### Events that occurred on a particular day of the month

![daily events](https://github.com/Prajwalsrinvas/event_api/blob/main/screenshots/6.events_november_6.png)


## file descriptions

### [collect_events.py](https://github.com/Prajwalsrinvas/event_api/blob/main/collect_events.py)

- Used to scrape [this site](https://www.onthisday.com/) using requests and BeautifulSoup modules, for all events information.
- Uses functions defined in [scraper.py](https://github.com/Prajwalsrinvas/event_api/blob/main/scraper.py)
- Events information stored as events.json, which is used as source of data by the API

### [main.py](https://github.com/Prajwalsrinvas/event_api/blob/main/main.py)

- Serves events information as an API using FastAPI
- Uses functions defined in [services.py](https://github.com/Prajwalsrinvas/event_api/blob/main/services.py)

## How to run it?

- python3 collect_events.py
  - creates events.json 
  - events.json file included for convenience
- uvicorn main:app --reload
  - deploys API on localhost using uvicorn server


## References:

- [FastAPI and Web Scraping in Python - Part 1: Project Setup and Scraping](https://www.youtube.com/watch?v=Nni0HX9O4hc)
- [FastAPI and Web Scraping in Python - Part 2: FastAPI](https://www.youtube.com/watch?v=hOipXax0Ogw)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
