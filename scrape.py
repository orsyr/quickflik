import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)

    hn.append({'title': title, 'link': href})
  return hn

print(create_custom_hn(links, subtext))
  