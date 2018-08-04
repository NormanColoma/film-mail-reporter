from abc import ABC, abstractmethod


class IMailSender(ABC):
    @abstractmethod
    def connect(self, user: str, password: str):
        raise NotImplementedError

    @abstractmethod
    def send(self, from_user: str, to_user: str, file_to_send: str):
        raise NotImplementedError
