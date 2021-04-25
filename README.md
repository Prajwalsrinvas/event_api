# Events API

An API created using FastAPI to provide us information on important events that have occurred on a given day, month or throughout the year.

## endpoints

- / : acts as homepage
- /events : returns all events information 
- /events/today : returns events that occurred on current month and day
- /events/{month} : returns events that occurred on particular month, ex: /months/november
- /events/{month}/{day} : returns events that occurred on particular day and month, ex: /events/november/6
- /docs : API documentation automatically created by FastAPI using [Swagger UI](https://swagger.io/tools/swagger-ui/)
- /redoc: API documentation automatically created by FastAPI using [redoc](https://github.com/Redocly/redoc)

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
