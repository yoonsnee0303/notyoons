import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f.appspot.com'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

# Firebase Storage 인스턴스 생성
bucket = storage.bucket()

# 버킷의 파일 리스트 가져오기
blobs = bucket.list_blobs()

# 'prefix='images/'   list_blobs() 안에 파라미터로 넣는건데, 폴더 경로 지정할 수 있음.

# 가져온 파일 리스트 출력하기
cnt = 1
for blob in blobs:
    print(blob.name)
    blob.download_to_filename(blob.name)
    cnt += 1
    print(cnt)
