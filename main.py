from time import sleep


from src.scraper import Scraper
from src.notifier import Notifier
from src.logger import Logger


def main():
    scraper = Scraper('trackers/TRACKER_PRODUCTS.csv')
    logger = Logger()
    while scraper.interval <= scraper.interval_count:
        for x, url in enumerate(scraper.product_info.urls):
            price = scraper.get_price(url)
            if price and price < scraper.product_info.buy_below[x]:
                notifier = Notifier()
                message = f'{scraper.product_info.name[x]} が {price} で販売されています'
                notifier.send_line_notify(message)
            logger.save_log(scraper.product_info.name[x], url, scraper.title,
             scraper.product_info.buy_below, price)
        
        sleep(3)
        print(f'インターバル{scraper.interval}終了')
        print(f'次に実行されるのは{scraper.interval_hours}時間後です')
        scraper.interval += 1
        sleep(scraper.interval_hours*60*60)

   
if __name__ == "__main__":
    main()
