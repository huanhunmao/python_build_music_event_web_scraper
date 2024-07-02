import requests
import selectorlib
from send_email import send_email

URL = 'http://programmer100.pythonanywhere.com/tours/'


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    # 从 extract.yaml 文件中创建 Extractor 对象
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')

    # 使用 Extractor 对象从 source 中提取数据
    extracted_data = extractor.extract(source)

    # 返回提取到的 tours 数据
    value = extracted_data.get('tours')

    return value

# 存事件
def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n')


# 读存储的事件
def read_store_data():
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read_store_data()
    if extracted != 'No upcoming tours':
        # 有事件 and 不重复，才会存数据，发邮件
        if extracted not in content:
            store(extracted)
            send_email(extracted)