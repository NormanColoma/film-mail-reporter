import smtplib
import os

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from domain.service.mail.IMailSender import IMailSender


class MailSenderImpl(IMailSender):
    def __init__(self, host, port):
        self.server = smtplib.SMTP_SSL(host, port)

    def connect(self, user, password):
        try:
            self.server.ehlo()
            self.server.login(user, password)
        except Exception as error:
            print(error)

    def send(self, from_user, to_user, file_to_send):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Daily Films Report"
        msg['From'] = from_user
        msg['To'] = to_user

        body = MIMEText('Hey there, this is the report of day!!', 'plain')
        report = MIMEBase('application', "octet-stream")
        file_path = os.path.dirname(os.path.realpath('__file__')) + '/' + file_to_send
        report.set_payload(open(file_path, "rb").read())
        encoders.encode_base64(report)
        report.add_header('Content-Disposition', 'attachment; filename="' + file_to_send + '"')

        msg.attach(body)
        msg.attach(report)
        self.server.sendmail(from_user, to_user, msg.as_string())
        os.remove(file_path)