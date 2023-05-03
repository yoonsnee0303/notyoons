import requests
from bs4 import BeautifulSoup as bs
import csv

detail_url = []
for pg in range(1,6):
    url = f'https://browse.auction.co.kr/search?keyword=%ec%9e%a5%ec%9d%b8%ea%b0%80%ea%b5%ac%2b%eb%8f%99%ec%84%9c%ea%b0%80%ea%b5%ac&itemno=&nickname=&encKeyword=%25EC%259E%25A5%25EC%259D%25B8%25EA%25B0%2580%25EA%25B5%25AC%252B%25EB%258F%2599%25EC%2584%259C%25EA%25B0%2580%25EA%25B5%25AC&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=0&p={pg}'
    response = requests.get(url)

    html_content = response.text

    # HTML 코드가 저장된 문자열 변수를 이용하여 BeautifulSoup 객체 생성
    soup = bs(html_content, 'html.parser')

    # a 태그 찾기
    a_tags = soup.find_all('a')

    # href 속성 추출하기
    hrefs = [a_tag['href'] for a_tag in a_tags if 'href' in a_tag.attrs if 'itempage3' in a_tag['href']]
    hrefs = hrefs[::2]
    for href in hrefs:
        detail_url.append(href)
    print(url)
    print(pg,'/5')

print(detail_url)
with open('auc_list.csv', "w", newline='',encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows([detail_url])
