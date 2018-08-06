import pika

from config import config
from config import rabbitmq_config
from domain.repository.FilmsReportRepositoryImpl import FilmsReportRepositoryImpl
from domain.repository.IFilmsReportRepository import IFilmsReportRepository
from domain.service.mail.IMailSender import IMailSender
from domain.service.mail.MailSenderImpl import MailSenderImpl
from use_case.SendFilmsReport import SendFilmsReport


class FilmsReportListener:
    @staticmethod
    def callback(ch, method, properties, body: bytes):
        report_name: str = body.decode()
        print("Event received: %r" % report_name)

        mail_service: IMailSender = MailSenderImpl(config.EMAIL_SERVER['host'], config.EMAIL_SERVER['port'])
        films_report_repository: IFilmsReportRepository = FilmsReportRepositoryImpl()
        send_films_report: SendFilmsReport = SendFilmsReport(films_report_repository, mail_service)
        send_films_report.execute(report_name)

    @staticmethod
    def listen():
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_config.HOST))
        channel = connection.channel()
        channel.queue_declare(queue=rabbitmq_config.QUEUE)
        channel.basic_consume(FilmsReportListener.callback, queue=rabbitmq_config.QUEUE, no_ack=True)
        channel.start_consuming()
