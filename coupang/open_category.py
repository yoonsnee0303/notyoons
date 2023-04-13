from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import getpass
path_input = getpass.getuser()

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

# 웹페이지 접속
driver.get("https://store.coupang.com/vp/vendors/A00037308/products")

# 전체 페이지 높이를 저장합니다.
page_height = driver.execute_script("return document.body.scrollHeight")
print('done')
# y축을 전체 높이의 1/3까지 내립니다.
scroll_height = page_height // 2.5
driver.execute_script("window.scrollTo(0, {});".format(scroll_height))



import time


ul_elements = driver.find_elements(By.CLASS_NAME, 'scp-component-filter-options__option-items__btn-fold')
for ul_element in ul_elements:
    driver.execute_script("arguments[0].click();", ul_element)
    time.sleep(1.5)
html = driver.page_source
# 파일 쓰기 모드로 열기
with open('html_files.txt', 'w',encoding='utf-8') as f:
    # 파일에 쓸 내용 작성
    f.write(html)












