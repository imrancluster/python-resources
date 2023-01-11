#
# GP SMS Provider
#
from smsprovider.SendSMS import SendSMS


class GPSMSProvider(SendSMS):
    def send_sms(self):
        return "Send SMS from GP provider."
