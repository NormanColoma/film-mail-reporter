import pika
from MailSender import MailSender
from config import config


class EventReceiver:
    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        
        mail_sender = MailSender(config.EMAIL_SERVER['host'], config.EMAIL_SERVER['port'])
        mail_sender.connect(config.EMAIL_CREDENTIALS['account'], config.EMAIL_CREDENTIALS['password'])
        mail_sender.send('normancolomagar@gmail.com', 'ua.norman@gmail.com')

    @staticmethod
    def receive():
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='film-reporter')
        channel.basic_consume(EventReceiver.callback, queue='film-reporter',
                              no_ack=True)
        channel.start_consuming()
