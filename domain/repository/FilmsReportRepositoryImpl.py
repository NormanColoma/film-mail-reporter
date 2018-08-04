from domain.repository.IFilmsReportRepository import IFilmsReportRepository
from google.cloud import storage
import datetime


class FilmsReportRepositoryImpl(IFilmsReportRepository):
    def retrieve_report(self, report_name):
        storage_client = storage.Client()

        bucket_name = 'film-reports'
        bucket = storage_client.get_bucket(bucket_name)
        blob = storage.Blob(report_name, bucket)
        file_report_name = 'films-' + datetime.date.today().strftime("%d-%m-%Y") + '.pdf'

        blob.download_to_filename(file_report_name)

        return file_report_name
