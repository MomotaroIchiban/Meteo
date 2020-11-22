Run test.py to run automated tests.

This program has two parts.  The REST API is run with server.py.  Dataupdates are fetched by fetcher.py.  You can either run fetcher as a cron job, or you can run updater.py, which is a Python task scheduler that will call fetcher.py at regular intervals.

The REST API runs at http://0.0.0.0:5000/api/ui by default.

