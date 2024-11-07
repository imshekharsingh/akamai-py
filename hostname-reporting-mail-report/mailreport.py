from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def mailreport(sender,receiver,subject,body,files):

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    # message['Cc'] = cc_email
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))

    for each_file in files:
        file_name = Path(each_file).name
        with open(each_file, 'rb') as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename = {file_name}")
        message.attach(part)

    text = message.as_string()

    with smtplib.SMTP('mail.example.com', 25) as server:
        server.ehlo()
        # server.starttls()
        # server.ehlo()
        # server.login(sender, 'Cdrwf%#re23')
        text = message.as_string()
        server.sendmail(sender, receiver, text)

def mail_report():
    today = datetime.today().strftime('%d_%m_%Y')

    sender = 'john.doe@example.com'
    receiver = 'john.doe@example.com'
    # cc_email = 'john.doe@example.com'
    subject = 'Hostname - Traffic Reports'
    body = (f"Hi,\n"
            f"Please find attached hostname reports.\n"
            f"Regards.")
    files = [f'./one_week_report_{today}.csv',
             f'./two_weeks_report_{today}.csv',
             f'./monthly_report_{today}.csv']

    mailreport(sender,receiver,subject,body,files)