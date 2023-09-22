import requests

# url = "https://google.com"
url = "https://www.danawa.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers) # Response 객체 리턴
# res = requests.get(url)
res.raise_for_status() # 정상 확인 비정상이면 에러 발생
print(res.text) # 내용 출력

# 파일에 저장
with open("danawa_test.html", "w", encoding="utf8") as f:
    f.write(res.text)