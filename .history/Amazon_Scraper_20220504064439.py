import enum
import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep


# https://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

class Scraper:
    def __init__(self, path_to_csv):
        """スクレイピングに関連する関数を集めたクラスです

        Args:
            path_to_csv (string): url情報を含んだcsvファイルへのパス
        """
        self.urls = path_to_csv
        
    def get_price(self, interval_count=1, interval_hours = 6):
        """csvファイル内のurlから商品の価格を取得します

        Returns:
            float: 商品の価格
        """

        # CSVファイルをインポートし、URLを取得
        prod_tracker = pd.read_csv(self.urls, encoding='unicode-escape')
        prod_tracker_URLS = prod_tracker.url
        tracker_log = pd.DataFrame()
        now = datetime.now().strftime('%Y-%m-%d %H%Mm')
        interval = 0

        while interval < interval_count:
            for x, url in enumerate(prod_tracker_URLS):
                # URLをフェッチ
                page = requests.get(url, headers=HEADERS)

                # URL内の全ての情報を含むオブジェクトを生成
                soup = BeautifulSoup(page.content, features='lxml')
                # 商品名
                title = soup.find(id='productTitle').get_text().strip()

                # 商品の価格が取得できなかった場合のクラッシュを防ぐ
                try:
                    price = float(soup.find(id='price').get_text().replace('¥', '').replace(',', '').strip())
                except:
                    # ドルで取得
                    try:
                        price = float(soup.find(id='newBuyBoxPrice').get_text().replace('$', '').replace(',', '').strip())
                    except:
                        print('Failed to get price')
                        price = ''
                log = pd.DataFrame({'date': now.replace('h', ':').replace('m', ''),
                'code': prod_tracker.code[x],
                'url': url,
                'title': title,
                'buy_below': prod_tracker.buy_below[x],
                'price': price}, index=[x])
                print(log)

                # 価格が閾値より低いか確認
                try:
                    if price < prod_tracker.buy_below[x]:
                        print('===========Send notification===============')
                except:
                    pass
                tracker_log = pd.concat([tracker_log ,log], copy=True)
                print(f'{title}のログを追加\n\n')
                print(tracker_log)
                sleep(5)

            interval += 1

        return price

                

        # # URLをフェッチ
        # page = requests.get(prod_tracker_URLS[0], headers=HEADERS)

        # # URL内の全ての情報を含むオブジェクトを生成
        # soup = BeautifulSoup(page.content, 'lxml')


           

scraper = Scraper('trackers/TRACKER_PRODUCTS.csv')
print(scraper.get_price())