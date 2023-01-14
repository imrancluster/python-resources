#
# Example of retrieving json data from the internet
#

from urllib.request import urlopen
import json


class Entity:
    def __init__(self, api: str, description: str, link: str, category: str):
        self._api = api
        self._description = description
        self._link = link
        self._category = category

    def __str__(self):
        return "Entity({0}-{1})".format(self._api, self._category)


def exract_result_by_oop(data):
    json_data = json.loads(data)
    entity_list = []

    if "entries" in json_data:
        for entity in json_data['entries'][:10]:
            entity = Entity(
                entity['API'],
                entity['Description'],
                entity['Link'],
                entity['Category'],
            )
            entity_list.append(entity)

    for entity in entity_list:
        print(entity)


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
        # extract_result(data)
        exract_result_by_oop(data)
    else:
        print("getting error during calling the rest api: " + str(response.getcode()))


if __name__ == '__main__':
    main()
