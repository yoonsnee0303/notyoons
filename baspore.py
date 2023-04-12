from bs4 import BeautifulSoup as bs
import time
import requests
import re
import csv

with open('html_files.txt', 'r',encoding='utf-8') as f:
    html = f.read()
soup = bs(html,'html.parser')
li_tags = soup.find_all('li', {'class': 'scp-component-category-item'})


label_tags = soup.find_all('label')
cnt = 0
tag_list = []
for tag in label_tags:
    if str(tag).__contains__('for="component'):
        parent = tag.parent
        if not str(parent).__contains__ ('href'):
            cnt+=1
            tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
            tag_list.append(tag)
            print(cnt)
    

tag_list = tag_list[1:]
print(tag_list)
print(tag_list[0])
print(type(tag_list[0]))
for tag in tag_list:
    url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
    response = requests.get(url)
    print(response)
    # with open("url_list.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(url)
    # response = requests.get(url)
    # print(response)
    # json_data = response.json()

    # if 'data' in json_data.keys() and 'itemTotalCount' in json_data['data'].keys():
    #     item_total_count = json_data['data']['itemTotalCount']
    #     print(f"'itemTotalCount' 키의 값: {item_total_count}")
    # else:
    #     print(f"'itemTotalCount' 키를 찾을 수 없습니다.")


# pagenum은 json에서 item_total_count를 가지고 온 다음에 30으로 나누면 되겠죠/???? 30으로 나눈 몫의 값만큼 pagenum을 for 구문으로 돌리고.... 상품 상세 링크(link) 들고 오면 되지요
    

    
