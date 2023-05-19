from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage
import math

import sys
import psutil
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QToolBar, QDialog
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QProgressBar, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from firebase_admin import storage
from firebase_admin import credentials
import firebase_admin
import requests
import re

import pytesseract
import cv2
import urllib.request
import pyautogui
from bs4 import BeautifulSoup as bs
import os
import urllib3
import csv
from PIL import Image
import unittest
import time
import socket

import datetime
now = datetime.datetime.now()
now = now.strftime('%Y%m%d %H%M%S')

import getpass
path_input = getpass.getuser()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
in_ip = sock.getsockname()[0]
print("내부 IP: ", in_ip)
req = requests.get("http://ipconfig.kr")
ex_ip = re.search(
    r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", ex_ip)


# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate(
    'upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f.appspot.com'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert


import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)





class WorkerThread_mall(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self,test):
        super().__init__()
        self.test = test
    
    def run(self):
        self.login_id = getpass.getuser()

        self.log_update.emit(f'firebase 서버 접속')


        # 옵션 - 셀레니움
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink_features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable_logging"])
        options.add_argument("no_sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extionsions")
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)

        def open_csv(file_name):  # return lists, start_cnt
            with open(f'{file_name}_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
                read = csv.reader(f)
                lists = list(read)
            lists = lists[0]
            # print(lists)
            for i in range(len(lists)):
                if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
                    start_cnt = i
                    break

            return lists, start_cnt
        
        def brand():  # return brand_lists
            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today','gmarket', 'auction', 'interpark', 'coupang']
            return brand_lists
        
        def get_week_of_month():  # return week_syntax
            today = datetime.date.today()
            first_day_of_month = datetime.date(today.year, today.month, 1)
            week_number = (today - first_day_of_month).days // 7 + 1
            week_syntax = str(today.month) + '월' + str(week_number) + '주차'
            return week_syntax
        

        brand_lists = brand()
        
        def txt_check(file_name, text):  # return '동서가구'
            self.log_img_update.emit(text)
            if text.count("동서가구"):
                print(text)
                print("\n\n\n")

                pyautogui.screenshot(f'{file_name}.jpg')
                image_file_path = f'{file_name}.jpg'
                # brand_lists = brand()
                for brand in brand_lists:
                    if brand in file_name:
                        # make bucket and get folder name for each brand
                        bucket = storage.bucket()
                        folder_name = get_week_of_month()
                        folder_blob = bucket.blob(folder_name)

                        # check specific folder name exist or not
                        if not folder_blob.exists():
                            print(f'Creating folder {folder_name}')
                            folder_blob.upload_from_string('')

                        # Upload a file to the folder
                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                        blob.upload_from_filename(image_file_path)
                        print(f'File {file_name} uploaded to {folder_name}')
                        self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                        if os.path.exists('./'+file_name):
                            os.remove('./'+file_name)
                            print(f"{file_name}가 삭제되었습니다.")
                        else:
                            print(f"{file_name}가 존재하지 않습니다.")
                        break

                return '동서가구'
            else:
                return
            
        def img_check(url, width_con, hight_con1, hight_con2, cropped_con):  # return check, hight
            def 이미지확인(url):
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                
                urllib.request.urlretrieve(url, f"test1_{self.login_id}.jpg")
                # log
                # load the new pixmap
                new_pixmap = QPixmap(f"test1_{self.login_id}.jpg")
                # emit the custom signal to pass the new pixmap to the main thread
                self.pixmap_update.emit(new_pixmap)

                image = cv2.imread(f"test1_{self.login_id}.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
                img_width = int(image.shape[1])
                img_hight = int(image.shape[0])
                print(img_width, img_hight)

                print(img_width/100)
                width_unit = int(round(img_width/100))
                hight_unit = int(round(img_hight/100))
                print(width_unit)
                # plt.imshow(image, cmap="gray"), plt.axis("off")
                # plt.show()

                return image, img_width, img_hight, width_unit, hight_unit

            def 상단글자(image, width_unit, hight_unit, img_width, img_hight):
                try:
                    width = 0

                    print('img_width:', img_width)
                    print('img_hight:', img_hight)
                    print('width_unit:', width_unit)
                    print('hight_unit:', hight_unit)
                    # time.sleep(1000)

                    for hight in range(width_unit, img_hight, hight_unit):
                        now_hight = (hight/img_hight)*50
                        print(hight)
                        print(img_hight)

                        if img_width != width_con:
                            if hight >= hight_con1:
                                image_cropped = image[hight - hight_con1:hight, width:]
                            else:
                                image_cropped = image[:hight, width:]
                        else:
                            if hight >= hight_con2:
                                image_cropped = image[hight - hight_con2:hight, cropped_con:]
                            else:
                                image_cropped = image[:hight, cropped_con:]

                        text = pytesseract.image_to_string(image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                        print(text)

                        #log
                        self.log_img_update.emit(text)

                        # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                        # plt.show()

                        if hight > (img_hight)*0.9:  # img_hight
                            return hight,img_hight,'이미지없음'
                        elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                            # plt.show()
                            return hight,img_hight,'동서가구'
                except:
                    pass

            image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
            hight,img_hight,check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)

            return hight, img_hight, check
        # cou
        # cou
        # cou
        if self.test == '쿠팡':
            #log
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('cou') # cou_list.csv
                brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split('=')[1].split('&')[0]
                    file_name = 'cou' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'쿠팡 [텍스트 상단] 확인 중..')
                    main = soup.find('div', class_='prod-atf-main').text.strip().replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    # 02 필수 표기정보
                    # log
                    self.log_update.emit(f'쿠팡 [텍스트 필수 표기정보] 확인 중..')
                    driver.find_element(By.ID, 'itemBrief').click()
                    brief = soup.find('div', id="itemBrief").text.strip().replace (" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                    check = txt_check(file_name, brief)
                    if check == '동서가구':
                        return '동서가구'

                    # 03 배송/교환/반품 안내
                    # log
                    self.log_update.emit(f'쿠팡 [텍스트 배송/교환/반품 안내] 확인 중..')
                    driver.find_element(By.NAME, 'etc').click()
                    time.sleep(1)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    etc = soup.find('li', class_='product-etc tab-contents__content').text.strip().replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                    check = txt_check(file_name, etc)
                    if check == '동서가구':
                        return '동서가구'
                    
                    # img #img #img #img #img #img #img #img #img #img
                    # 04 이미지
                    # log
                    self.log_update.emit(f'쿠팡 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    img_url = 'https:' + soup.find('img', class_="prod-image__detail")['src']
                    print(img_url)
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        pyautogui.screenshot(f'{file_name}.jpg')
                        print(f'{file_name}.jpg')

                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:

                            if brand in file_name:

                                # make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                # check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                        return '동서가구'
                    
                    # 05 상세이미지
                    detail = soup.find('div', id="productDetail")
                    imgs = detail.find_all('img')
                    print(imgs)
                    imgs_cnt = 1
                    for img in imgs:
                        # log
                        self.log_update.emit(f'쿠팡 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['src']
                            img_url = src
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                count = 0
                                while count < len(lists):  # len(lists)
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)

                                    script = "document.querySelector('.product-detail-seemore-btn').click();"
                                    time.sleep(3)
                                    driver.execute_script(script)
                                    if hight < 50:
                                        driver.execute_script(f"window.scrollBy(0, {int(location['y']) - int(hight)*1.7});")
                                    elif 50 < hight < 80:
                                        driver.execute_script(f"window.scrollBy(0, {int(location['y']) - int(hight)});")
                                    else:
                                        driver.execute_script(f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                    time.sleep(2)
                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    image_file_path = f'{file_name}.jpg'

                                    for brand in brand_lists:
                                        if brand in file_name:
                                            # make bucket and get folder name for each brand
                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            # check specific folder name exist or not
                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            # Upload a file to the folder
                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            if os.path.exists('./'+file_name):
                                                os.remove('./'+file_name)
                                                print(f"{file_name}가 삭제되었습니다.")
                                            else:
                                                print(f"{file_name}가 존재하지 않습니다.")
                                            break
                                    break
                                break
                        except:
                            pass
                    return check
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)                
        # llst
        # llst
        # llst
        elif self.test == 'llst': 
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('11') # 11_list.csv
                brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split('/')[4].split('?')[0]
                    file_name = 'llst' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # text #text #text #text #text #text #text #text

                    # 01 상단
                    # log
                    self.log_update.emit(f'11번가 [텍스트 상단] 확인 중..')
                    main = soup.find('div', 'l_product_side_info').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    print(main)
                    check = txt_check(file_name,main)
                    if check == '동서가구':
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return 
                    
                    # #01 하단
                    self.log_update.emit(f'11번가 [텍스트 하단] 확인 중..')
                    element = driver.find_element(By.ID,'provisionNotice')
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    driver.execute_script("window.scrollBy(0, -100);")
                    time.sleep(2)
                    main = element.text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    print(main)
                    check = txt_check(file_name,main)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    
                    # img #img #img #img #img #img #img #img #img #img
                    # img #img #img #img #img #img #img #img #img #img


                    # 04 메인 이미지
                    # log
                    self.log_update.emit(f'11번가 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    img_url = soup.find('div', id="productImg") 
                    img_url = img_url.find('img')['src']
                    print(img_url)
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url,640,150,100,300)
                    if check == '동서가구':
                        pyautogui.screenshot(f'{file_name}.jpg')
                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:
                            if brand in file_name:
                                #make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                #check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                break
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    

                    # 05 상세페이지
                    self.log_update.emit(f'11번가 [이미지 상세이미지] 확인 중..')
                    iframes = driver.find_element(By.ID,'prdDescIfrm')
                    driver.switch_to.frame(iframes)
                    time.sleep(2)
                    iframe_html = driver.page_source
                    iframe_html = bs(iframe_html,'html.parser')
                    imgs = iframe_html.find_all('img')
                    print(imgs)
                    imgs_cnt = 1
                    links = []
                    for img in imgs:
                        self.log_update.emit(f'11번가 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        src = img['src']
                        img_url = src
                    #     links.append(img["src"])
                    # print(links)
                    # for link in links:
                        try:
                            # print(link)

                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url,640,150,100,300)
                            if check == '동서가구': 
                                self.log_update.emit('동서가구')
                                count = 0  

                                while count < len(links): #lists
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)

                                    script = "document.querySelector('.product-detail-seemore-btn').click();"
                                    time.sleep(3)
                                    driver.execute_script(script)
                                    print(hight)
                                    driver.execute_script(f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                    time.sleep(5)
                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    image_file_path = f'{file_name}.jpg'
                                    for brand in brand_lists:
                                        if brand in file_name:
                                            #make bucket and get folder name for each brand
                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            #check specific folder name exist or not
                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            # Upload a file to the folder
                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            if os.path.exists('./'+file_name):
                                                os.remove('./'+file_name)
                                                print(f"{file_name}가 삭제되었습니다.")
                                            else:
                                                print(f"{file_name}가 존재하지 않습니다.")
                                            break
                                break
                        
                        except:
                            pass
                    return check
                
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)
        # lot
        # lot
        # lot
        elif self.test == 'lot': 
            # log
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('lot') # lot_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                        driver.get(url)
                        print(url)
                        time.sleep(1)
                        scroll_height_increment = 300 
                        total_scroll_height = driver.execute_script("return document.body.scrollHeight") 

                        while True:
                            new_scroll_height = driver.execute_script("return window.pageYOffset + " + str(scroll_height_increment) + ";")
                            if new_scroll_height > total_scroll_height:
                                new_scroll_height = total_scroll_height

                            driver.execute_script("window.scrollTo(0, " + str(new_scroll_height) + ");")

                            time.sleep(0.3)

                            if driver.execute_script("return window.pageYOffset + window.innerHeight;") >= total_scroll_height:
                                break
                        code = driver.page_source
                        soup = bs(code, 'html.parser')

                        pro_num = url.split('=')[1]
                        file_name = 'lotte' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'롯데온 [텍스트 상단] 확인 중..')
                        main = soup.find('div', class_='purchase_product').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name,main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # 02 구매/배송정보
                        # log
                        self.log_update.emit(f'롯데온 [구매/배송정보] 확인 중..')
                        driver.find_element(By. CLASS_NAME, 'tab2').click()
                        time.sleep(.5)
                        soup = bs(driver.page_source, 'html.parser')

                        brief = soup.find('div', class_="wrap_detail content2 on").text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name,brief)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'


                        # img #img #img #img #img #img #img #img #img #img
                        # 03 이미지
                        # log
                        self.log_update.emit(f'롯데온 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        thumb = soup.find('div', class_='thumb_product')
                        img_url = thumb.find('img')['src']
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            count = 0
                            while count < len(lists) : #len(lists)
                                img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                print('find img_element')
                                location = img_element.location
                                print(location)

                                script = "document.querySelector('.product-detail-seemore-btn').click();"
                                time.sleep(3)
                                driver.execute_script(script)
                                driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                time.sleep(2)

                                pyautogui.screenshot(f'{file_name}.jpg')
                                print(f'{file_name}.jpg')

                                image_file_path = f'{file_name}.jpg'
                                for brand in brand_lists:
                                    if brand in file_name:

                                        bucket = storage.bucket()
                                        folder_name = get_week_of_month()
                                        folder_blob = bucket.blob(folder_name)

                                        if not folder_blob.exists():
                                            print(f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(image_file_path)
                                        print(f'File {file_name} uploaded to {folder_name}')
                                        break
                                count +=1
                            return '동서가구'
                        
                        #04 상세페이지
                        self.log_update.emit(f'롯데온 [이미지 상세이미지] 확인 중..')
                        driver.find_element(By. CLASS_NAME, 'tab1').click()
                        time.sleep(1)
                        soup = bs(driver.page_source, 'html.parser')
                        detail = soup.find('div', class_="detail")
                        imgs = detail.find_all('img')
                        imgs_cnt = 1
                        for img in imgs:
                            self.log_update.emit(f'롯데온 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                if src.count('data:image/gif;') == 0:
                                    if src.count('https:') == 0:
                                        src = 'https:' + src
                                    img_url = src
                                    ##
                                    ##
                                    ##
                                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                    if check == '동서가구':
                                        count = 0

                                        while count < len(lists) : #len(lists)
                                            img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                            print('find img_element')
                                            location = img_element.location
                                            print(location)

                                            script = "document.querySelector('.product-detail-seemore-btn').click();"
                                            time.sleep(1)
                                            driver.execute_script(script)
                                            driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                            time.sleep(1)

                                            pyautogui.screenshot(f'{file_name}.jpg')
                                            print(f'{file_name}.jpg')

                                            image_file_path = f'{file_name}.jpg'
                                            for brand in brand_lists:
                                                if brand in file_name:

                                                    bucket = storage.bucket()
                                                    folder_name = get_week_of_month()
                                                    folder_blob = bucket.blob(folder_name)

                                                    if not folder_blob.exists():
                                                        print(f'Creating folder {folder_name}')
                                                        folder_blob.upload_from_string('')

                                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                    blob.upload_from_filename(image_file_path)
                                                    print(f'File {file_name} uploaded to {folder_name}')
                                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                    if os.path.exists('./'+file_name):
                                                        os.remove('./'+file_name)
                                                        print(f"{file_name}가 삭제되었습니다.")
                                                    else:
                                                        print(f"{file_name}가 존재하지 않습니다.")
                                                        
                                            break
                                        break
                            except:
                                pass

                        # driver.close()
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        else:
                            return

                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')
        # ss
        # ss
        # ss
        elif self.test == 'ss':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('nav') # cou_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split('/')[-1]
                    file_name =  'naver'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'스마트스토어 [텍스트 상단] 확인 중..')
                    main = soup.find('fieldset').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    # 02 하단
                    # log
                    self.log_update.emit(f'스마트스토어 [텍스트 하단] 확인 중..')
                    element = driver.find_element(By.CLASS_NAME,"product_info_notice")
                    driver.execute_script("arguments[0].scrollIntoView();", element)

                    main = soup.find('div', id='INTRODUCE').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")

                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    # img #img #img #img #img #img #img #img #img #img
                    # 03 이미지
                    # log
                    self.log_update.emit(f'스마트스토어 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    main = soup.find('div', id='container')
                    img_urls = main.find_all('img')
                    for imm in img_urls:
                        try:
                            if imm['alt'] == '대표이미지':
                                img_url = imm['data-src']
                                break
                        except:
                            pass
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        count = 0
                        while count < len(lists) : 
                            
                            img_element = driver.find_element(By.XPATH, f"//img[@data-src='{img_url}']")
                            print('find img_element')
                            location = img_element.location
                            print(location)

                            driver.execute_script(f"window.scrollBy(0, {location['y']});")
                            time.sleep(3)
                            pyautogui.screenshot(f'{file_name}.jpg')
                            image_file_path = f'{file_name}.jpg'
                                    
                            for brand in brand_lists:
                                if brand in file_name:
                                    #make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    #check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    if os.path.exists('./'+file_name):
                                        os.remove('./'+file_name)
                                        print(f"{file_name}가 삭제되었습니다.")
                                    else:
                                        print(f"{file_name}가 존재하지 않습니다.")
                                    break
                        return '동서가구'
                    
                    # 04 상세 이미지
                    # log
                    detail = soup.find('div', id='INTRODUCE')
                    imgs = detail.find_all('img')
                    print(imgs)
                    imgs_cnt = 1
                    for img in imgs:
                        self.log_update.emit(f'스마트스토어 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['data-src']
                            img_url = src
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                count = 0
                                while count < len(lists):  # len(lists)
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)

                                    driver.execute_script("arguments[0].scrollIntoView();", img_element) # {behavior: 'smooth', block: 'start', inline: 'nearest', aligntotop: true}
                                    time.sleep(3)
                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    print(f'{file_name}.jpg')

                                    image_file_path = f'{file_name}.jpg'

                                    for brand in brand_lists:
                                        if brand in file_name:
                                            # make bucket and get folder name for each brand
                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            # check specific folder name exist or not
                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            # Upload a file to the folder
                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            if os.path.exists('./'+file_name):
                                                os.remove('./'+file_name)
                                                print(f"{file_name}가 삭제되었습니다.")
                                            else:
                                                print(f"{file_name}가 존재하지 않습니다.")
                                            break
                                    break
                                break
                        except:
                            pass
                    return check
                
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)                   
        # sin
        # sin
        # sin
        elif self.test == 'sin':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('sin') # sin_list.csv
                # 팝업 창 확인
                def check_alert(driver):
                    alert = Alert(driver)

                    # 경고 대화 상자의 텍스트 확인
                    popup_text = alert.text
                    print(popup_text)

                    # "품절된 상품입니다"라는 문자열이 포함되어 있는지 확인
                    if "판매가 종료된 상품입니다." in popup_text:
                        print("품절된 상품 팝업 창이 있습니다.")
                        return '판매종료'
                    else:
                        return '판매중'

                def EA_cou_item_ck(url):
                    
                    driver.get(url)
                    time.sleep(3)
                    check = check_alert(driver)
                    if check == '판매중':
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('=')[1]
                        file_name = 'sin'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'신세계 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'cdtl_row_top').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # 02 필수 표기정보
                        # log
                        self.log_update.emit(f'신세계 [텍스트 필수 표기정보] 확인 중..')
                        brief = soup.find_all('div', class_="cdtl_cont_info")
                        brief_text = ''
                        i = 0
                        for br in brief:
                            brief_text = br.text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                            if str.__contains__(brief_text,'동서가구'):
                                ActionChains(driver).move_to_element(driver.find_elements(By.CLASS_NAME,"cdtl_cont_info")[i]).perform()
                                break
                            i += 1
                            print(i)
                        brief = brief_text
                        check = txt_check(file_name,brief)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # 04 메인 이미지
                        # log
                        self.log_update.emit(f'신세계 [이미지 대표이미지] 확인 중..')

                        img_url = soup.find('span', class_='cdtl_imgbox imgzoom')
                        img_url = img_url.find('img')['src'] 
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')

                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:

                                if brand in file_name:

                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                    if os.path.exists('./'+file_name):
                                        os.remove('./'+file_name)
                                        print(f"{file_name}가 삭제되었습니다.")
                                    else:
                                        print(f"{file_name}가 존재하지 않습니다.")
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                            return '동서가구'
                        
                        # 05 상세 페이지
                        driver.find_element(By.CLASS_NAME,'cdtl_seller_html_collapse').click()
                        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
                        html = driver.find_element(By.CLASS_NAME,'cdtl_capture_img')
                        iframe = html.find_element(By.TAG_NAME, 'iframe')
                        driver.switch_to.frame(iframe)
                        time.sleep(2)
                        iframe_html = driver.page_source
                        iframe_html = bs(iframe_html,'html.parser')
                        imgs = iframe_html.find_all('img')
                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'신세계 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    self.log_update.emit('동서가구')
                                    count = 0
                                    while count < len(lists):  # len(lists)
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location
                                        print(location)
                                        img_element.click()
                                        driver.execute_script("arguments[0].scrollIntoView();", img_element)
                                        time.sleep(1)

                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        print(f'{file_name}.jpg')
                                        image_file_path = f'{file_name}.jpg'
                                        for brand in brand_lists:
                                            if brand in file_name:
                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                if os.path.exists('./'+file_name):
                                                    os.remove('./'+file_name)
                                                    print(f"{file_name}가 삭제되었습니다.")
                                                else:
                                                    print(f"{file_name}가 존재하지 않습니다.")
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                        count +=1
                                        break
                                    break
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)
        # oj
        # oj
        # oj
        elif self.test == 'oj':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('o') # cou_list.csv
                brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    string = url.split('?')[0]
                    pro_num = re.sub(r'[^0-9]', '', string)
                    file_name = 'today'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'오늘의집 [텍스트 상단] 확인 중..')
                    main = soup.find('div', 'production-selling-overview container').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    # img #img #img #img #img #img #img #img #img #img
                    # 04 메인 이미지
                    # log
                    self.log_update.emit(f'오늘의집 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    img_url = soup.find('img', class_="production-selling-cover-image__entry__image")['src']
                    print(img_url)
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        pyautogui.screenshot(f'{file_name}.jpg')
                        print(f'{file_name}.jpg')

                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:

                            if brand in file_name:

                                # make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                # check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                if os.path.exists('./'+file_name):
                                    os.remove('./'+file_name)
                                    print(f"{file_name}가 삭제되었습니다.")
                                else:
                                    print(f"{file_name}가 존재하지 않습니다.")
                        return '동서가구'
                    
                    # 04 상세이미지
                    detail = soup.find('div', class_="production-selling-description__content")
                    imgs = detail.find_all('img')
                    print(imgs)
                    go_out = False
                    imgs_cnt = 1
                    for img in imgs:
                        # log
                        self.log_update.emit(f'오늘의집 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['src']
                            img_url = src
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                detail = soup.find('div', class_="production-selling-description__content")
                                imgs = detail.find_all('img')
                                self.log_update.emit('동서가구')
                                for img in imgs:
                                    src = img['src']
                                    img_url2 = src

                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url2}']")

                                    driver.execute_script("arguments[0].scrollIntoView(true);", img_element)
                                    time.sleep(.5)
                                    scroll_y = driver.execute_script('return window.scrollY;')


                                    if img_url == img_url2:
                                        go_out = True
                                        if img_hight < 300:
                                            driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)-int(img_hight*2))});')
                                        elif hight > 800:
                                            hight = hight*.7
                                            driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)+int(hight))});')
                                        time.sleep(.5)

                                        print('scroll_y', scroll_y)
                                        print('hight', hight)
                                        print('img_hight', img_hight)

                                        pyautogui.screenshot(f'{file_name}_img.jpg')
                                        print(f'{file_name}_img.jpg')

                                        image_file_path = f'{file_name}_img.jpg'
                                        for brand in brand_lists:
                                            if brand in file_name:

                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                if os.path.exists('./'+file_name):
                                                    os.remove('./'+file_name)
                                                    print(f"{file_name}가 삭제되었습니다.")
                                                else:
                                                    print(f"{file_name}가 존재하지 않습니다.")
                                                break
                                    if go_out == True:
                                        break
                            if go_out == True:
                                break
                        except:
                            pass
                    return check
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)
        # interpark
        # interpark
        # interpark
        elif self.test == 'interpark':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('inter') # inter_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split("=")[1]
                    file_name = 'interpark'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'인터파크 [텍스트 상단] 확인 중..')
                    main = soup.find('div', 'productTopRight').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        self.log_update.emit('동서가구')
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    
                    
                    # img #img #img #img #img #img #img #img #img #img
                    # 04 이미지
                    # log
                    self.log_update.emit(f'인터파크 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    img_url = soup.find('div', class_='viewImage')
                    img_url = img_url.find('img')['src']
                    print(img_url)
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        pyautogui.screenshot(f'{file_name}.jpg')
                        print(f'{file_name}.jpg')

                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:
                            if brand in file_name:
                                # make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                # check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                        return '동서가구'
                    

                    # 05. 상세이미지
                    iframes = driver.find_elements(By.TAG_NAME, "iframe")
                    print(len(iframes))
                    for ifr in iframes:
                        if ifr.get_attribute('title').count('상품상세') > 0:
                            driver.switch_to.frame(ifr)
                            detail = bs(driver.page_source, 'html.parser')
                            break
                    
                    imgs = detail.find_all('img')
                    go_out = False
                    imgs_cnt = 1
                    for img in imgs:
                        # log
                        self.log_update.emit(f'인터파크 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['src']
                            img_url = src
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url,640,150,100,300)
                            if check == '동서가구':
                                detail = bs(driver.page_source, 'html.parser')
                                imgs = detail.find_all('img')

                                for img in imgs:
                                    src = img['src']
                                    img_url2 = src
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url2}']")

                                    driver.execute_script("arguments[0].scrollIntoView(true);", img_element)
                                    time.sleep(.5)
                                    scroll_y = driver.execute_script('return window.scrollY;')


                                    if img_url == img_url2:
                                        go_out = True
                                        if img_hight < 300:
                                            driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)-int(img_hight*2))});')
                                        elif hight > 800:
                                            hight = hight*.7
                                            driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)+int(hight))});')
                                        time.sleep(.5)

                                        print('scroll_y', scroll_y)
                                        print('hight', hight)
                                        print('img_hight', img_hight)
                                        
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        print(f'{file_name}.jpg')

                                        image_file_path = f'{file_name}.jpg'
                                        for brand in brand_lists:
                                            if brand in file_name:

                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                if os.path.exists('./'+file_name):
                                                    os.remove('./'+file_name)
                                                    print(f"{file_name}가 삭제되었습니다.")
                                                else:
                                                    print(f"{file_name}가 존재하지 않습니다.")
                                                break
                                    if go_out == True:
                                        break
                            if go_out == True:
                                break
                        except:
                            pass
                    return check
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)
        # auction
        # auction
        # auction
        elif self.test == 'auction':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('auc') # cou_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split('=')[1]
                    file_name = 'auction' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'옥션 [텍스트 상단] 확인 중..')
                    main = soup.find('div', 'item-topinfo').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    

                    # img #img #img #img #img #img #img #img #img #img
                    # 04 이미지
                    # log
                    button = driver.find_element(By.CLASS_NAME, "button__detail-more.js-toggle-button")
                    button.click()
                    img_url = soup.find('div', class_='box__viewer-container')
                    img_url = 'https:' + img_url.find('img')['src'] 
                    print(img_url)
                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        pyautogui.screenshot(f'{file_name}.jpg')
                        print(f'{file_name}.jpg')

                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:

                            if brand in file_name:

                                # make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                # check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                if os.path.exists('./'+file_name):
                                    os.remove('./'+file_name)
                                    print(f"{file_name}가 삭제되었습니다.")
                                else:
                                    print(f"{file_name}가 존재하지 않습니다.")
                                
                        return '동서가구'
                    # 05 상세이미지

                    iframe = driver.find_element(By.ID,'hIfrmExplainView')
                    driver.switch_to.frame(iframe)
                    time.sleep(2)
                    iframe_html = driver.page_source
                    iframe_html = bs(iframe_html,'html.parser')
                    imgs = iframe_html.find_all('img')
                    print(imgs)

                    imgs_cnt = 1
                    for img in imgs:
                        # log
                        self.log_update.emit(f'옥션 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['src']
                            img_url = src
                            ##
                            ##
                            ##

                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                count = 0
                                while count < len(lists):  # len(lists)
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)


                                    time.sleep(3)
                                    img_element.click()
                                    driver.execute_script(f"window.scrollBy(0,{int(location['y']) - int(hight)*0.5});")
                                    time.sleep(3)

                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    print(f'{file_name}.jpg')
                                    image_file_path = f'{file_name}.jpg'
                                    for brand in brand_lists:
                                        if brand in file_name:
                                            #make bucket and get folder name for each brand
                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            #check specific folder name exist or not
                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            # Upload a file to the folder
                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            if os.path.exists('./'+file_name):
                                                os.remove('./'+file_name)
                                                print(f"{file_name}가 삭제되었습니다.")
                                            else:
                                                print(f"{file_name}가 존재하지 않습니다.")
                                    count +=1
                                    break
                                break
                        except:
                            pass
                    return check
                
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('auc_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('auc_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)
        # gmarket
        # gmarket
        # gmarket
        elif self.test == 'gmarket':
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('gm') # cou_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
                    code = driver.page_source
                    soup = bs(code, 'html.parser')
                    pro_num = url.split('=')[1]
                    file_name = 'gmarket' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                    # text #text #text #text #text #text #text #text
                    # 01 상단
                    # log
                    self.log_update.emit(f'지마켓 [텍스트 상단] 확인 중..')
                    main = soup.find('div', 'item-topinfo').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                    check = txt_check(file_name, main)
                    if check == '동서가구':
                        return '동서가구'
                    elif main.count('현재판매중인상품이아닙니다'):
                        print("품절 상품 / 패스")
                        return
                    

                    # img #img #img #img #img #img #img #img #img #img
                    # 04 이미지
                    # log
                    self.log_update.emit(f'지마켓 [이미지 대표이미지] 확인 중..')
                    actions = ActionChains(driver)  
                    actions.send_keys(Keys.HOME).perform()  
                    img_url = soup.find('div', class_="box__viewer-container")
                    img_url = img_url.find('img')['src']
                    print(img_url)

                    ##
                    ##
                    ##
                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                    if check == '동서가구':
                        pyautogui.screenshot(f'{file_name}.jpg')
                        print(f'{file_name}.jpg')

                        image_file_path = f'{file_name}.jpg'
                        for brand in brand_lists:

                            if brand in file_name:

                                # make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = get_week_of_month()
                                folder_blob = bucket.blob(folder_name)

                                # check specific folder name exist or not
                                if not folder_blob.exists():
                                    print(f'Creating folder {folder_name}')
                                    folder_blob.upload_from_string('')

                                # Upload a file to the folder
                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                blob.upload_from_filename(image_file_path)
                                print(f'File {file_name} uploaded to {folder_name}')
                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                if os.path.exists('./'+file_name):
                                    os.remove('./'+file_name)
                                    print(f"{file_name}가 삭제되었습니다.")
                                else:
                                    print(f"{file_name}가 존재하지 않습니다.")
                        return '동서가구'
                    
                    # 05 상세이미지
                    iframes = driver.find_element(By.XPATH,"//iframe[@id='detail1']")
                    driver.switch_to.frame(iframes)
                    time.sleep(2)
                    iframe_html = driver.page_source
                    iframe_html = bs(iframe_html,'html.parser')
                    imgs = iframe_html.find_all('img')
                    print(imgs)

                    imgs_cnt = 1
                    for img in imgs:
                        # log
                        self.log_update.emit(f'지마켓 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                        imgs_cnt += 1
                        try:
                            src = img['src']
                            img_url = src
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                count = 0
                                while count < len(lists):  # len(lists)
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)

                                    script = "document.querySelector('.product-detail-seemore-btn').click();"
                                    time.sleep(3)
                                    driver.execute_script(script)
                                    driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                    time.sleep(2)
                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    image_file_path = f'{file_name}.jpg'

                                    for brand in brand_lists:
                                        if brand in file_name:

                                            #make bucket and get folder name for each brand
                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            #check specific folder name exist or not
                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            # Upload a file to the folder
                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            if os.path.exists('./'+file_name):
                                                os.remove('./'+file_name)
                                                print(f"{file_name}가 삭제되었습니다.")
                                            else:
                                                print(f"{file_name}가 존재하지 않습니다.")
                                    count +=1
                                    break
                                break
                        except:
                            pass
                    return check
                
            print('시작', datetime.datetime.now())
            for li in range(start_cnt, len(lists)):
                #log
                percent = int((li+1)/(len(lists)/100))
                self.progress_update.emit(percent)
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    self.log_update.emit('동서가구')
                    lists[li] = [lists[li], '스캔필요']
                    with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)        

class WorkerThread_list_get(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_update2 = pyqtSignal(str)

    def run(self):
        def get_week():
            def get_week_of_month(date):
                first_day = date.replace(day=1)
                adjusted_day = first_day + datetime.timedelta(days=(6 - first_day.weekday()))
                week_number = (date - adjusted_day).days // 7 + 2
                return week_number

            # Firebase Storage 인스턴스 생성
            bucket = firebase_storage.bucket()

            blobs = bucket.list_blobs()


            # 현재 날짜 구하기
            current_date = datetime.date.today()

            # 현재 월의 주차와 월 출력
            week_of_month = get_week_of_month(current_date)
            month = current_date.strftime("%m월")
            date = month[1:3] + str(week_of_month) + '주차'
            for l in list(range(10,12)): # 10월 11월 12월
                if str(l) in month:
                    date = month[:3] + str(week_of_month) + '주차'
                    print(date)
            for blob in blobs:
                # print(blob.name)
                folder_name = blob.name.split('/')[0]
                if date == folder_name:
                    print(f'{date}는 이미 다운로드 되어있는 주차입니다.')
                    return date,'다운로드 필요없음'
            return date,'다운로드 필요'
        
        def get_list(date):
            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today','gmarket', 'auction', 'interpark']
            cnt = 1
            ratio = 11
            brand_lists = ['auction','interpark','coupang']
            for brand in brand_lists:
                if brand == '11':
                    self.log_update.emit("11번가")
                    json_data = []
                    ll_lists = []
                    for pg in range(1,9): #41
                        test = int((ratio/8)*pg)
                        self.progress_update.emit(test)

                        url = f'https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=동서가구+장인가구&pageNo={pg}&pageSize=250'
                        response = requests.get(url)
                        response_json = response.json()  # JSON 형식으로 변환
                        for i in range(len(response_json['commonPrdList']['items'])):
                            u = response_json['commonPrdList']['items'][i]['productDetailUrl']
                            ll_lists.append(u)
                            print(f"11번가 {len(ll_lists)}")
                            self.log_update2.emit(f"상세페이지 총 {len(ll_lists)}개 수집")
                            print(u)

                    with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([ll_lists])
                    self.log_update2.emit(f"{date} csv 파일 저장 완료")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'lotte':
                    self.log_update.emit("롯데온")
                    url = 'https://www.lotteimall.com/search/searchMain.lotte?isTemplate=Y&headerQuery=장인가구&colldisplay=3200'
                    response = requests.get(url)
                    json_data = response.json()
                    temp = json_data['body'][15]['data'] # 15 ckp // 기존 16에서 동작되다 오류남 15로 바꾸니 정상동작 왜? 모름
                    # print(len(temp))
                    lotte_lists = []
                    for i in range(len(temp)):
                        test = int((ratio/len(temp))*i+ratio*1)

                        # log
                        self.progress_update.emit(test)
                        url = 'https://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=' + str(temp[i]['wishListMap']['goods_no'])
                        print(url)
                        lotte_lists.append(url)
                        print(f'롯데온 {len(lotte_lists)}')
                        
                        # log_update2
                        self.log_update2.emit(f"상세페이지 총 {len(lotte_lists)}개 수집")

                    with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lotte_lists])
                    self.log_update2.emit(f"{date} csv 파일 저장 완료")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'naver':
                    self.log_update.emit("스마트스토어")
                    nav_lists = []
                    find_word = '/newdf2013/products/'
                    for page in range(1, 23):
                        test = int((ratio/22)*page+ratio*2)
                        self.progress_update.emit(test)
                        url = f'https://smartstore.naver.com/newdf2013/category/e78c2895503c4c4e993a71348c4cd9e8?st=POPULAR&dt=IMAGE&page={page}&size=40'
                        res = requests.get(url)
                        html = res.text
                        cnt = html.count(find_word)

                        for i in range(cnt):
                            html = html[html.find(find_word)+len(find_word):]
                            ea_url = 'https://smartstore.naver.com/newdf2013/products/' + html[:html.find('"')]
                            nav_lists.append(ea_url)
                            self.log_update2.emit(f"상세페이지 총 {len(nav_lists)}개 수집")
                            print(f'스마트스토어 {len(nav_lists)}')
                            print(ea_url)

                        #list_test csv파일로 저장
                        with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([nav_lists])
                    self.log_update2.emit(f"{date} 상세페이지 ")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'today':
                    self.log_update.emit("오늘의집")
                    #옵션 - 셀레니움
                    options = webdriver.ChromeOptions()
                    options.add_argument("--disable-blink_features=AutomationControlled")
                    options.add_experimental_option("excludeSwitches",["enable_logging"])
                    options.add_argument("no_sandbox")
                    options.add_argument("--start-maximized")
                    options.add_argument("disable-infobars")
                    options.add_argument("--disable-extionsions")
                    options.add_experimental_option("useAutomationExtension",False)
                    options.add_argument("headless")
                    options.add_argument("disable-gpu")
                    options.add_argument("lang=ko_KR")
                    driver = webdriver.Chrome(options=options)
                    actions = ActionChains(driver)
                    url = 'https://ohou.se/brands/home?query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC'

                    driver.get(url)
                    time.sleep(1)

                    scroll_height = 10000

                    o_lists = []
                    while True:
                            
                        html = driver.page_source
                        soup = bs(html, 'html.parser')

                        elems = soup.find_all('a', 'production-item__overlay')

                        for el in range(len(elems)):
                            temp = 'https://ohou.se' + elems[el]['href']
                            o_lists.append(temp)
                            self.log_update2.emit(f"상세페이지 총 {len(o_lists)}개 수집")
                            print(f'오늘의집 {len(o_lists)}')
                            print(temp)
                        o_lists = list(dict.fromkeys(o_lists))
                        test = int((ratio/400)*len(o_lists)+ratio*3)
                        self.progress_update.emit(test)

                        # Scroll down by the defined amount
                        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
                        time.sleep(1)

                        # get the current scroll position
                        scroll_position = driver.execute_script("return window.pageYOffset;")


                        #마지막 페이지 확인

                        cnt = 0
                        if 'temp_scroll_postion' in locals() and temp_scroll_postion == scroll_position:
                            # print(o_lists)
                            cnt += 1
                            #list_test csv파일로 저장
                            with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                                write = csv.writer(f)
                                write.writerows([o_lists])


                            break
                        #아니면 계속 리스트 수집
                        temp_scroll_postion = scroll_position
                    
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'gmarket':
                    self.log_update.emit("지마켓")
                    url = 'https://browse.gmarket.co.kr/search?keyword=장인가구+동서가구'
                    response = requests.get(url)
                    soup = bs(response.text, 'html.parser')
                    a_tags = soup.find_all('a', 'link__shop')

                    url2 = 'http://item.gmarket.co.kr/Item?goodscode='

                    gm_lists = []
                    for tag in range(len(a_tags)):
                        test = int((ratio/len(a_tags))*tag+ratio*5)
                        self.progress_update.emit(test)
                        gm = url2 + str(a_tags[tag].get('data-montelena-goodscode')).strip('[]"\'')
                        gm_lists.append(gm)
                        self.log_update2.emit(f"상세페이지 총 {len(gm_lists)}개 수집")   
                        print(f'지마켓 {len(gm_lists)}')
                        print(gm)


                    with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        writer = csv.writer(f)
                        writer.writerow(gm_lists)
                    
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    
                    
                elif brand == 'auction':
                    self.log_update.emit("옥션")
                    auc_lists = []
                    for pg in range(1,6):
                        test = int((ratio/5)*pg+ratio*6)
                        self.progress_update.emit(test)
                        url = f'https://browse.auction.co.kr/search?keyword=%ec%9e%a5%ec%9d%b8%ea%b0%80%ea%b5%ac%2b%eb%8f%99%ec%84%9c%ea%b0%80%ea%b5%ac&itemno=&nickname=&encKeyword=%25EC%259E%25A5%25EC%259D%25B8%25EA%25B0%2580%25EA%25B5%25AC%252B%25EB%258F%2599%25EC%2584%259C%25EA%25B0%2580%25EA%25B5%25AC&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=0&p={pg}'
                        response = requests.get(url)

                        html_content = response.text
                        soup = bs(html_content, 'html.parser')
                        a_tags = soup.find_all('a')

                        hrefs = [a_tag['href'] for a_tag in a_tags if 'href' in a_tag.attrs if 'itempage3' in a_tag['href']]
                        hrefs = hrefs[::2]
                        for href in hrefs:
                            auc_lists.append(href)
                            self.log_update2.emit(f"상품페이지 총 {len(auc_lists)}개 수집")
                            print(f'옥션 {len(auc_lists)}')
                            print(href)
                            # print(href)


                    with open('auc_list.csv', "w", newline='',encoding="utf-8-sig") as f:
                        writer = csv.writer(f)
                        writer.writerows([auc_lists])
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")

                elif brand == 'interpark':
                    self.log_update.emit("인터파크")
                    url_data = []
                    for i in range(134): 
                        try:
                            url = f'https://shopping.interpark.com/niSearch/shop/listPrdChoiceAndNormal.json?pis1=shop&page={i+1}&keyword=장인가구&rows=52'
                            res = requests.get(url)
                            data = json.loads(res.text)
                            test = int((ratio/134)*i+ratio*7)
                            self.progress_update.emit(test)
                            cnt = len(data['data']['listChoiceAndNormal'][0])
                            for j in range(cnt+1):
                                try:
                                    item_url = 'https://shopping.interpark.com/product/productInfo.do?prdNo=' + str(data['data']['listChoiceAndNormal'][j]['prdNo'])
                                    # print(f'{j}/{item_url}')
                                    # print(cnt)
                                    url_data.append(item_url)
                                    self.log_update2.emit(f"상세페이지 총 {len(url_data)}개 수집")
                                    print(f'인터파크 {len(url_data)}')
                                    print(item_url)
                                except:
                                    pass
                        except:
                            pass
                    
                    #list_test csv파일로 저장
                    with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([url_data])
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    
                # elif brand == 'coupang':

                self.progress_update.emit(cnt*ratio)
                cnt += 1 

        date,check = get_week()
        if check == '다운로드 필요':
            get_list(date)


                

    def stop(self):
        self.log_update2.emit("다운로드 완료")
        # Stop the thread gracefully
        pass

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Item list check & Download")
        self.resize(400, 1)

        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar(self)
        label_log = QLabel('log')
        label_log2 = QLabel('log2')

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.progress_bar)
        vbox1.addWidget(label_log)
        vbox1.addWidget(label_log2)

        layout.addLayout(vbox1)

        # Create a worker thread to perform the independent work
        self.worker_thread = WorkerThread_list_get()
        self.worker_thread.progress_update.connect(self.update_progress)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_update2.connect(label_log2.setText)
        self.worker_thread.finished.connect(self.close_dialog)
        self.finished.connect(self.worker_thread.stop)
        self.showEvent = self.start_work

    def start_work(self, event):
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def close_dialog(self):
        self.close()
        

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread_running = False

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Confirm Close', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                #크롬, 크롬드라이버 프로세서 종료
                processes = [p for p in psutil.process_iter(['pid', 'name', 'create_time'])]
                processes_sorted = sorted(processes, key=lambda x: x.info['create_time'], reverse=True)

                #프로세스 내 chromedriver.exe가 있으면 chrome, chromedriver 종료
                for process in processes_sorted:
                    print(f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")
                    if process.info['name'] == 'chromedriver.exe':

                        for process in processes_sorted:
                            print(f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")

                            if process.info['name'] == 'chrome.exe':
                                process_id = process.info['pid']
                                process = psutil.Process(process_id)
                                process.terminate()
                            elif process.info['name'] == 'chromedriver.exe':
                                process_id = process.info['pid']
                                process = psutil.Process(process_id)
                                process.terminate()
                                break
                        event.accept()
                event.accept()
            else:
                event.ignore()

    def initUI(self):
        self.login_id = getpass.getuser()

        리스트받아오기 = QAction('리스트받아오기', self)
        쿠팡 = QAction('쿠팡', self)
        ll번가 = QAction('11번가', self)
        롯데온 = QAction('롯데온', self)
        스마트스토어 = QAction('스마트스토어', self)
        신세계 = QAction('신세계', self)
        오늘의집 = QAction('오늘의집', self)
        인터파크 = QAction('인터파크', self)
        옥션 = QAction('옥션', self)
        지마켓 = QAction('지마켓', self)

        self.statusBar()

        self.toolbar = QToolBar()
        self.toolbar.addAction(리스트받아오기)
        self.toolbar.addAction(쿠팡)
        self.toolbar.addAction(ll번가)
        self.toolbar.addAction(롯데온)
        self.toolbar.addAction(스마트스토어)
        self.toolbar.addAction(신세계)
        self.toolbar.addAction(오늘의집)
        self.toolbar.addAction(인터파크)
        self.toolbar.addAction(옥션)
        self.toolbar.addAction(지마켓)

        self.addToolBar(self.toolbar)

        # toolbar action
        리스트받아오기.triggered.connect(self.open_popup)
        쿠팡.triggered.connect(self.cou)
        ll번가.triggered.connect(self.llst)
        롯데온.triggered.connect(self.lot)
        스마트스토어.triggered.connect(self.ss)
        신세계.triggered.connect(self.sin)
        오늘의집.triggered.connect(self.oj)
        인터파크.triggered.connect(self.interpark)
        옥션.triggered.connect(self.auction)
        지마켓.triggered.connect(self.gmarket)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 800, 600)
        self.show()

    # 쿠팡함수
    def cou(self):

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('쿠팡 수집')
        label_log = QLabel('쿠팡 수집')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = '쿠팡'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def llst(self):

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('11번가 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'llst'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def lot(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('롯데온 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'lot'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def ss(self):
        

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('네이버스마트스토어 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'ss'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def sin(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('신세계 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'sin'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def oj(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('오늘의집 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'oj'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def interpark(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('인터파크 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'interpark'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def auction(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('옥션 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'auction'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def gmarket(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('지마켓 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'gmarket'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def resetThreadRunning(self):
        self.thread_running = False

    def open_popup(self):
        popup = PopupDialog(self)
        popup.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
