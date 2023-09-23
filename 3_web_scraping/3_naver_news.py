import requests
from bs4 import BeautifulSoup

key = input()
url ="https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}".format(key)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

myurls = soup.find_all('a', attrs={'class':'news_tit'})

for myurl in myurls:
    print(myurl.attrs['title'])
    print(myurl.attrs['href'])