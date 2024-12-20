from akamauth import akamai_auth
from mailreport import mail_report
from reportrange import report_1_week,report_2_weeks,report_30_days

def main():
    s,baseurl = akamai_auth()
    report_1_week(s,baseurl)
    report_2_weeks(s,baseurl)
    report_30_days(s,baseurl)
    mail_report()

if __name__ == '__main__':
    main()