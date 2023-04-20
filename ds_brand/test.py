import schedule
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import 상품리스트_동서식품
import 상품리스트_매일유업
import 상품리스트_KN디지털
import 상품리스트_결합상품

import getpass
path_input = getpass.getuser()

def main():


    from bs4 import BeautifulSoup as bs
    import os
    import time
    import urllib3

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
    from selenium.webdriver.support.ui import WebDriverWait

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
    options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    def get(driver):

        import pandas as pd

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

        if ex_ip != '121.133.167.1622':


            # 고도몰 로그인
            url = 'http://gdadmin.edftr76860385.godomall.com/base/login.php'
            driver.get(url)
            driver.implicitly_wait(5)
            driver.find_element(By.NAME, 'managerId').send_keys('dfgagu')
            time.sleep(0.5)
            driver.find_element(By.NAME, 'managerPw').send_keys('df1051184!@')
            time.sleep(0.5)
            driver.find_element(By.CLASS_NAME, 'btn.btn-black').click()

            # 공급사 선택
            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "menu_order")))
            url = 'http://gdadmin.edftr76860385.godomall.com/order/order_list_all.php?view=orderGoods&'
            driver.get(url)
            driver.implicitly_wait(5)

            driver.find_element(
                By.XPATH, '//*[@id="frmSearchOrder"]/div[2]/table/tbody[1]/tr[1]/td/input').click()
            time.sleep(0.5)

            elem = driver.find_elements(
                By.CLASS_NAME, 'pagination.pagination-sm')[1]
            lis = elem.find_elements(By.TAG_NAME, 'li')

            url_add = 'http://gdadmin.edftr76860385.godomall.com/order/order_list_all.php?detailSearch=n&scmFl=1'
            for page in range(1, len(lis)+1):
                if page != 1:
                    driver.find_element(
                        By.XPATH, f'//*[@id="layer-wrap"]/div[2]/nav/ul/li[{str(page)}]/a').click()
                    time.sleep(1)

                table2 = driver.find_elements(
                    By.CLASS_NAME, 'table.table-rows')[1]
                labels = table2.find_elements(By.TAG_NAME, 'label')
                for label in labels:
                    if label.text.count('동서가구') == 0:
                        label_no = label.get_attribute('for')
                        label_no = '&scmNo[]=' + \
                            re.sub(r'[^0-9]', '', label_no)
                        label_temp = label.text
                        label_temp = label_no + '&scmNoNm[]=' + \
                            label_temp.replace(" ", "+")
                        url_add = url_add + label_temp

            # setting url
            now = datetime.now()
            today = now.strftime("%Y") + "-" + \
                now.strftime("%m") + "-" + now.strftime("%d")
            month = now - relativedelta(months=3)
            month3 = month.strftime(
                "%Y") + "-" + month.strftime("%m") + "-" + month.strftime("%d")
            data_EA = 5000

            url_add = url_add + \
                f'''&key[]=o.orderNo&keyword[]=&key[]=o.orderNo&keyword[]=&key[]=o.orderNo&keyword[]=&goodsKey=og.goodsNm&goodsNo=&goodsText=&treatDateFl=og.regDt&searchPeriod=89&treatDate[]={month3}&treatTime[]=00:00:00&treatDate[]={today}&treatTime[]=23:59:59&orderTypeFl[]=&orderChannelFl[]=&orderStatus[]=&settleKind[]=&invoiceCompanySno=0&invoiceNoFl=&orderMemoCd=&memFl=&settlePrice[]=&settlePrice[]=&receiptFl=&overDepositDay=&underDeliveryDay=&sort=og.orderNo+desc&pageNum={data_EA}&view=orderGoods&searchFl=y&applyPath=/order/order_list_all.php?view=orderGoods'''

            # 동서가구 제외 브랜드 3개월치 검색
            driver.get(url_add)
            driver.implicitly_wait(5)

            # 자료 들고오기
            table = driver.find_element(
                By.CLASS_NAME, 'table-responsive').get_attribute('innerHTML')
            return driver, table

    def pros(driver, htmll):
        import csv
        from bs4 import BeautifulSoup as bs
        import time

        soup = bs(htmll, 'html.parser')
        th = soup.find_all('th')

        # title 제어
        pass_title = ['교환', '환불', '반품']
        pass_state = ['중단', '환불', '실패', '취소', '반품']
        replace_words = ['무료배송', '의자BEST', '땡처리특가', '가격인하특가', 'MD추천', '무료배송 특가', '/낱개선택', '/무료배송','제주도배송','동서특가', '설연휴특가', '원데이특가', '원데이행사', '브랜드위크', '동서가구 단독/쿠폰다운', '주말특가', '주말 특가', '위클리딜', '식탁생활', '소파마켓', '[']

        # 자료
        lists = []
        lists_1 = []
        lists_2 = []

        tbody = soup.find('tbody')
        tr = tbody.find_all('tr', class_='text-center')

        for trs in tr:

            # 날짜
            date = trs.find('td', class_='font-date nowrap').text.strip()[:10]

            # 시간
            ttime = trs.find('td', class_='font-date nowrap').text.strip()[10:]

            # 주소
            url = trs.find('td', class_='text-left').find('a')['href']

            # 이미지
            img = trs.find('td', class_='text-left').find('img')['src']

            # 상품명
            title = trs.find(
                'a', class_='one-line bold mgb5').text.replace('\n', '')

            # replace_word1
            title = title.replace("]", " ")

            while True:
                title = title.replace('  ', ' ')
                if title.count('  ') == 0:
                    break

            # replace_words2
            for rps in replace_words:
                title = title.replace(rps, '')
            title = title.strip()

            # 동서식품 상품리스트
            for items in 상품리스트_동서식품.itme_list:
                if title.count(items) > 0:
                    title = '동서식품 ' + title

            # 매일유업 상품리스트
            for items in 상품리스트_매일유업.itme_list:
                if title.count(items) > 0:
                    title = '매일유업 ' + title

            # KN디지털 상품리스트
            for items in 상품리스트_KN디지털.itme_list:
                if title.count(items) > 0:
                    title = 'KN디지털 ' + title

            # 결합상품 상품리스트
            for items in 상품리스트_결합상품.itme_list:
                if title.count(items) > 0:
                    title = '결합상품 ' + title

            # 금지어확인1
            ck_code1 = False
            for ck in pass_title:
                if title.count(ck) > 0:
                    ck_code1 = True
                    break

            # 처리상태
            td = trs.find_all('td')
            for tds in td:
                try:
                    stateT = tds.find('div')
                    if stateT['title'] == '주문 상품별 주문 상태':
                        state = stateT.text
                except:
                    pass

            # 금지어확인2
            ck_code2 = False
            for ck in pass_state:
                if state.count(ck) > 0:
                    ck_code2 = True
                    break

            if ck_code1 == False and ck_code2 == False:

                # 개별 상품명 컨트롤
                if title.count("낮은 틈새 베란다 거실") > 0 or title.count("800블라인드") > 0 or title.count("팬트리장 속 깊은 냉장고") > 0:
                    title = '도아르 ' + title
                elif title.count("슈가 주방 상하") > 0 or title.count("하이브리드 1인가구 멀티옷장") > 0:
                    title = '코코미 ' + title

                # 업체명
                cpy = title
                cpy = cpy.split(' ')[0]

                # 상품명에서 업체명 제거
                title = title.replace(cpy, '').strip()

                # 옵션명
                try:
                    opt = trs.find(
                        'div', class_='option_info').text.replace('\n', '')
                    while True:
                        opt = opt.replace('  ', ' ')
                        if opt.count('  ') == 0:
                            break
                except:
                    opt = ' '
                
                # 주문수
                cnt = trs.find('td', class_='goods_cnt').text

                # 상품가
                td = trs.find_all('td')
                for tds in td:
                    if tds.text.count('0원') > 0:
                        price = tds.text.replace('원', '').replace(',', '')
                        break

                # save temp
                temp = []
                temp.append(date)
                temp.append(cpy)
                temp.append(f'{img}#{url}')
                temp.append(f'{title}#{opt}')
                temp.append(cnt)
                temp.append(price)
                temp.append(state)
                temp.append(ttime)

                # save lists
                lists.append(temp)





        # 콤마 제거
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                lists[i][j] = lists[i][j].replace(', ', '_').replace(',', '')


        # 가구 (구분) 그 외
        except_cpy = ['동서식품', '매일유업', '이지드롭', 'KN디지털']
        for i in range(len(lists)):
            except_cnt = 0
            for j in range(len(except_cpy)):
                if lists[i].count(except_cpy[j])>0:
                    except_cnt += 1
            if except_cnt > 0:
                lists_1.append(lists[i])
            else:
                if lists[i][1] == "매트리스" or lists[i][1] == "서라운드" or lists[i][1] == "전신거울도어":
                    lists[i][3] = lists[i][1] + " " + lists[i][3]
                    lists[i][1] = lists[i-1][1]
                lists_2.append(lists[i])


        print('here to next')
        print('here to next')
        print('here to next')


        # setting_url2
        # 결합상품 
        now = datetime.now()
        today = now.strftime("%Y") + "-" + \
                now.strftime("%m") + "-" + now.strftime("%d")
        data_EA = 5000

        month = now - relativedelta(months=3)
        month3 = month.strftime("%Y") + "-" + month.strftime("%m") + "-" + month.strftime("%d")

        url_add = 'http://gdadmin.edftr76860385.godomall.com/order/order_list_all.php?detailSearch=n&scmFl=all'
        url_add = url_add + \
        f'''&key[]=o.orderNo&keyword[]=&key[]=o.orderNo&keyword[]=&key[]=o.orderNo&keyword[]=&goodsKey=og.goodsNm&goodsNo=&goodsText=결합상품&treatDateFl=og.regDt&searchPeriod=89&treatDate[]={month3}&treatTime[]=00:00:00&treatDate[]={today}&treatTime[]=23:59:59&orderTypeFl[]=&orderChannelFl[]=&orderStatus[]=&settleKind[]=&invoiceCompanySno=0&invoiceNoFl=&orderMemoCd=&memFl=&settlePrice[]=&settlePrice[]=&receiptFl=&overDepositDay=&underDeliveryDay=&sort=og.orderNo+desc&pageNum={str(data_EA)}&view=orderGoods&searchFl=y&applyPath=/order/order_list_all.php?view=orderGoods'''
        print(url_add)

        # 검색
        driver.get(url_add)
        driver.implicitly_wait(5)

        # 자료 들고오기
        htmll = driver.find_element(By.CLASS_NAME, 'table-responsive').get_attribute('innerHTML')
        
        soup = bs(htmll, 'html.parser')
        th = soup.find_all('th')

        tbody = soup.find('tbody')
        tr = tbody.find_all('tr', class_='text-center')

        pass_title = ['교환', '환불', '반품']
        pass_state = ['중단', '환불', '실패', '취소', '반품']

        for trs in tr: 
            # 날짜
            date = trs.find('td', class_='font-date nowrap').text.strip()[:10]

            # 시간
            ttime = trs.find('td', class_='font-date nowrap').text.strip()[10:]

            # 주소
            url = trs.find('td', class_='text-left').find('a')['href']

            # 이미지
            img = trs.find('td', class_='text-left').find('img')['src']

            # 상품명
            title = trs.find(
                'a', class_='one-line bold mgb5').text.replace('\n', '')

            # replace_word1
            title = title.split(' ')[0].replace("]", " ").replace("[","")

            while True:
                title = title.replace('  ', ' ')
                if title.count('  ') == 0:
                    break


            # 금지어확인1
            ck_code1 = False
            for ck in pass_title:
                if title.count(ck) > 0:
                    ck_code1 = True
                    break

            # 처리상태
            td = trs.find_all('td')
            for tds in td:
                try:
                    stateT = tds.find('div')
                    if stateT['title'] == '주문 상품별 주문 상태':
                        state = stateT.text
                except:
                    pass
            # 금지어확인2
            ck_code2 = False
            for ck in pass_state:
                if state.count(ck) > 0:
                    ck_code2 = True
                    break


            if ck_code1 == False and ck_code2 == False:

                # 처리상태
                td = trs.find_all('td')

                for tds in td: 
                    # 상품 상태
                    state = soup.find('div', {'title': '주문 상품별 주문 상태'}).text.strip()

                    # 업체명
                    cpy = title

                    # 옵션명
                    try:
                        opt = trs.find(
                            'div', class_='option_info').text.replace('\n', '')
                        while True:
                            opt = opt.replace('  ', ' ')
                            if opt.count('  ') == 0:
                                break
                    except:
                        opt = ' '

                    # 주문수
                    cnt = trs.find('td', class_='goods_cnt').text

                    # 상품가
                    td = trs.find_all('td')
                    for tds in td: #td
                        if tds.text.count('0원') > 0:
                            price = tds.text.replace('원', '').replace(',', '')
                            break

                    # save temp
                    temp = []
                    temp.append(date)
                    temp.append(cpy)
                    temp.append(f'{img}#{url}')
                    temp.append(f'{title}#{opt}')
                    temp.append(cnt)
                    temp.append(price)
                    temp.append(state)
                    temp.append(ttime)

                    # save lists
                    lists.append(temp)
                    lists_1.append(temp)


        # setting date
        for i in range(len(lists)):
            if int(lists[i][7][:2]) >= 17 and int(lists[i][7][:2]) <= 23:
                cal_date = (datetime.strptime(
                    lists[i][0], '%Y-%m-%d') + timedelta(days=1)).strftime("%Y-%m-%d")
                lists[i].append(lists[i][0])
                lists[i][0] = cal_date
            else:
                lists[i].append(lists[i][0])
            


        # list_test csv파일로 저장
        with open('brand.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows(lists)

        # list_test csv파일로 저장
        with open('brand_1.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows(lists_1)

        # list_test csv파일로 저장
        with open('brand_2.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows(lists_2)



    
    def ftp_trans():

        import ftplib
        try:
            url = 'http://priceflow.co.kr'
            dir = '/html/ds/df/br/'
            session = ftplib.FTP()
            session.connect('112.175.185.27', 21)
            session.encoding = 'utf-8'
            session.login("dailyroutine85", "dpg85kjp#")
            session.cwd(dir)

            uploadFiles = ['brand.csv', 'brand_1.csv', 'brand_2.csv', 'index.html', 'index_1.html', 'index_2.html', 'index_all.html']
            for files in uploadFiles:
                with open(file=files, mode='rb') as wf:
                    session.storbinary(f'STOR {files}', wf)
            print('try')
        except Exception as e:
            print('error')
            print(e)
            print('except')


    # Main
    # Main
    # Main

    while True:
        try:
            driver, htmll= get(driver)
            pros(driver, htmll) 
            ftp_trans()
            break
        except:
            pass

main()

# step3.실행 주기 설정
schedule.every(1).hours.do(main)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
    print('done')
