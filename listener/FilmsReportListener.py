import pika

from domain.repository.FilmsReportRepositoryImpl import FilmsReportRepositoryImpl
from domain.service.mail import MailSenderImpl

from config import config
from use_case.SendFilmsReport import SendFilmsReport


class FilmsReportListener:
    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

        mail_service = MailSenderImpl(config.EMAIL_SERVER['host'], config.EMAIL_SERVER['port'])
        films_report_repository = FilmsReportRepositoryImpl()
        send_films_report = SendFilmsReport(films_report_repository, mail_service)
        send_films_report.execute(body)

    @staticmethod
    def listen():
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='film-reporter')
        channel.basic_consume(FilmsReportListener.callback, queue='film-reporter',
                              no_ack=True)
        channel.start_consuming()
