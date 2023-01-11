#
# BanglaLink SMS Provider
#
from smsprovider.SendSMS import SendSMS


class BanglaLinkProvider(SendSMS):
    def send_sms(self):
        return "Send SMS from BanglaLink provider."
