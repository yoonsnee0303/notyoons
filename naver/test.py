#테스트 url - 쿠팡-바스포르 벤더-동서가구 검색

#https://store.coupang.com/vp/vendors/A00037308/products?vendorName=%28%EC%A3%BC%29%EB%B0%94%EC%8A%A4%ED%8F%AC%EB%A5%B4&productId=1668601&outboundShippingPlaceId=

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')
project_id = 'upload-img-5b02f.appspot.com'
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


start_cnt = 0
if ex_ip != '183.100.232.2444':

    import csv
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    with open('nav_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
        read = csv.reader(f)
        lists = list(read)
    lists = lists[0]
    # print(lists)
    print(f'전체 상세페이지 개수: {len(lists)}')

    for i in range(len(lists)):

        if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
            start_cnt = i
            break

    print(f'남은 상세페이지 개수: {len(lists) - start_cnt}')


    import getpass
    path_input = getpass.getuser()


    import pytesseract
    import cv2
    from matplotlib import pyplot as plt
    import urllib.request


    import pyautogui
    from bs4 import BeautifulSoup as bs
    import os
    import urllib3
    import csv
    from PIL import Image
    import sys
    import unittest
    import datetime

    # save in Firebase
    # save in Firebase
    # save in Firebase

    brand_lists = ['11','lotte','sin','naver','today','gmarket','auction','interpark','coupang']

    def to_ascii(string):
        return int(sum([ord(character) for character in string]) / len(brand_lists))
    
    def get_week_of_month():
        today = datetime.date.today()
        first_day_of_month = datetime.date(today.year, today.month, 1)
        week_number = (today - first_day_of_month).days // 7 + 1
        week_syntax = str(today.month) + '월' + str(week_number) + '주차'
    
        return week_syntax


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
            time.sleep(1)
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
                        return '이미지없음',hight
                    elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                        #plt.show()
                        return '동서가구', hight
            except:
                pass


        image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
        check,hight = 상단글자(image, width_unit, hight_unit, img_width, img_hight)
        print(check,hight)

        return check,hight











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
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script('window.scrollTo(0, 0);')
        time.sleep(3)
        code = driver.page_source
        soup = bs(code, 'html.parser')

        # setting file_name
        import datetime
        now = datetime.datetime.now()
        now = now.strftime('%Y%m%d %H%M%S')
        print(url)
        pro_num = url.split('/')[-1]
        file_name = 'naver'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num
        #text #text #text #text #text #text #text #text





        # #01 상단
        main = soup.find('fieldset').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
        print(main)

        check = txt_check(file_name,main)
        if check == '동서가구':
            return '동서가구'
        elif main.count('현재판매중인상품이아닙니다'):
            print("품절 상품 / 패스")
            return


        # #02 하단
        element = driver.find_element(By.CLASS_NAME,"product_info_notice")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        main = soup.find('div', id='INTRODUCE').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
        # print(main)

        check = txt_check(file_name,main)
        if check == '동서가구':
            return '동서가구'
        elif main.count('현재판매중인상품이아닙니다'):
            print("품절 상품 / 패스")
            return

        #text #text #text #text #text #text #text #text



        #img #img #img #img #img #img #img #img #img #img

        #04 메인 이미지
        driver.execute_script('window.scrollTo(0, 0);')
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
        check,hight = img_check(img_url)
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


        #05 상세페이지
        driver.execute_script('window.scrollTo(0, 0);')
        detail = soup.find('div', id='INTRODUCE')
        imgs = detail.find_all('img')
        for img in imgs:
            try:
                src = img['data-src']
                print(src)
                img_url = src
                ##
                ##
                ##
                check,hight = img_check(img_url)
                if check == '동서가구':
                    count = 0
                    while count < len(lists) : 

                        img_element = driver.find_element(By.XPATH, f"//img[@data-src='{img_url}']")
                        location = img_element.location
                        print(location)


                        driver.execute_script("arguments[0].scrollIntoView();", img_element) # {behavior: 'smooth', block: 'start', inline: 'nearest', aligntotop: true}
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
        # driver.quit()
        # if check == '동서가구':
        #     return '동서가구'
        # else:
        #     return

        #img #img #img #img #img #img #img #img #img #img
    start_time = datetime.datetime.now()

    for li in range(start_cnt, len(lists)):
        check = EA_cou_item_ck(lists[li])
        if check == '동서가구':
            lists[li] = [lists[li],'스캔필요']
            #list_test csv파일로 저장
            with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
            end_time = datetime.datetime.now()
            print(f'총 걸린시간: {end_time - start_time}')

        else:
            lists[li] = [lists[li],'패스']
            #list_test csv파일로 저장
            with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
            end_time = datetime.datetime.now()
            print(f'총 걸린시간: {end_time - start_time}')
