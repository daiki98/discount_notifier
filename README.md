# Discount notifier
This app send you a notification by LINE if the product you want is discounted.

# Usage
Clone this repository to your computer
```
git clone git@github.com:daiki98/discount_notifier.git
```

Create directory named `trackers` then put `TRACKER_PRODUCTS.csv` like below.

| url | code | buy_below|
|-----|------|----------|
|https://...| Name of a product| price you want to get notification|
|...|...|...|


Your directory should be like this
```
main.py
README.md
Utild
    |__ Notifier.py
    |__ Scraper.py
trackers
    |__ TRACKER_PRODUCTS.csv
scraping
    |__ ...
```
In csv file, url column contains url of the product you want to check the price. name contains the name of the product. It doesn't matter what kind of name is in Code col. Buy_below contains the price you want to get a notification.

Activate venv
```
source scraping/bin/activate
```

Run main.py
```
python main.py
```


