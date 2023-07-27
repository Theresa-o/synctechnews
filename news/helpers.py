import requests
from .models import NewsItem
import time

def fetch_cronjob_news_items():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    response = requests.get(url)
    news_list = response.json()[:100]

    # Get the last synced item_id from the database
    last_synced_item_id = NewsItem.objects.order_by('-item_id').values_list('item_id', flat=True).first()

    # Find the index of the last synced item in the news_list
    if last_synced_item_id:
        try:
            last_synced_index = news_list.index(last_synced_item_id)
            news_list = news_list[last_synced_index + 1:]  
        except ValueError:
            pass

    # Process information about each submission and save to the database
    for item_id in news_list:
        url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        response = requests.get(url)
        response_dict = response.json()

        news_item = NewsItem(
            by=response_dict.get('by'),
            item_id=response_dict.get('id'),
            time=response_dict.get('time'),
            title=response_dict.get('title'),
            score=response_dict.get('score'),
            item_type=response_dict.get('type'),
            url=response_dict.get('url'),
        )
        news_item.save()
    time.sleep(60)
 