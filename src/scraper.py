import requests
import pandas as pd
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, path_to_csv, interval_count=1, interval_hours = 6):
        """スクレイピングに関連する関数を集めたクラスです

        Args:
            path_to_csv (str): url情報を含んだcsvファイルへのパス
            interval_count (int): インターバルの回数
            interval_hours (int): インターバルの間隔
        """
        # CSVファイルをインポート
        self.product_info = pd.read_csv(path_to_csv, encoding='unicode-escape')

        # https://www.networkinghowtos.com/howto/common-user-agent-list/
        self.HEADERS = ({'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})

        self.interval = 1
        self.interval_count = interval_count
        self.interval_hours = interval_hours
        self.is_sale = 0
        self.title = ''

    def get_price(self, url):
        """csvファイル内のurlから商品の価格を取得します

        Returns:
            float: 商品の価格
        """
        # URLをフェッチ
        page = requests.get(url, headers=self.HEADERS)
        # URL内の全ての情報を含むオブジェクトを生成
        soup = BeautifulSoup(page.content, features='lxml')
        # 商品名
        self.title = soup.find(id='productTitle').get_text().strip()
        # 商品の価格が取得できなかった場合をキャッチ
        if soup.find(id='price'):
            price = float(soup.find(id='price').get_text().replace('¥', '').replace(',', '').strip())
        else:
            print('Failed to get price')
            price = None
        
        return price
 