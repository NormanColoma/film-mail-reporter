from domain.repository.IFilmsReportRepository import IFilmsReportRepository
from google.cloud import storage
from config import config

import datetime


class FilmsReportRepositoryImpl(IFilmsReportRepository):
    def retrieve_report(self, report_name: str) -> str:
        storage_client: storage.Client = storage.Client()

        bucket: storage.Bucket = storage_client.get_bucket(config.GOOGLE_CLOUD_STORAGE['bucket'])
        blob: storage.Blob = storage.Blob(report_name, bucket)
        file_report_name: str = 'films-' + datetime.date.today().strftime("%d-%m-%Y") + '.pdf'

        blob.download_to_filename(file_report_name)

        return file_report_name
