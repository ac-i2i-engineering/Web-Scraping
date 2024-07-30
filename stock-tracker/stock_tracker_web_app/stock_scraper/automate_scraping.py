import schedule
import time
import subprocess
from config import SCHEDULE_TIME

def job():
    subprocess.run(['python', '../manage.py','scrape_data.py'])

# Schedule the job
schedule.every().day.at(SCHEDULE_TIME).do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
