#
# Example of retrieving json data from the internet
#

from urllib.request import urlopen
import json


def extract_result(data):
    json_data = json.loads(data)

    total_entity_count = json_data['count']
    print(str(total_entity_count) + " record found")

    if total_entity_count >= 1 and "entries" in json_data:
        for entity in json_data['entries'][:10]:
            print(entity['API'])


def main():
    rest_api_url = "https://api.publicapis.org/entries"
    response = urlopen(rest_api_url)
    if response.getcode() == 200:
        data = response.read()
        extract_result(data)
    else:
        print("getting error during calling the rest api: " + str(response.getcode()))


if __name__ == '__main__':
    main()
