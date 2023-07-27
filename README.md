
# SyncTechNews

SyncTechNews is a super-clean read-only Hacker News app built for fast scannable reading and has features that enable you to scan for what you care most about to improve your reading experience.

The technology stack includes Python (Django, Django Rest Framework), HTML, and CSS.



## Installation

To run this project on your local machine, please follow the following steps:

- Clone this repository git clone https://github.com/Theresa-o/synctechnews.git

- cd into hackernews

- Install the requirements py running pip install -r requirements.txt

- Run the server using python -m manage.py runserver 
    
## Accomplishment

- Implements a scheduled job to sync published news to a database every 5 minutes.
- Implements a view to list the latest news.
- Allows filtering by the type of news item.
- Implements a search box for text-based filtering.
- Uses pagination for displaying a large number of news items.
- Exposes an API with endpoints to list and add news items.
- Allows updating and deleting items created through the API but not data retrieved from Hacker News.

Overall, the project aims to create a web app that makes it easier to navigate through tech-related news from Hacker News. It achieves this by syncing and displaying the latest news, allowing filtering and searching, implementing pagination, and providing an API for data consumption. Additionally, the project includes some bonus features like displaying children items and enabling updates and deletions through the API.


