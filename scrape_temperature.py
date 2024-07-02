import requests
import selectorlib
from datetime import datetime
import os

URL = 'http://programmer100.pythonanywhere.com/'

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract1.yaml')
    extracted_data = extractor.extract(source)
    value = extracted_data.get('tours')
    return value


def store_data(data):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    file_path = 'date_temperature.txt'
    file_exists = os.path.exists(file_path)
    with open('date_temperature.txt', 'a') as file:
        # 不存在表头才添加，存在不重复添加
        if not file_exists or os.stat(file_path).st_size == 0:
            file.write('Date,Temperature' + '\n')
        line = f'{now},{data}\n'
        file.write(line)


if __name__ == '__main__':
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store_data(extracted)