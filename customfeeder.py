import feedparser
from bs4 import BeautifulSoup
import requests
import webbrowser
from configparser import ConfigParser

cp = ConfigParser()
cp.read(r'C:\Users\Piter\Documents\Python\news_feeder\settings.config')

urls = []
latest_feeds = []
i = 1


for x in cp.sections():
    print(i, cp.get(x, 'my_url'))
    urls.append(
        {
            "id": i,
            "url": cp.get(x, 'my_url'),
            'html_content': cp.get(x, 'html_content'),
            'number_of_news': cp.get(x, 'number_of_news')
        }
    )
    i += 1

my_url = input('Choose URL ID: ')

feeds = feedparser.parse(urls[int(my_url)-1]['url'])


for news_number in range(0,int(urls[int(my_url)-1]['number_of_news'])):

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
    classfind = soup.select(urls[int(my_url)-1]['html_content'])

    with open(r'news.html', 'w+', encoding='utf-8') as news_file:
        news_file.write(str(classfind))
    news_file.close()

    webbrowser.open_new_tab(r'news.html')