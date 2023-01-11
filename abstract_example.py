#
# We will see abstract class example
#
from smsprovider import SendSMS, GPSMSProvider, BanglaLinkProvider


def main(sms: SendSMS):
    """
    main function to explore the abstract feature

    :param sms:
    :return: print result of send_sms()
    """
    print(sms.send_sms())


if __name__ == "__main__":
    """ Creating provider object using GPSMSProvider class 
        which has implemented the SendSMS abstract class
    """
    provider = GPSMSProvider()

    """ Now we are able to switch the sms provider from GP to BanglaLink very easily
        by creating a new object of BanglaLinkProvider class
    """
    # provider = BanglaLinkProvider()

    main(provider)
