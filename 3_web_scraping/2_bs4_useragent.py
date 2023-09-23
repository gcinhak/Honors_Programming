import requests
from bs4 import BeautifulSoup

url ="https://www.danawa.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.text) # 모든 내용 출력
# print(soup.get_text()) # 모든 내용 출력
# print(soup.string) # 모든 내용 출력
# print(soup.title.get_text()) # tag의 text 리턴
# print(soup.find("title"))
# print(soup.title.text) # tag의 text 리턴
# print(soup.title.string) # 빈 값으로 출력
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.string) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력
# print(soup.find("li", {"id":"shoppingClipContent_1"}).find("a").string)
# print(soup.find("a", "link_title main-info-thumb-text__link")["href"]) # class="link_title main-info-thumb-text__link" 인 a element 를 찾아줘
# print(soup.find("a", {"class":"link_nav", "href":"http://auto.danawa.com/?logger_kw=dnw_gnb_auto"})) # 조건 2개
# print(soup.find(class_="link_title main-info-thumb-text__link")) # class_="link_title main-info-thumb-text__link" 인 어떤 element 를 찾아줘
# print(soup.find(attrs={"class":"link_title main-info-thumb-text__link"})) # class="link_title main-info-thumb-text__link" 인 어떤 element 를 찾아줘






# print(soup.find_all("li", "main-clip__item"))
menu1 = soup.find("li", "main-clip__item")
# print(menu1)
# print(menu1.a.get_text())
# print(menu1.a.text)
print(menu1.next_sibling.a.text)
# menu2 = menu1.next_sibling
# print(menu2.a.get_text())
# menu3 = menu2.next_sibling.next_sibling
# print(menu3.a.get_text())
# menu2 = menu3.previous_sibling.previous_sibling
# print(menu2.a.get_text())
# print(menu1.parent)
# print(menu1.children)
# menu2 = menu1.find_next_sibling("li")
# print(menu2.a.get_text())
# menu3 = menu2.find_next_sibling("li")
# print(menu3.a.get_text())
# menu2 = menu3.find_previous_sibling("li")
# print(menu2.a.get_text())
#
# print(menu1.find_next_siblings("li"))

clip1 = soup.find("a", string="조립PC 구매가이드!")
clip2 = soup.find("span", attrs={"class":"prod-list__txt"})
clip3 = soup.find("span", "prod-list__txt")
print(clip1)
print(clip2)
print(clip3)