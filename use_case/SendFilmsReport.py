from domain.repository.IFilmsReportRepository import IFilmsReportRepository
from domain.service.mail.IMailSender import IMailSender
from config import config


class SendFilmsReport:
    def __init__(self, films_report_repository: IFilmsReportRepository, mail_service: IMailSender):
        self.films_report_repository: IFilmsReportRepository = films_report_repository
        self.mail_service: IMailSender = mail_service

    def execute(self, report_name: str):
        films_report: str = self.films_report_repository.retrieve_report(report_name)

        self.mail_service.connect(config.EMAIL_CREDENTIALS['account'], config.EMAIL_CREDENTIALS['password'])
        self.mail_service.send(config.EMAIL_CREDENTIALS['account'], config.EMAIL_CREDENTIALS['to'], films_report)
