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
# HEADERS = ({'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
# 'Accept-Language': 'en-US, en;q=0.5'})

HEADERS = {
'authority': 'www.amazon.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape', sep='\t')
prod_tracker_URLS = prod_tracker.url

# 抽出したい要素をyamlファイルから読み込む
extractor = Extractor.from_yaml_file('trackers/selectors.yml')
# print(extractor.extract())

# URLをフェッチ
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)



# URL内の全ての情報を含むオブジェクトを生成
soup = BeautifulSoup(page.content, 'lxml')

# 商品名
title = soup.find(id='productTitle').get_text().strip()
price = soup.find(id='#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > div > div > div > div > div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.s-list-col-right > div > div > div.sg-row > div.sg-col.sg-col-4-of-12.sg-col-4-of-16.sg-col-4-of-20 > div > div.a-section.a-spacing-none.a-spacing-top-small.s-price-instructions-style > div:nth-child(2) > a > span:nth-child(1) > span:nth-child(2) > span.a-price-whole')
print(price)

# 商品の価格が取得できなかった場合のクラッシュを防ぐ
# try:
# price = soup.find(id='priceblock_ourprice').get_text().strip()
# print(page.content)
# print(price)
# except:
#     print('Failed to get price')
#     price = ''
