from firebase_admin import storage
from firebase_admin import credentials
import firebase_admin
import requests
import re
import sys
import psutil


from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QToolBar
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QProgressBar, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import pytesseract
import cv2
import urllib.request
import pyautogui
from bs4 import BeautifulSoup as bs
import os
import urllib3
import csv
from PIL import Image
import sys
import unittest
import time
import socket
import datetime

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


def run(self):
    start_cnt = 0
    if ex_ip != '183.100.232.2444':
        def open_csv(csv):  # return lists, start_cnt
            with open(f'{csv}_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
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
            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today',
                           'gmarket', 'auction', 'interpark', 'coupang']
            return brand_lists

        def txt_check(file_name, text):  # return '동서가구'
            if text.count("동서가구"):
                print(text)
                print("\n\n\n")

                pyautogui.screenshot(f'{file_name}.jpg')
                image_file_path = f'{file_name}.jpg'
                brand_lists = brand()
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
                        break

                return '동서가구'

            else:
                return

        def get_week_of_month():  # return week_syntax
            today = datetime.date.today()
            first_day_of_month = datetime.date(today.year, today.month, 1)
            week_number = (today - first_day_of_month).days // 7 + 1
            week_syntax = str(today.month) + '월' + str(week_number) + '주차'
            return week_syntax
        # img_check 쓸 때 'self.img_check(url, 300)'

        def img_check(url, width_con, hight_con1, hight_con2, interval_con):  # return check, hight
            def 이미지확인(url):
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                urllib.request.urlretrieve(url, "test1.jpg")

                # log
                # load the new pixmap
                new_pixmap = QPixmap('test1.jpg')
                # emit the custom signal to pass the new pixmap to the main thread
                self.pixmap_update.emit(new_pixmap)

                image = cv2.imread(
                    "test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
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
                                image_cropped = image[hight -
                                                      hight_con1:hight, width:]
                            else:
                                image_cropped = image[:hight, width:]
                        else:
                            if hight >= hight_con2:
                                image_cropped = image[hight -
                                                      hight_con2:hight, interval_con:]
                            else:
                                image_cropped = image[:hight, interval_con:]

                        text = pytesseract.image_to_string(
                            image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                        print(text)

                        # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                        # plt.show()

                        if hight > (img_hight)*0.9:  # img_hight
                            return '이미지없음', hight
                        elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                            # plt.show()
                            return '동서가구', hight
                except:
                    pass

            image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
            print('test')
            check, hight = 상단글자(image, width_unit,
                                hight_unit, img_width, img_hight)
            print('hre')

            return check, hight

        def EA_cou_item_ck(url):  # return check


class WorkerThread_cou(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

    def run(self):
        # log
        self.log_update.emit(f'firebase 서버 접속')

        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import storage

        # Firebase 서비스 계정의 키 파일 경로
        cred = credentials.Certificate(
            'upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

        # Firebase 프로젝트 ID
        project_id = 'upload-img-5b02f.appspot.com'

        # Firebase 초기화
        firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

        import time
        import socket
        import re
        import requests
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("pwnbit.kr", 443))
        in_ip = sock.getsockname()[0]
        print("내부 IP: ", in_ip)
        req = requests.get("http://ipconfig.kr")
        ex_ip = re.search(
            r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
        print("외부 IP: ", ex_ip)

        start_cnt = 0
        if ex_ip != '183.100.232.2444':

            import csv
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기

            # log
            self.log_update.emit(f'쿠팡 수집 리스트 확인')

            with open('cou_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
                read = csv.reader(f)
                lists = list(read)
            lists = lists[0]
            # print(lists)

            for i in range(len(lists)):
                if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
                    start_cnt = i
                    break

            import getpass
            path_input = getpass.getuser()

            import pytesseract
            import cv2
            # from matplotlib import pyplot as plt
            import urllib.request

            import pyautogui
            from bs4 import BeautifulSoup as bs
            import os
            import urllib3
            import csv
            from PIL import Image
            import sys
            import unittest

            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today',
                           'gmarket', 'auction', 'interpark', 'coupang']

            # save in Firebase
            # save in Firebase
            # save in Firebase
            def to_ascii(string):
                return int(sum([ord(character) for character in string]) / len(brand_lists))

            def get_week_of_month():
                today = datetime.date.today()
                first_day_of_month = datetime.date(today.year, today.month, 1)
                week_number = (today - first_day_of_month).days // 7 + 1
                week_syntax = str(today.month) + '월' + str(week_number) + '주차'

                return week_syntax

            # make dicts
            brand_dicts = {}
            for brand in brand_lists:
                ascii_code = to_ascii(brand)
                brand_dicts[brand] = {ascii_code: []}

            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            def txt_check(file_name, text):
                if text.count("동서가구"):
                    print(text)
                    print("\n\n\n")

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
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                            break

                    return '동서가구'

                else:
                    return

            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            def img_check(url):
                def 이미지확인(url):
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                    urllib.request.urlretrieve(url, "test1.jpg")

                    # log
                    # load the new pixmap
                    new_pixmap = QPixmap('test1.jpg')
                    # emit the custom signal to pass the new pixmap to the main thread
                    self.pixmap_update.emit(new_pixmap)

                    image = cv2.imread(
                        "test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
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

                            if img_width != 640:
                                if hight >= 150:
                                    image_cropped = image[hight -
                                                          150:hight, width:]
                                else:
                                    image_cropped = image[:hight, width:]
                            else:
                                if hight >= 100:
                                    image_cropped = image[hight -
                                                          100:hight, 300:]
                                else:
                                    image_cropped = image[:hight, 300:]

                            text = pytesseract.image_to_string(
                                image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                            print(text)

                            # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                            # plt.show()

                            if hight > (img_hight)*0.9:  # img_hight
                                return '이미지없음', hight
                            elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                                # plt.show()
                                return '동서가구', hight
                    except:
                        pass

                image, img_width, img_hight, width_unit, hight_unit = 이미지확인(
                    url)
                print('test')
                check, hight = 상단글자(image, width_unit,
                                    hight_unit, img_width, img_hight)
                print('hre')

                return check, hight

            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔

            def EA_cou_item_ck(url):

                urllib3.disable_warnings(
                    urllib3.exceptions.InsecureRequestWarning)

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
                chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
                    0]
                driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
                if os.path.exists(driver_path):
                    print(f"chrome driver is installed: {driver_path}")
                else:
                    print(f"install the chrome driver(ver: {chrome_ver})")
                    chromedriver_autoinstaller.install(True)

                # 옵션 - 셀레니움
                options = webdriver.ChromeOptions()
                options.add_argument(
                    "--disable-blink_features=AutomationControlled")
                options.add_experimental_option(
                    "excludeSwitches", ["enable_logging"])
                options.add_argument("no_sandbox")
                options.add_argument("--start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extionsions")
                options.add_experimental_option(
                    "useAutomationExtension", False)
                # options.add_argument("headless")
                options.add_argument("disable-gpu")
                options.add_argument("lang=ko_KR")
                driver = webdriver.Chrome(options=options)
                actions = ActionChains(driver)

                driver.get(url)
                time.sleep(3)
                code = driver.page_source
                soup = bs(code, 'html.parser')

                import datetime
                now = datetime.datetime.now()
                now = now.strftime('%Y%m%d %H%M%S')

                pro_num = url.split('=')[1].split('&')[0]
                file_name = 'coupang'+'_' + \
                    now.split('.')[0].replace('-', '').replace(' ',
                                                               '_').replace(':', '') + '_' + pro_num

                # text #text #text #text #text #text #text #text

                # 01 상단
                # log
                self.log_update.emit(f'쿠팡 [텍스트 상단] 확인 중..')
                main = soup.find('div', class_='prod-atf-main').text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                brief = soup.find('div', id="itemBrief").text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                etc = soup.find('li', class_='product-etc tab-contents__content').text.strip(
                ).replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                check = txt_check(file_name, etc)
                if check == '동서가구':
                    return '동서가구'

                # text #text #text #text #text #text #text #text

                # img #img #img #img #img #img #img #img #img #img

                # 04 이미지
                # log
                self.log_update.emit(f'쿠팡 [이미지 대표이미지] 확인 중..')

                actions = ActionChains(driver)
                actions.send_keys(Keys.HOME).perform()
                img_url = 'https:' + \
                    soup.find('img', class_="prod-image__detail")['src']
                print(img_url)
                ##
                ##
                ##
                check, hight = img_check(img_url)
                if check == '동서가구':
                    pyautogui.screenshot(f'{file_name}.jpg')
                    print(f'{file_name}.jpg')

                    image_file_path = f'{file_name}.jpg'
                    for brand in brand_lists:

                        if brand in file_name:

                            # make bucket and get folder name for each brand
                            bucket = storage.bucket()
                            folder_name = str(
                                list(brand_dicts[brand].keys())[0])
                            folder_blob = bucket.blob(folder_name)

                            # check specific folder name exist or not
                            if not folder_blob.exists():
                                print(f'Creating folder {folder_name}')
                                folder_blob.upload_from_string('')

                            # Upload a file to the folder
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                    return '동서가구'

                # 05 상세페이지
                detail = soup.find('div', id="productDetail")
                imgs = detail.find_all('img')
                print(imgs)
                imgs_cnt = 1
                for img in imgs:
                    # log
                    self.log_update.emit(
                        f'쿠팡 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                    imgs_cnt += 1
                    try:
                        src = img['src']

                        img_url = src
                        ##
                        ##
                        ##
                        check, hight = img_check(img_url)
                        if check == '동서가구':
                            count = 0
                            while count < len(lists):  # len(lists)
                                img_element = driver.find_element(
                                    By.XPATH, f"//img[@src='{img_url}']")
                                print('find img_element')
                                location = img_element.location
                                print(location)

                                script = "document.querySelector('.product-detail-seemore-btn').click();"
                                time.sleep(3)
                                driver.execute_script(script)
                                print(hight)
                                if hight < 50:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*1.7});")
                                elif 50 < hight < 80:
                                    print('here')
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)});")
                                else:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                time.sleep(2)
                                pyautogui.screenshot(f'{file_name}.jpg')
                                image_file_path = f'{file_name}.jpg'

                                for brand in brand_lists:
                                    if brand in file_name:
                                        # make bucket and get folder name for each brand
                                        bucket = storage.bucket()
                                        folder_name = str(
                                            list(brand_dicts[brand].keys())[0])
                                        folder_blob = bucket.blob(folder_name)

                                        # check specific folder name exist or not
                                        if not folder_blob.exists():
                                            print(
                                                f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        # Upload a file to the folder
                                        blob = bucket.blob(
                                            f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(
                                            image_file_path)
                                        print(
                                            f'File {file_name} uploaded to {folder_name}')
                                        break
                                break
                            break
                    except:
                        pass
                return check

                # img #img #img #img #img #img #img #img #img #img

            import datetime
            print('시작', datetime.datetime.now())

            for li in range(start_cnt, len(lists)):
                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)

                lists[li] = lists[li].replace(
                    "'", "").replace("[", "").replace("]", "")

                # log
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')

                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(
                        f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

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



    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

    def run(self):
        # log
        self.log_update.emit(f'firebase 서버 접속')

        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import storage

        # Firebase 서비스 계정의 키 파일 경로
        cred = credentials.Certificate(
            'upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

        # Firebase 프로젝트 ID
        project_id = 'upload-img-5b02f.appspot.com'

        # Firebase 초기화
        firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

        import time
        import socket
        import re
        import requests
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("pwnbit.kr", 443))
        in_ip = sock.getsockname()[0]
        print("내부 IP: ", in_ip)
        req = requests.get("http://ipconfig.kr")
        ex_ip = re.search(
            r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
        print("외부 IP: ", ex_ip)

        start_cnt = 0
        if ex_ip != '183.100.232.2444':

            import csv
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기

            # log
            self.log_update.emit(f'쿠팡 수집 리스트 확인')

            with open('cou_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
                read = csv.reader(f)
                lists = list(read)
            lists = lists[0]
            # print(lists)

            for i in range(len(lists)):
                if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
                    start_cnt = i
                    break

            import getpass
            path_input = getpass.getuser()

            import pytesseract
            import cv2
            # from matplotlib import pyplot as plt
            import urllib.request

            import pyautogui
            from bs4 import BeautifulSoup as bs
            import os
            import urllib3
            import csv
            from PIL import Image
            import sys
            import unittest

            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today',
                           'gmarket', 'auction', 'interpark', 'coupang']

            # save in Firebase
            # save in Firebase
            # save in Firebase
            def to_ascii(string):
                return int(sum([ord(character) for character in string]) / len(brand_lists))

            def get_week_of_month():
                today = datetime.date.today()
                first_day_of_month = datetime.date(today.year, today.month, 1)
                week_number = (today - first_day_of_month).days // 7 + 1
                week_syntax = str(today.month) + '월' + str(week_number) + '주차'

                return week_syntax

            # make dicts
            brand_dicts = {}
            for brand in brand_lists:
                ascii_code = to_ascii(brand)
                brand_dicts[brand] = {ascii_code: []}

            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            def txt_check(file_name, text):
                if text.count("동서가구"):
                    print(text)
                    print("\n\n\n")

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
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                            break

                    return '동서가구'

                else:
                    return

            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            def img_check(url):
                def 이미지확인(url):
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                    urllib.request.urlretrieve(url, "test1.jpg")

                    # log
                    # load the new pixmap
                    new_pixmap = QPixmap('test1.jpg')
                    # emit the custom signal to pass the new pixmap to the main thread
                    self.pixmap_update.emit(new_pixmap)

                    image = cv2.imread(
                        "test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
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

                            if img_width != 640:
                                if hight >= 150:
                                    image_cropped = image[hight -
                                                          150:hight, width:]
                                else:
                                    image_cropped = image[:hight, width:]
                            else:
                                if hight >= 100:
                                    image_cropped = image[hight -
                                                          100:hight, 300:]
                                else:
                                    image_cropped = image[:hight, 300:]

                            text = pytesseract.image_to_string(
                                image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                            print(text)

                            # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                            # plt.show()

                            if hight > (img_hight)*0.9:  # img_hight
                                return '이미지없음', hight
                            elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                                # plt.show()
                                return '동서가구', hight
                    except:
                        pass

                image, img_width, img_hight, width_unit, hight_unit = 이미지확인(
                    url)
                print('test')
                check, hight = 상단글자(image, width_unit,
                                    hight_unit, img_width, img_hight)
                print('hre')

                return check, hight

            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔

            def EA_cou_item_ck(url):

                urllib3.disable_warnings(
                    urllib3.exceptions.InsecureRequestWarning)

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
                chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
                    0]
                driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
                if os.path.exists(driver_path):
                    print(f"chrome driver is installed: {driver_path}")
                else:
                    print(f"install the chrome driver(ver: {chrome_ver})")
                    chromedriver_autoinstaller.install(True)

                # 옵션 - 셀레니움
                options = webdriver.ChromeOptions()
                options.add_argument(
                    "--disable-blink_features=AutomationControlled")
                options.add_experimental_option(
                    "excludeSwitches", ["enable_logging"])
                options.add_argument("no_sandbox")
                options.add_argument("--start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extionsions")
                options.add_experimental_option(
                    "useAutomationExtension", False)
                # options.add_argument("headless")
                options.add_argument("disable-gpu")
                options.add_argument("lang=ko_KR")
                driver = webdriver.Chrome(options=options)
                actions = ActionChains(driver)

                driver.get(url)
                time.sleep(3)
                code = driver.page_source
                soup = bs(code, 'html.parser')

                import datetime
                now = datetime.datetime.now()
                now = now.strftime('%Y%m%d %H%M%S')

                pro_num = url.split('=')[1].split('&')[0]
                file_name = 'coupang'+'_' + \
                    now.split('.')[0].replace('-', '').replace(' ',
                                                               '_').replace(':', '') + '_' + pro_num

                # text #text #text #text #text #text #text #text

                # 01 상단
                # log
                self.log_update.emit(f'쿠팡 [텍스트 상단] 확인 중..')
                main = soup.find('div', class_='prod-atf-main').text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                brief = soup.find('div', id="itemBrief").text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                etc = soup.find('li', class_='product-etc tab-contents__content').text.strip(
                ).replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                check = txt_check(file_name, etc)
                if check == '동서가구':
                    return '동서가구'

                # text #text #text #text #text #text #text #text

                # img #img #img #img #img #img #img #img #img #img

                # 04 이미지
                # log
                self.log_update.emit(f'쿠팡 [이미지 대표이미지] 확인 중..')

                actions = ActionChains(driver)
                actions.send_keys(Keys.HOME).perform()
                img_url = 'https:' + \
                    soup.find('img', class_="prod-image__detail")['src']
                print(img_url)
                ##
                ##
                ##
                check, hight = img_check(img_url)
                if check == '동서가구':
                    pyautogui.screenshot(f'{file_name}.jpg')
                    print(f'{file_name}.jpg')

                    image_file_path = f'{file_name}.jpg'
                    for brand in brand_lists:

                        if brand in file_name:

                            # make bucket and get folder name for each brand
                            bucket = storage.bucket()
                            folder_name = str(
                                list(brand_dicts[brand].keys())[0])
                            folder_blob = bucket.blob(folder_name)

                            # check specific folder name exist or not
                            if not folder_blob.exists():
                                print(f'Creating folder {folder_name}')
                                folder_blob.upload_from_string('')

                            # Upload a file to the folder
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                    return '동서가구'

                # 05 상세페이지
                detail = soup.find('div', id="productDetail")
                imgs = detail.find_all('img')
                print(imgs)
                imgs_cnt = 1
                for img in imgs:
                    # log
                    self.log_update.emit(
                        f'쿠팡 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                    imgs_cnt += 1
                    try:
                        src = img['src']

                        img_url = src
                        ##
                        ##
                        ##
                        check, hight = img_check(img_url)
                        if check == '동서가구':
                            count = 0
                            while count < len(lists):  # len(lists)
                                img_element = driver.find_element(
                                    By.XPATH, f"//img[@src='{img_url}']")
                                print('find img_element')
                                location = img_element.location
                                print(location)

                                script = "document.querySelector('.product-detail-seemore-btn').click();"
                                time.sleep(3)
                                driver.execute_script(script)
                                print(hight)
                                if hight < 50:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*1.7});")
                                elif 50 < hight < 80:
                                    print('here')
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)});")
                                else:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                time.sleep(2)
                                pyautogui.screenshot(f'{file_name}.jpg')
                                image_file_path = f'{file_name}.jpg'

                                for brand in brand_lists:
                                    if brand in file_name:
                                        # make bucket and get folder name for each brand
                                        bucket = storage.bucket()
                                        folder_name = str(
                                            list(brand_dicts[brand].keys())[0])
                                        folder_blob = bucket.blob(folder_name)

                                        # check specific folder name exist or not
                                        if not folder_blob.exists():
                                            print(
                                                f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        # Upload a file to the folder
                                        blob = bucket.blob(
                                            f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(
                                            image_file_path)
                                        print(
                                            f'File {file_name} uploaded to {folder_name}')
                                        break
                                break
                            break
                    except:
                        pass
                return check

                # img #img #img #img #img #img #img #img #img #img

            import datetime
            print('시작', datetime.datetime.now())

            for li in range(start_cnt, len(lists)):
                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)

                lists[li] = lists[li].replace(
                    "'", "").replace("[", "").replace("]", "")

                # log
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')

                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(
                        f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

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

    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

    def run(self):
        # log
        self.log_update.emit(f'firebase 서버 접속')

        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import storage

        # Firebase 서비스 계정의 키 파일 경로
        cred = credentials.Certificate(
            'upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

        # Firebase 프로젝트 ID
        project_id = 'upload-img-5b02f.appspot.com'

        # Firebase 초기화
        firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

        import time
        import socket
        import re
        import requests
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("pwnbit.kr", 443))
        in_ip = sock.getsockname()[0]
        print("내부 IP: ", in_ip)
        req = requests.get("http://ipconfig.kr")
        ex_ip = re.search(
            r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
        print("외부 IP: ", ex_ip)

        start_cnt = 0
        if ex_ip != '183.100.232.2444':

            import csv
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기
            # csv파일 list로 불러오기

            # log
            self.log_update.emit(f'쿠팡 수집 리스트 확인')

            with open('cou_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
                read = csv.reader(f)
                lists = list(read)
            lists = lists[0]
            # print(lists)

            for i in range(len(lists)):
                if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
                    start_cnt = i
                    break

            import getpass
            path_input = getpass.getuser()

            import pytesseract
            import cv2
            # from matplotlib import pyplot as plt
            import urllib.request

            import pyautogui
            from bs4 import BeautifulSoup as bs
            import os
            import urllib3
            import csv
            from PIL import Image
            import sys
            import unittest

            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today',
                           'gmarket', 'auction', 'interpark', 'coupang']

            # save in Firebase
            # save in Firebase
            # save in Firebase
            def to_ascii(string):
                return int(sum([ord(character) for character in string]) / len(brand_lists))

            def get_week_of_month():
                today = datetime.date.today()
                first_day_of_month = datetime.date(today.year, today.month, 1)
                week_number = (today - first_day_of_month).days // 7 + 1
                week_syntax = str(today.month) + '월' + str(week_number) + '주차'

                return week_syntax

            # make dicts
            brand_dicts = {}
            for brand in brand_lists:
                ascii_code = to_ascii(brand)
                brand_dicts[brand] = {ascii_code: []}

            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            # 텍스트 내 '동서가구' 로고 포함 여부 확인
            def txt_check(file_name, text):
                if text.count("동서가구"):
                    print(text)
                    print("\n\n\n")

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
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                            break

                    return '동서가구'

                else:
                    return

            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            # 이미지 내 '동서가구' 로고 포함 여부 확인
            def img_check(url):
                def 이미지확인(url):
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                    urllib.request.urlretrieve(url, "test1.jpg")

                    # log
                    # load the new pixmap
                    new_pixmap = QPixmap('test1.jpg')
                    # emit the custom signal to pass the new pixmap to the main thread
                    self.pixmap_update.emit(new_pixmap)

                    image = cv2.imread(
                        "test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
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

                            if img_width != 640:
                                if hight >= 150:
                                    image_cropped = image[hight -
                                                          150:hight, width:]
                                else:
                                    image_cropped = image[:hight, width:]
                            else:
                                if hight >= 100:
                                    image_cropped = image[hight -
                                                          100:hight, 300:]
                                else:
                                    image_cropped = image[:hight, 300:]

                            text = pytesseract.image_to_string(
                                image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                            print(text)

                            # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                            # plt.show()

                            if hight > (img_hight)*0.9:  # img_hight
                                return '이미지없음', hight
                            elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                                # plt.show()
                                return '동서가구', hight
                    except:
                        pass

                image, img_width, img_hight, width_unit, hight_unit = 이미지확인(
                    url)
                print('test')
                check, hight = 상단글자(image, width_unit,
                                    hight_unit, img_width, img_hight)
                print('hre')

                return check, hight

            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔
            # 쿠팡 개별 상품 스캔

            def EA_cou_item_ck(url):

                urllib3.disable_warnings(
                    urllib3.exceptions.InsecureRequestWarning)

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
                chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
                    0]
                driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
                if os.path.exists(driver_path):
                    print(f"chrome driver is installed: {driver_path}")
                else:
                    print(f"install the chrome driver(ver: {chrome_ver})")
                    chromedriver_autoinstaller.install(True)

                # 옵션 - 셀레니움
                options = webdriver.ChromeOptions()
                options.add_argument(
                    "--disable-blink_features=AutomationControlled")
                options.add_experimental_option(
                    "excludeSwitches", ["enable_logging"])
                options.add_argument("no_sandbox")
                options.add_argument("--start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extionsions")
                options.add_experimental_option(
                    "useAutomationExtension", False)
                # options.add_argument("headless")
                options.add_argument("disable-gpu")
                options.add_argument("lang=ko_KR")
                driver = webdriver.Chrome(options=options)
                actions = ActionChains(driver)

                driver.get(url)
                time.sleep(3)
                code = driver.page_source
                soup = bs(code, 'html.parser')

                import datetime
                now = datetime.datetime.now()
                now = now.strftime('%Y%m%d %H%M%S')

                pro_num = url.split('=')[1].split('&')[0]
                file_name = 'coupang'+'_' + \
                    now.split('.')[0].replace('-', '').replace(' ',
                                                               '_').replace(':', '') + '_' + pro_num

                # text #text #text #text #text #text #text #text

                # 01 상단
                # log
                self.log_update.emit(f'쿠팡 [텍스트 상단] 확인 중..')
                main = soup.find('div', class_='prod-atf-main').text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                brief = soup.find('div', id="itemBrief").text.strip().replace(
                    " ", "").replace("\n", "").replace("\t", "").replace("\r", "")
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
                etc = soup.find('li', class_='product-etc tab-contents__content').text.strip(
                ).replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                check = txt_check(file_name, etc)
                if check == '동서가구':
                    return '동서가구'

                # text #text #text #text #text #text #text #text

                # img #img #img #img #img #img #img #img #img #img

                # 04 이미지
                # log
                self.log_update.emit(f'쿠팡 [이미지 대표이미지] 확인 중..')

                actions = ActionChains(driver)
                actions.send_keys(Keys.HOME).perform()
                img_url = 'https:' + \
                    soup.find('img', class_="prod-image__detail")['src']
                print(img_url)
                ##
                ##
                ##
                check, hight = img_check(img_url)
                if check == '동서가구':
                    pyautogui.screenshot(f'{file_name}.jpg')
                    print(f'{file_name}.jpg')

                    image_file_path = f'{file_name}.jpg'
                    for brand in brand_lists:

                        if brand in file_name:

                            # make bucket and get folder name for each brand
                            bucket = storage.bucket()
                            folder_name = str(
                                list(brand_dicts[brand].keys())[0])
                            folder_blob = bucket.blob(folder_name)

                            # check specific folder name exist or not
                            if not folder_blob.exists():
                                print(f'Creating folder {folder_name}')
                                folder_blob.upload_from_string('')

                            # Upload a file to the folder
                            blob = bucket.blob(
                                f'{folder_name}/{image_file_path}')
                            blob.upload_from_filename(image_file_path)
                            print(
                                f'File {file_name} uploaded to {folder_name}')
                    return '동서가구'

                # 05 상세페이지
                detail = soup.find('div', id="productDetail")
                imgs = detail.find_all('img')
                print(imgs)
                imgs_cnt = 1
                for img in imgs:
                    # log
                    self.log_update.emit(
                        f'쿠팡 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                    imgs_cnt += 1
                    try:
                        src = img['src']

                        img_url = src
                        ##
                        ##
                        ##
                        check, hight = img_check(img_url)
                        if check == '동서가구':
                            count = 0
                            while count < len(lists):  # len(lists)
                                img_element = driver.find_element(
                                    By.XPATH, f"//img[@src='{img_url}']")
                                print('find img_element')
                                location = img_element.location
                                print(location)

                                script = "document.querySelector('.product-detail-seemore-btn').click();"
                                time.sleep(3)
                                driver.execute_script(script)
                                print(hight)
                                if hight < 50:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*1.7});")
                                elif 50 < hight < 80:
                                    print('here')
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)});")
                                else:
                                    driver.execute_script(
                                        f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                time.sleep(2)
                                pyautogui.screenshot(f'{file_name}.jpg')
                                image_file_path = f'{file_name}.jpg'

                                for brand in brand_lists:
                                    if brand in file_name:
                                        # make bucket and get folder name for each brand
                                        bucket = storage.bucket()
                                        folder_name = str(
                                            list(brand_dicts[brand].keys())[0])
                                        folder_blob = bucket.blob(folder_name)

                                        # check specific folder name exist or not
                                        if not folder_blob.exists():
                                            print(
                                                f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        # Upload a file to the folder
                                        blob = bucket.blob(
                                            f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(
                                            image_file_path)
                                        print(
                                            f'File {file_name} uploaded to {folder_name}')
                                        break
                                break
                            break
                    except:
                        pass
                return check

                # img #img #img #img #img #img #img #img #img #img

            import datetime
            print('시작', datetime.datetime.now())

            for li in range(start_cnt, len(lists)):
                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)

                lists[li] = lists[li].replace(
                    "'", "").replace("[", "").replace("]", "")

                # log
                self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')

                check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    lists[li] = [lists[li], '스캔필요']
                    with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')

                    # log
                    self.log_update.emit(
                        f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

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


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread_running = False

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Close', 'Are you sure you want to exit?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 크롬, 크롬드라이버 프로세서 종료
            processes = [p for p in psutil.process_iter(
                ['pid', 'name', 'create_time'])]
            processes_sorted = sorted(
                processes, key=lambda x: x.info['create_time'], reverse=True)

            for process in processes_sorted:
                print(
                    f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")

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
        인터파크.triggered.connect(self.inter)
        옥션.triggered.connect(self.ac)
        지마켓.triggered.connect(self.gma)

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
        self.worker_thread = WorkerThread_cou()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def llst(self):
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
        self.worker_thread = WorkerThread_11st()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def lot(self):
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
        self.worker_thread = WorkerThread_lot()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def ss(self):
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
        self.worker_thread = WorkerThread_ss()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def sin(self):
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
        self.worker_thread = WorkerThread_sin()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def oj(self):
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
        self.worker_thread = WorkerThread_oj()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def interpark(self):
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
        self.worker_thread = WorkerThread_inter()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def auction(self):
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
        self.worker_thread = WorkerThread_auction()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def gmarket(self):
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
        self.worker_thread = WorkerThread_gmarket()
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(
            self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def resetThreadRunning(self):
        self.thread_running = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
