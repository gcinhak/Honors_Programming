import requests
from bs4 import BeautifulSoup

url ="https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%89%B4%EC%8A%A4"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb api_get"})

for idx, image in enumerate(images, 1):
    image_url = image["data-lazysrc"]
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie_{}.jpg".format(idx), "wb") as f:
        f.write(image_res.content)