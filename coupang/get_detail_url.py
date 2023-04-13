import os
import time
import math
import csv

#크롬드라이버 버전 자동 설치
import chromedriver_autoinstaller
from numpy import source
# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    #print(f"chrom driver is insatlled: {driver_path}")
    pass
else:
    #print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

#셀레니움
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

#크롬드라이버 콘솔창 제거_________________
from subprocess import CREATE_NO_WINDOW
service = Service(driver_path)
service.creationflags = CREATE_NO_WINDOW


# Selenium setting
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")

#options.add_argument('headless')            # headless모드 (창 비활성화)
options.add_argument('disable-gpu')         # GPU 가속 종료
options.add_argument("lang=ko_KR")          # 가짜 플러그인 탑재

driver = webdriver.Chrome(options=options, service=service)
actions = ActionChains(driver)

from bs4 import BeautifulSoup as bs
import time
import requests

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
    

tag_list = tag_list[1:]

url_list = []
for tag in tag_list:
    url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
    url_list.append(url)
print('ck1')

# CSV 파일을 쓰기 모드로 열기


for num,tag in enumerate(tag_list,start=1):

        driver = webdriver.Chrome(options=options, service=service)
        actions = ActionChains(driver)

        # # driver.get(url)
        url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
        driver.get(url)
        elem = driver.find_element(By.TAG_NAME, 'body').text

        find_word = '"itemTotalCount":'
        total_cnt = elem[elem.find(find_word) + len(find_word):]
        total_cnt = total_cnt[:total_cnt.find(",")]
        print(total_cnt)

        cnt = math.ceil(int(total_cnt)/30)

        detail_url = []
        file_path = 'detail_url.csv'
        for pageNum in range(1, cnt+1): 
            url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum={str(pageNum)}'
            driver.get(url)
            find_word = 'link'
            elem = driver.find_element(By.TAG_NAME, 'body').text
            cnt = elem.count(find_word)
            for i in range(cnt):
                search2 = elem[elem.find(find_word) + len(find_word)+3:]
                elem = search2
                search2 = search2[:search2.find('"')]
                detail_url.append(search2)
        with open(file_path, "a", newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            for url in detail_url:
                writer.writerow([url])
        time.sleep(2)
        print(f'{num}/{len(tag_list)}')
        driver.close()                

        # print(len(detail_url))




    

    
