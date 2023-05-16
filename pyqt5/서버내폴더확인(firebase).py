
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage
import os
import datetime

def get_week_of_month(date):
    first_day = date.replace(day=1)
    adjusted_day = first_day + datetime.timedelta(days=(6 - first_day.weekday()))
    week_number = (date - adjusted_day).days // 7 + 2
    return week_number


# Firebase 인증 정보 설정
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}.appspot.com'})

# Firebase Storage 인스턴스 생성
bucket = firebase_storage.bucket()

blobs = bucket.list_blobs()


# 현재 날짜 구하기
current_date = datetime.date.today()

# 현재 월의 주차와 월 출력
week_of_month = get_week_of_month(current_date)
month = current_date.strftime("%m월")
date = month + week_of_month

origin = []
for blob in blobs:
    print(blob.name)
    folder_name = blob.name.split('/')[0]
    origin.append(folder_name)
origin = set(origin) # 중복제거
if date in origin:
    print('true')
