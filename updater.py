import schedule
import time

from fetcher import job
from settings import REFRESH_MIN

schedule.every(REFRESH_MIN).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
