This program has two parts.  The REST API is run with server.py.  Data updates are fetched by fetcher.py.  You can either run fetcher as a cron job, or you can run updater.py, which is a Python task scheduler that will call fetcher.py at regular intervals.

Run init.py to create the database and put in some starting data.

After running init.py, you can run server.py to use the APIs and view the swagger page and try them out with initial data. The REST API runs at http://0.0.0.0:5000/api/ui by default. The REST API offers two APIs: one to fetch all weather entries, and one to fetch weather entries from a city. By default (see settings.py), the cities are:
- Montreal
- Quebec
- Sherbrooke

Call fetcher.py directly to go fetch new data from the external source.  You may schedule this with a cron job, or run updater.py to do so.  By default, setting.py sets the updater's refresh interval to 1 minute for demonstration purposes.

The external data source is weather data collected from https://openweathermap.org/.
