import time

import requests
import selectorlib
from send_email import send_email
import time
import sqlite3

URL = 'http://programmer100.pythonanywhere.com/tours/'

class Event:
    def scrape(self,url):
        response = requests.get(url)
        source = response.text
        return source


    def extract(self,source):
        # 从 extract.yaml 文件中创建 Extractor 对象
        extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')

        # 使用 Extractor 对象从 source 中提取数据
        extracted_data = extractor.extract(source)

        # 返回提取到的 tours 数据
        value = extracted_data.get('tours')

        return value

class Database:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)

    # 存事件
    def store(self, extracted):
        row = extracted.split(',')
        row = [item.strip() for item in row]
        cursor =  self.connection.cursor()
        print('row',row)
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()


    # 读存储的事件
    def read_store_data(self,extracted):
        row = extracted.split(',')
        row = [item.strip() for item in row]
        band, city, date = row
        cursor =  self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == '__main__':
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != 'No upcoming tours':
            database = Database(dbname='data.db')
            row = database.read_store_data(extracted)
            # 有事件 and 不重复，才会存数据，发邮件
            if  not row:
                database.store(extracted)
                send_email(extracted)
        time.sleep(2)