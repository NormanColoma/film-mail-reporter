from abc import ABC, abstractmethod


class IFilmsReportRepository(ABC):
    @abstractmethod
    def retrieve_report(self, report_name):
        raise NotImplementedError
