from datetime import datetime
from csvreport import monthly_output_csv,one_week_output_csv,two_weeks_output_csv

today = datetime.today().strftime('%d_%m_%Y')

def process_data(result, id):
    # print(result)
    for each_entry in result['data']:
        data = [ {
                "Hostname": each_entry['hostname'],
                "Total Hits": each_entry['edgeHitsSum'],
                "Cache Hit": each_entry['edgeHitsSum'] - each_entry['originHitsSum'],
                "Cache Miss": each_entry['originHitsSum'],
                "Cache Hit Ratio": round(each_entry['offloadedHitsPercentage'], 2),
                "Cache Miss Ratio": round(100 - each_entry['offloadedHitsPercentage'], 2),
                "Akamai Bandwidth": each_entry['edgeBytesSum'] + each_entry['midgressBytesSum'],
                "Origin Bandwidth": each_entry['originBytesSum']
            }
        ]
        
        if id == "weekly":
            one_week_output_csv(data, today)
        elif id == "monthly":
            monthly_output_csv(data, today)
        else:
            two_weeks_output_csv(data, today)