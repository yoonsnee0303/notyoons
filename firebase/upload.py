import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f.appspot.com'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

# 업로드할 이미지 파일 경로
image_file_path = './coupang.png'

# Firebase Storage 버킷 객체
bucket = storage.bucket()

# 업로드할 이미지 파일 경로를 지정하여 버킷에 업로드
blob = bucket.blob('coupang.png')
blob.upload_from_filename(image_file_path)
print(f'File {image_file_path} was uploaded to Firebase Storage.')
