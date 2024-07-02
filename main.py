import requests
import selectorlib

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


if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)