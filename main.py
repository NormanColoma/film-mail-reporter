from service.EventReceiver import EventReceiver


class MailSenderApplication:
    def run(self):
        EventReceiver.receive()


if __name__ == '__main__':
    app = MailSenderApplication()
    app.run()
