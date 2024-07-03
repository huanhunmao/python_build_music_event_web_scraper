import requests
import selectorlib
from datetime import datetime
import os
import sqlite3

URL = 'http://programmer100.pythonanywhere.com/'

connection = sqlite3.connect('data1.db')
cursor = connection.cursor()

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
    cursor = connection.cursor()
    cursor.execute('INSERT INTO temperatures VALUES(?,?)',(now,data))
    connection.commit()


if __name__ == '__main__':
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store_data(extracted)