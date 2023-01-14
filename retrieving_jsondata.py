#
# Example of retrieving json data from the internet
#
from urllib.request import urlopen
import certifi


def main():
    rest_api_url = "https://api.publicapis.org/entries"
    response = urlopen(rest_api_url, cafile=certifi.where())
    print(response.getcode())


if __name__ == '__main__':
    main()