import requests
from bs4 import BeautifulSoup
import pandas as pd


def coupang_products(keyword, pages):
    baseurl = 'https://www.coupang.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

    products_link = []
    for page in range(1, pages + 1):
        url =f'https://www.coupang.com/np/search?q={keyword}&channel=user&sorter=scoreDesc&listSize=36&isPriceRange=false&rating=0&page={page}&rocketAll=false'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        products_lis = soup.find('ul', id='productList').find_all('li')
        for li in products_lis:
            a_link = li.find('a', href=True)['href']
            prd_link = baseurl + a_link
            prd_name = li.find('div', class_='name').text
            try:
                base_price = li.find('span', class_='price-info').find('del', class_='base-price').text
            except:
                base_price = ''
            price = li.find('strong', class_='price-value').text

            products_info = {
                'name': prd_name,
                'base_price': base_price,
                'price': price,
                'product_url': prd_link
            }
            products_link.append(products_info)

    print(len(products_link))
    df = pd.DataFrame(products_link)
    print(df)
    df.to_csv('쿠팡_products_list.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    coupang_products('노트북', 1)