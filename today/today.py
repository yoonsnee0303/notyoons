#테스트 url - 쿠팡-바스포르 벤더-동서가구 검색

#https://store.coupang.com/vp/vendors/A00037308/products?vendorName=%28%EC%A3%BC%29%EB%B0%94%EC%8A%A4%ED%8F%AC%EB%A5%B4&productId=1668601&outboundShippingPlaceId=

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

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
ex_ip = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", ex_ip)
# time.sleep(1000)


start_cnt = 0
if ex_ip != '183.100.232.2444':

    import csv
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    with open('o_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
        read = csv.reader(f)
        lists = list(read)
    lists = lists[0]

    for i in range(len(lists)):

        if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
            start_cnt = i
            break

    # print(start_cnt)

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
    brand_lists = ['coupang', 'sin','today']

    # save in Firebase
    # save in Firebase
    # save in Firebase
    def to_ascii(string):
        return int(sum([ord(character) for character in string]) / len(brand_lists))

    #make dicts
    brand_dicts = {}
    for brand in brand_lists:
        ascii_code = to_ascii(brand)
        brand_dicts[brand] = {ascii_code: []}




    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def txt_check(file_name,text):
        if text.count("동서가구"):
            print(text)
            print("\n\n\n")
            pyautogui.screenshot(f'{file_name}_text.jpg')
            image_file_path = f'{file_name}_text.jpg'
            for brand in brand_lists:

                if brand in file_name:

                    #make bucket and get folder name for each brand
                    bucket = storage.bucket()
                    folder_name = str(list(brand_dicts[brand].keys())[0])
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
        else:
            return

    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def img_check(url):
        def 이미지확인(url):
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            urllib.request.urlretrieve(url, "test1.jpg")
            image = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드
            try:
                if image == None:
                    return 0,0,0,0,0
            except:
                pass
            img_width = int(image.shape[1])
            img_hight = int(image.shape[0])

            width_unit = int(round(img_width/100))
            hight_unit = int(round(img_hight/100))

            print(hight_unit)

            if hight_unit == 0:
                urllib.request.urlretrieve(url, "test1.jpg")
                image = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드

                img_width = int(image.shape[1])

                img_hight = int(image.shape[0])

                width_unit = int(round(img_width/100))
                hight_unit = int(round(img_hight/100))
                print('reload image')

            # plt.imshow(image, cmap="gray"), plt.axis("off")
            # plt.show()


            return image, img_width, img_hight, width_unit, hight_unit



        def 상단글자(image, width_unit, hight_unit, img_width, img_hight):
            try:
                if image == 0:
                    return '이미지없음'
            except:
                pass
            
            try:
                width = 0

                print('img_width:', img_width)
                print('img_hight:', img_hight)
                print('width_unit:', width_unit)
                print('hight_unit:', hight_unit)

                for hight in range(width_unit, img_hight, hight_unit):
                    now_hight = (hight/img_hight)*50
                    print(hight)

                        
                    if img_width != 640:
                        if hight >= 150:
                            image_cropped = image[hight-150:hight, width:]
                        else:
                            image_cropped = image[:hight, width:]
                    else :
                        if hight >= 100:
                            image_cropped = image[hight-100:hight, 300:]
                        else:
                            image_cropped = image[:hight, 300:]

                    text = pytesseract.image_to_string(image_cropped, lang='kor').strip().replace(" ", "").replace("\n","")
                    print(text)

                    # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                    # plt.show()

                    if now_hight > 30:
                        return '이미지없음'
                    elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                        #plt.show()
                        return '동서가구'
            except:
                pass
        

        image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
        check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)
        print(check)

        return check











    #오늘의 집 개별 상품 스캔
    #오늘의 집 개별 상품 스캔
    #오늘의 집 개별 상품 스캔
    def EA_cou_item_ck(url):

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


        #옵션 - 셀레니움
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink_features=AutomationControlled")
        options.add_experimental_option("excludeSwitches",["enable_logging"])
        options.add_argument("no_sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extionsions")
        options.add_experimental_option("useAutomationExtension",False)
        #options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)

        driver.get(url)
        time.sleep(3)
        code = driver.page_source
        soup = bs(code, 'html.parser')

        # setting file_name
        # 시간 및 날짜
        import datetime
        now = datetime.datetime.now()
        now = now.strftime('%Y%m%d %H%M%S')
        
        # 상품 번호
        string = url.split('?')[0]
        pro_num = re.sub(r'[^0-9]', '', string)


        file_name = 'today'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num



        #text #text #text #text #text #text #text #text 
        # #01 상단
        main = soup.find('div', 'production-selling-overview container').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
        print(main)
        check = txt_check(file_name,main)
        if check == '동서가구':
            return '동서가구'
        elif main.count('현재판매중인상품이아닙니다'):
            print("품절 상품 / 패스")
            return

        #text #text #text #text #text #text #text #text 



        #img #img #img #img #img #img #img #img #img #img 

        #04 메인 이미지
        img_url = soup.find('img', class_="production-selling-cover-image__entry__image")['src']
        print(img_url)
        ##
        ##
        ##
        check = img_check(img_url)
        if check == '동서가구':
            return '동서가구'


        #05 상세페이지
        detail = soup.find('div', class_="production-selling-description__content")
        imgs = detail.find_all('img')
        
        for img in imgs:
            try:
                src = img['src']
                print(src)
                img_url = src
                ##
                ##
                ##
                check = img_check(img_url)
                print(check)
                if check == '동서가구':
                    count = 0
                    while count < len(lists) : 
                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                        print('find img_element')
                        location = img_element.location
                        print(location)

                        driver.execute_script(f"window.scrollBy(0, {location['y']+550});")
                        time.sleep(3)
                        pyautogui.screenshot(f'{file_name}_img.jpg')
                        print(f'{file_name}_img.jpg')

                        image_file_path = f'{file_name}_img.jpg'
                        for brand in brand_lists:
                            if brand in file_name:

                                #make bucket and get folder name for each brand
                                bucket = storage.bucket()
                                folder_name = str(list(brand_dicts[brand].keys())[0])
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
                        break
                    break
            except:
                pass
        return check       
        #img #img #img #img #img #img #img #img #img #img 

    for li in range(start_cnt, len(lists)):
        check = EA_cou_item_ck(lists[li])
        print(check)
        if check == '동서가구':
            lists[li] = [lists[li],'스캔필요']
            #list_test csv파일로 저장
            with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
        else:
            
            lists[li] = [lists[li],'패스']
            #list_test csv파일로 저장
            with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
