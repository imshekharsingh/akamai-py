# import requests
import json
from datetime import datetime, timedelta
from urllib.parse import urljoin
from processdata import process_data

today = datetime.today().strftime('%d_%m_%Y')
report_url = '/reporting-api/v2/reports/delivery/traffic/current/data'

data =   {
    "dimensions": [
      "hostname"
    ],
    "metrics": [
      "edgeHitsSum",
      "edgeBytesSum",
      "midgressBytesSum",
      "originHitsSum",
      "originBytesSum",
      "offloadedHitsPercentage",
      "offloadedBytesPercentage"
    ],
    "sortBys": [
      {
        "name": "edgeHitsSum",
        "sortOrder": "DESCENDING"
      }
    ]
  }

headers = {
    "Content-Type": "application/json"
}

def report_1_week(s,baseurl):
    query_param = 'timeRange=LAST_1_WEEK'
    result = s.post(urljoin(baseurl, f'{report_url}?{query_param}'), json=data, headers=headers)
    # print(result.status_code)
    # print(result)
    if result.status_code == 200:
        result_1_week = json.loads(result.text)
        process_data(result_1_week, id="weekly")
    else:
        None

def report_2_weeks(s,baseurl):
    # query_param = 'timeRange=LAST_1_WEEK'
    end_time = datetime.now()
    start_time = end_time - timedelta(days = 15)

    start = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    end = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    query_param = f'start={start}&end={end}'

    result = s.post(urljoin(baseurl, f'{report_url}?{query_param}'), json=data, headers=headers)
    # print(result.status_code)
    # print(result)
    if result.status_code == 200:
        result_1_week = json.loads(result.text)
        process_data(result_1_week, id="15_days")
    else:
        None

def report_30_days(s,baseurl):
    query_param = 'timeRange=LAST_30_DAYS'
    result = s.post(urljoin(baseurl, f'{report_url}?{query_param}'), json=data, headers=headers)
    # print(result.status_code)
    # print(result)
    if result.status_code == 200:
        result_30_days = json.loads(result.text)
        process_data(result_30_days, id="monthly")
    else:
        None