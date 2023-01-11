#
# SendSMS Abstract Class for others sms providers
#

from abc import ABC, abstractmethod


class SendSMS(ABC):
    @abstractmethod
    def send_sms(self):
        pass
