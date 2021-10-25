import hashlib
import json

wiki_url = 'https://ru.wikipedia.org/wiki/'



class MyIterator:

    def __init__(self, path):
        with open('countries.json', 'r') as file:
            country_list = json.load(file)
            name = (country['name']['common'] for country in country_list)
            self.iter = iter(name)


    def url_country(self, country_name: str):
        country_name = country_name.replace(' ', '_')
        country_url = f'{wiki_url}{country_name}'
        return country_url

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.iter)
        result = f'{country_name} - {self.url_country(country_name)}'
        return result


def hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    with open('counties_link.txt', 'w') as country_names_file:
        for country_link in MyIterator('countries.json'):
            country_names_file.write(f'{country_link}\n')

    for hash_str in hash('counties_link.txt'):
        print(hash_str)
