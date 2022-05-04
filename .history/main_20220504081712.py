from Utils.Scraper import Scraper



def main():
    scraper = Scraper('trackers/TRACKER_PRODUCTS.csv')
    scraper.get_price()


   
if __name__ == "__main__":
    main()
