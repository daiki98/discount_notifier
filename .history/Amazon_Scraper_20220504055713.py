import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
from selectorlib import Extractor
import json
import html


# https://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

# HEADERS = {
# 'authority': 'www.amazon.com',
# 'pragma': 'no-cache',
# 'cache-control': 'no-cache',
# 'dnt': '1',
# 'upgrade-insecure-requests': '1',
# 'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'sec-fetch-site': 'none',
# 'sec-fetch-mode': 'navigate',
# 'sec-fetch-dest': 'document',
# 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# }

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape')
prod_tracker_URLS = prod_tracker.url

# 抽出したい要素をyamlファイルから読み込む
# extractor = Extractor.from_yaml_file('trackers/selectors.yml')
# print(extractor.extract())

# URLをフェッチ
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)



# URL内の全ての情報を含むオブジェクトを生成
soup = BeautifulSoup(page.content, 'lxml')

# 商品名
title = soup.find(id='productTitle').get_text().strip()

# to prevent script from crashing when there isn't a price for the product
price = float(soup.find(id='price').get_text().replace('$', '').replace('￥', '').replace(',', '.').strip())
# decimal_point = price.index('.')
# price = price[:price.index('.')]
order = 1
# price = soup.select(f".widgetId\=search-results_{order}, .s-price-instructions-style, .a-price-whole")
# price = soup.find("span", {"class":"a-price"}, {"class": "a-price-whole"})
print(price)
# try:
#     price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
# except:
#     # this part gets the price in dollars from amazon.com store
#     try:
#         price = float(soup.find(id='priceblock_saleprice').get_text().replace('$', '').replace(',', '').strip())
#     except:
#         print('fail')
#         price = ''
# 商品の価格が取得できなかった場合のクラッシュを防ぐ
# try:
# price = soup.find(id='priceblock_ourprice').get_text().strip()
# print(page.content)
# print(price)
# except:
#     print('Failed to get price')
#     price = ''
