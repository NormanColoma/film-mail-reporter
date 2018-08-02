import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender:
    def __init__(self, host, port):
        self.server = smtplib.SMTP_SSL(host, port)

    def connect(self, user, password):
        try:
            self.server.ehlo()
            self.server.login(user, password)
        except Exception as error:
            print(error)

    def send(self, from_user, to_user):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Daily Films Report"
        msg['From'] = from_user
        msg['To'] = to_user
        body = MIMEText('Hey there, this is the report of day!!', 'plain')

        msg.attach(body)
        self.server.sendmail(from_user, to_user, msg.as_string())

