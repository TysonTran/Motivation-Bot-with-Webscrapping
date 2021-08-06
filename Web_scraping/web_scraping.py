import requests
import bs4
import pandas as pd

def get_links(start, end, base_link):
    lst_links =[]
    for i in range(start, end+1):
        if i == 1:
            lst_links.append(base_link)
        else:
            lst_links.append(base_link + '_' + str(i))
    return lst_links

def get_quotes(links):
    quotes = []
    authors = []
    for i in links:
        r = requests.get(i)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        quote = [x.text.strip() for x in soup.find('div', attrs={'id':'qbc1'}).find_all('a', attrs={'title':'view quote'}) if x.text.strip()]
        quotes = quotes + quote
        author =[x.text for x in soup.find('div', attrs={'id':'qbc1'}).find_all('a', attrs={'title':'view author'})]
        authors = authors + author
    pd.DataFrame({'quotes':quotes, 'authors':authors}).to_csv('motivation.csv', index=False)
    return None

get_quotes(get_links(1,8, 'https://www.brainyquote.com/topics/inspirational-quotes'))