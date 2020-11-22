This program has two parts.  The REST API is run with server.py.  Data updates are fetched by fetcher.py.  You can either run fetcher as a cron job, or you can run updater.py, which is a Python task scheduler that will call fetcher.py at regular intervals.

Run init.py to create the database and put in some starting data. The REST API runs at http://0.0.0.0:5000/api/ui by default.

Weather data is collected from https://openweathermap.org/.  The REST API offers two APIs: one to fetch all weather entries, and one to fetch weather entries from a city.

By default, the cities are:
- Montreal
- Quebec
- Sherbrooke
