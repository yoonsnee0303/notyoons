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


start_cnt = 0
if ex_ip != '183.100.232.2444':

    import csv
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    with open('sin_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
        read = csv.reader(f)
        lists = list(read)
    lists = lists[0]
    print(lists[0])
    print(lists)

    for i in range(len(lists)):
        if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
            start_cnt = i
            break

    print(start_cnt)

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
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    import csv
    from PIL import Image
    import sys
    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.by import By


    import datetime
    now = datetime.datetime.now





    #텍스트 내 '동서가구' 로고 포함 여부 확인
    #텍스트 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def txt_check(file_name,text):
        if text.count("동서가구"):
            pyautogui.screenshot(f'{file_name}_text.jpg')
            image_file_path = f'./{file_name}_text.jpg'
            bucket = storage.bucket()
            blob = bucket.blob(f'{file_name}_text.jpg')
            blob.upload_from_filename(image_file_path)
            print(f'File {image_file_path} was uploaded to Firebase Storage.')
            return '동서가구'
        else:
            return None

    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def img_check(url):
        def 이미지확인(url):
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            urllib.request.urlretrieve(url, "test1.png")
            image = cv2.imread("test1.png", cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드
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

                    if img_width != 1100:
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
                    elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구')!= 0:
                        #plt.show()
                        return '동서가구'
            except:
                pass


        image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
        check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)
   

        return check











    #신세계 개별 상품 스캔
    #신세계 개별 상품 스캔
    #신세계 개별 상품 스캔
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

        now = datetime.datetime.now()
        now = now.strftime('%Y%m%d %H%M%S')
        
        file_name = now.split('.')[0].replace('-','').replace(' ','_').replace(':','')

        #text #text #text #text #text #text #text #text 

        #01 상단
        main = soup.find('div', class_='cdtl_row_top').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
        check = txt_check(file_name,main)
        if check == '동서가구':    
            return '동서가구'
        elif main.count('현재판매중인상품이아닙니다'):
            print("품절 상품 / 패스")
            return

        #02 기타 표기 정보 모두
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
            return '동서가구'




        #04 이미지
        elem = soup.find('span', class_='cdtl_imgbox imgzoom')
        img_url = elem.find('img')['src']
        ##
        ##
        ##
        check = img_check(img_url)
        if check == '동서가구':
            return '동서가구'

        #05 상세페이지

        iframes = driver.find_elements(By.TAG_NAME, 'iframe')[1]
        driver.switch_to.frame(iframes)
        time.sleep(1)

        soup = bs(driver.page_source, 'html.parser')
        imgs = soup.find_all('img')

        links = []
        for img in imgs:
            links.append(img["src"])
        print(links)
        print(len(links))
        for link in links:
            try:
                print(link)
                ##
                ##
                ##
                check = img_check(link)
                print(check)
                if check == '동서가구': 
                    count = 0  
                    while count < len(links): #lists
                        # try:
                            img_element = driver.find_element(By.XPATH, f"//img[@src='{link}']")
                            print(img_element)
                            print('find img_element')

                            location = img_element.location
                            print(location)

                            driver.switch_to.default_content()

                            script = "document.getElementsByClassName('btn_collapse ctrl_collapse')[0].click();"
                            driver.execute_script(script)
                            print('done')

                            driver.execute_script(f"window.scrollBy(0, {str(location['y']+2560)});")
                            time.sleep(3)
                            pyautogui.screenshot(f'{file_name}_img.jpg')
                            print('스크린샷 완료')
                            print(f'{file_name}_img.jpg')

                            image_file_path = f'{file_name}_img.jpg'
                            bucket = storage.bucket()
                            blob = bucket.blob(image_file_path) # 저장된 파일의 이름
                            blob.upload_from_filename(image_file_path) # 등록할 파일의 이름
                            print(blob.public_url)
                            print(f'File {image_file_path} was uploaded to Firebase Storage.')
                            count +=1
                            print(count,'번째')

                        # except:
                        #     pass
                            break 
                    break
            
            except:
                pass
        return check
        #img #img #img #img #img #img #img #img #img #img 
    for li in range(start_cnt, len(lists)):
        check = EA_cou_item_ck(lists[li])

        if check == '동서가구':
            lists[li] = [lists[li],'스캔필요']
            with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
            print('스캔필요')
        else:
            lists[li] = [lists[li],'패스']
            #list_test csv파일로 저장
            with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
            print('패스')
