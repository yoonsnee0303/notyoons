import sys
import psutil

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QToolBar
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QProgressBar, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox



class WorkerThread_cou(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self,test):
        super().__init__()
        self.test = test
    def run(self):
        self.log_update.emit(f'firebase 서버 접속')
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

        import chromedriver_autoinstaller
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
        if os.path.exists(driver_path):
            print(f"chrome driver is installed: {driver_path}")
        else:
            print(f"install the chrome driver(ver: {chrome_ver})")
            chromedriver_autoinstaller.install(True)

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
                        # if os.path.exists('./'+file_name):
                        #     os.remove('./'+file_name)
                        #     print(f"{file_name}가 삭제되었습니다.")
                        # else:
                        #     print(f"{file_name}가 존재하지 않습니다.")
                        break

                return '동서가구'
            else:
                return
            
        def img_check(url, width_con, hight_con1, hight_con2, cropped_con):  # return check, hight
            def 이미지확인(url):
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                urllib.request.urlretrieve(url, "test1.jpg")
                # log
                # load the new pixmap
                new_pixmap = QPixmap('test1.jpg')
                # emit the custom signal to pass the new pixmap to the main thread
                self.pixmap_update.emit(new_pixmap)

                image = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
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
        elif self.test == 'llst': # 완
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
        elif self.test == 'lot': # 완
            self.log_update.emit(f'firebase 서버 접속')
            if ex_ip != '183.100.232.2444':
                lists, start_cnt = open_csv('lot') # lot_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)

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
                    time.sleep(2)
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

                    driver.quit()
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
                lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
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

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)
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
                lists, start_cnt = open_csv('sin') # cou_list.csv
                # brand_lists = brand()   
                def EA_cou_item_ck(url):
                    driver.get(url)
                    time.sleep(3)
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
                # ignore the close event
                event.ignore()

    def initUI(self):
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
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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
        pixmap = QPixmap('test1.jpg')
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        aspect_ratio = pixmap.width() / pixmap.height()
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
        self.worker_thread = WorkerThread_cou(test)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
