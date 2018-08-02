from MailSender import MailSender
from config import config


class MailSenderApplication:
    def run(self):
        mail_sender = MailSender(config.EMAIL_SERVER['host'], config.EMAIL_SERVER['port'])
        mail_sender.connect(config.EMAIL_CREDENTIALS['account'], config.EMAIL_CREDENTIALS['password'])
        mail_sender.send('normancolomagar@gmail.com', 'ua.norman@gmail.com')


if __name__ == '__main__':
    app = MailSenderApplication()
    app.run()
