# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import getpass
import logging
from io import StringIO

# StringIO 객체 생성
error_buffer = StringIO()

# 로그 설정
logging.basicConfig(stream=error_buffer, level=logging.ERROR)

# 예시
str1 = 'text'

# 에러상황 만들기
try: 
    str1 + 2
except Exception as e:
    # 예외 로그 기록
    logging.exception("예외 발생! ")
    error_logs = error_buffer.getvalue()
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()

    smtp.starttls()

    smtp.login('yoonsnee0303@gmail.com', 'qazyvibmpygpzswl')

    msg = MIMEText(error_logs) # 텍스트 내용
    msg['Subject'] = '붕붕붕 씽씽씽 달리는게 너무좋아' # 제목

    # 다중 이메일 보낼 때
    # list = ['tw04013@naver.com','gijungcpy@gmail.com'] 
    # for mail in list:
    smtp.sendmail('yoonsnee0303@gmail.com', 'yoonsnee0303@gmail.com', msg.as_string()) # 본인한테 메일보내기
    print('send email')

    smtp.quit()
