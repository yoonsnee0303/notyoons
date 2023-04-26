import requests
from bs4 import BeautifulSoup as bs
import csv

detail_url = []

url = 'https://browse.gmarket.co.kr/search?keyword=장인가구+동서가구'
response = requests.get(url)

html_content = response.text

# HTML 코드가 저장된 문자열 변수를 이용하여 BeautifulSoup 객체 생성
soup = bs(html_content, 'html.parser')

# a 태그 찾기
a_tags = soup.find_all('a', 'link__shop')

# print(a_tags)
url2 = 'http://item.gmarket.co.kr/Item?goodscode='
detail_url = []
for tag in a_tags:
    tag = str(tag).split(' ')
    for t in tag:
        if 'data-montelena-goodscode' in t:
            t = t.split('=')[1].replace('"','').replace("'","").replace("]","")
            detail_url.append(url2 + t)
print(detail_url)
print(len(detail_url))

import csv
with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([detail_url])






