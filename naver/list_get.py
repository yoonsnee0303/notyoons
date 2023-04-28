import requests
import csv

nav_list = []
find_word = '/newdf2013/products/'
for page in range(1, 23):
    url = f'https://smartstore.naver.com/newdf2013/category/e78c2895503c4c4e993a71348c4cd9e8?st=POPULAR&dt=IMAGE&page={page}&size=40'
    res = requests.get(url)
    print(res.url)

    html = res.text
    cnt = html.count(find_word)

    for i in range(cnt):
        html = html[html.find(find_word)+len(find_word):]
        ea_url = 'https://smartstore.naver.com/newdf2013/products/' + html[:html.find('"')]
        nav_list.append(ea_url)

    #list_test csv파일로 저장
    with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
        write = csv.writer(f)
        write.writerows([nav_list])
    
    print(f'{page}/22')
