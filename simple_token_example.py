#
# Simple token example using hashlib.sha256
#

from hashlib import sha256

SECRET_KEY_FOR_SERVER = "@YW7dkusx$wFTfLSRkERC}\A5X{;K2PA"
CLIENT_TOKEN = "1067bad8e6aad40de02ee53ba915e89c16c696d947212b364f665028576151da.8801799999999"


def main():
    MOBILE_NUMBER = CLIENT_TOKEN.split('.')[1]
    SERVER_SECRET_PLUS_MOBILE_NUMBER = SECRET_KEY_FOR_SERVER + MOBILE_NUMBER

    server_token = sha256(SERVER_SECRET_PLUS_MOBILE_NUMBER.encode('utf-8')).hexdigest() + "." + MOBILE_NUMBER
    if server_token == CLIENT_TOKEN:
        print("VALID TOKEN")
    else:
        print("INVALID TOKEN")


if __name__ == "__main__":
    main()
