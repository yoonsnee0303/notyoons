# 서버에서 오류가 발생했습니다

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f.appspot.com'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})
import time

# firebase 파일 리스트 가지고 오기
blobs = storage.bucket().list_blobs()
files = [blob.name for blob in blobs]

find_words = {}
# cou: [], sin: [], int('4'):[]
keys = [k for k in find_words.keys()]

# 신규 폴더 생성 및 파일 이동, 기존 파일 삭제
cnt = 0
temp = []
for file in files:
    bucket = storage.bucket()

    string = file.split('_')[0]
    brand = ''.join(filter(lambda x: not x.isdigit(), string))
    brand_to_ascii = int(sum([ord(spell) for spell in f'{brand}']) / 150)

    # 이동할 파일의 경로와 이름 지정
    ori_file_path = file
    new_file_path = f'coupang/{file}'


    if brand_to_ascii in keys: # coupang
        k = brand_to_ascii + len(keys)
        find_words[k] = []
        find_words[k].append(file)
        print(find_words)
        
        # 이동할 파일의 blob 객체 생성
        # blob = bucket.blob(ori_file_path) 

        # 새로운 경로와 이름으로 blob 객체 복사
        # new_blob = bucket.copy_blob(blob, bucket, new_file_path)

        # 이전 경로에 있는 blob 객체 삭제
        # blob.delete()
        print(file)
        print('쿠팡 복제 및 이동')
        cnt += 1
    
    # elif

    else : 
        k = int(sum([ord(spell) for spell in 'sin']) / 150) 
        temp.append(file)
        find_words[k] = temp
        
        print(find_words)

        # 이동할 파일의 blob 객체 생성
        # blob = bucket.blob(ori_file_path)


        # 새로운 경로와 이름으로 blob 객체 복사
        # new_blob = bucket.copy_blob(blob, bucket, new_file_path)

        # 이전 경로에 있는 blob 객체 삭제
        # blob.delete()

        print(file)
        print('신세계 복제 및 이동')
        cnt += 1
    print(f'{cnt} / {len(files)}')







        
