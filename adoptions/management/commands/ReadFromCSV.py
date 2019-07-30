from csv import DictReader
from datetime import datetime

from pytz import UTC

DATETIME_FORMAT = '%m/%d/%Y %H:%M'

for row in DictReader(open('./pet_data.csv')):
     raw_submission_date = row['submission date']
     submission_date = UTC.localize(
        datetime.strptime(raw_submission_date, DATETIME_FORMAT))
     print(submission_date)