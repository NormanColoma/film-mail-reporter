from listener.FilmsReportListener import FilmsReportListener


class MailSenderApplication:
    def run(self):
        FilmsReportListener.listen()


if __name__ == '__main__':
    app = MailSenderApplication()
    app.run()
