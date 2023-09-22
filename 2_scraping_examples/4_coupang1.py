import re
import requests
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?q=노트북&channel=user&sorter=scoreDesc&listSize=36&isPriceRange=false&rating=0&page=1&rocketAll=false"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 ", "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(len(items))

for item in items:
    # 요소에 리턴
    name = item.find("div", attrs={"class":"name"}) # 제품명
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    # 가격
    # 리뷰수

    # 제품명 출력
    print(name.text.strip())

    # 평점 출력
    if rate:
        print("평점: ", rate.text)
    else:
        print("  <평점 없는 상품 제외합니다>")

    # 가격 출력

    # 리뷰수 출력
    print("=" * 100)