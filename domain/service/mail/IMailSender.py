from abc import ABC, abstractmethod


class IMailSender(ABC):
    @abstractmethod
    def connect(self, user, password):
        raise NotImplementedError

    @abstractmethod
    def send(self, from_user, to_user, file_to_send):
        raise NotImplementedError
