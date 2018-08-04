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
        email = MIMEMultipart('alternative')
        email['Subject'] = "Daily Films Report"
        email['From'] = from_user
        email['To'] = to_user

        email_text = 'Hey there, this is the report of today!!'
        file_path = os.path.dirname(os.path.realpath('__file__')) + '/' + file_to_send

        self.__attach_plain_text(email_text, email)
        self.__attach_file(file_to_send, file_path, email)
        self.server.sendmail(from_user, to_user, email.as_string())
        os.remove(file_path)

    def __attach_file(self, file_name, file_path, email):
        report = MIMEBase('application', "octet-stream")
        report.set_payload(open(file_path, "rb").read())
        encoders.encode_base64(report)
        report.add_header('Content-Disposition', 'attachment; filename="' + file_name + '"')

        email.attach(report)

    def __attach_plain_text(self, text, email):
        email_text = MIMEText(text, 'plain')

        email.attach(email_text)
