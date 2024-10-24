# import datetime
import os, csv

# today = datetime.today().strftime('%d_%m_%Y')

def one_week_output_csv(data, today):
    file_name = f'one_week_report_{today}.csv'
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=[
                "Hostname",
                "Total Hits",
                "Cache Hit",
                "Cache Miss",
                "Cache Hit Ratio",
                "Cache Miss Ratio",
                "Akamai Bandwidth",
                "Origin Bandwidth"]
            )

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

def two_weeks_output_csv(data, today):
    file_name = f'two_weeks_report_{today}.csv'
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=[
                "Hostname",
                "Total Hits",
                "Cache Hit",
                "Cache Miss",
                "Cache Hit Ratio",
                "Cache Miss Ratio",
                "Akamai Bandwidth",
                "Origin Bandwidth"]
            )

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

def monthly_output_csv(data, today):
    file_name = f'monthly_report_{today}.csv'
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=[
                "Hostname",
                "Total Hits",
                "Cache Hit",
                "Cache Miss",
                "Cache Hit Ratio",
                "Cache Miss Ratio",
                "Akamai Bandwidth",
                "Origin Bandwidth"]
            )

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)