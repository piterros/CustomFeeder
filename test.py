import feedparser
from bs4 import BeautifulSoup
import requests
import webbrowser

my_url = 'https://www.ppe.pl/rss.html'
feeds = feedparser.parse(my_url)
latest_feeds = []
html_content = '.maintxt.news-body'
html_id = '#content'

for news_number in range(0,4):

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
        print('ID: ', news['ID'], '\n', 'Title: ', news['Title'], '\n', 'Short info: ', news['Short description'], '\n\n')
    
    readmore = input('Choose ID to read more: ')
    if readmore == 'exit':
        break
    chosen_readmore = requests.get(latest_feeds[int(readmore)]['Link'])

    soup = BeautifulSoup(chosen_readmore.content, 'html.parser')

    classfind = soup.select(html_content)


    with open(r'C:\Users\Piter\Documents\Python\news_feeder\news.html', 'w+') as news_file:
        news_file.write(str(classfind))
    news_file.close()

    webbrowser.open_new_tab(r'C:\Users\Piter\Documents\Python\news_feeder\news.html')