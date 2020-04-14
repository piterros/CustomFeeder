import feedparser
from bs4 import BeautifulSoup
import requests
import webbrowser
from configparser import ConfigParser

cp = ConfigParser()
cp.read('settings.config')
my_url = cp.get('custom-feeder-config', 'my_url')
html_content = cp.get('custom-feeder-config', 'html_content')
number_of_news = cp.get('custom-feeder-config', 'number_of_news')

feeds = feedparser.parse(my_url)
latest_feeds = []

for news_number in range(0,int(number_of_news)):

    latest_feeds.append(
        {
    "ID": news_number,
    "Title": feeds.entries[news_number].title,
    "Short description": feeds.entries[news_number].description,
    "Link": feeds.entries[news_number].link
        }
    )

while True:
    for news in latest_feeds:
        print('ID: ', news['ID']+1, '\n', 'Title: ', news['Title'], '\n', 'Short info: ', news['Short description'], '\n\n')
    
    readmore = input('Choose ID to read more (or exit to quit): ')
    if readmore == 'exit':
        break

    chosen_readmore = requests.get(latest_feeds[int(readmore)-1]['Link'])
    soup = BeautifulSoup(chosen_readmore.content, 'html.parser')
    classfind = soup.select(html_content)

    with open(r'news.html', 'w+') as news_file:
        news_file.write(str(classfind))
    news_file.close()

    webbrowser.open_new_tab(r'news.html')