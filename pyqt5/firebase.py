from PyQt5.QtWidgets import QFileDialog, QApplication
import firebase_admin
from firebase_admin import credentials, storage


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

import os

# 전체 폴더명 가지고 오기
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

project_id = 'upload-img-5b02f.appspot.com'

firebase_admin.initialize_app(cred)

bucket = storage.bucket(project_id)

blobs = bucket.list_blobs() #prefix=folder_name

folder_names = set()
for blob in blobs:
    folder_names.add(blob.name.split('/')[0])
folder_names = list(folder_names)
# print(folder_names)
# print(len(folder_names))


# 특정 폴더 내에서 가지고 오기 ('249', '181', '110', '19', '53', '78', '135')

from PIL import Image
for folder_name in folder_names:
    folder_name = '135/'
    blobs = bucket.list_blobs(prefix=f'{folder_name}') 
    
    file_list = []
    for file in blobs:
        file_list.append(file)
    print(folder_name,len(file_list))
    
# Extract image path from the first file in the file list
image_path = 'upload-img-5b02f.appspot.com/135/' + str(file_list[0]).split(',')[1].split('/')[1]
#'gs://'
    
# Download image data from Firebase Storage
blob = bucket.blob(image_path)

# Download image from Firebase Storage to a file
blob.download_to_filename(image_path)

# Open the downloaded image using Pillow
img = Image.open(image_path)

# Display the image
img.show()




# # PyQt에서 파일 다이얼로그 열기
# app = QApplication([])
# dialog = QFileDialog()
# dialog.setFileMode(QFileDialog.ExistingFile)
# if dialog.exec_() == QFileDialog.Accepted:
#     selected_file = dialog.selectedFiles()[0]
#     # Firebase에서 파일 다운로드
#     blob = bucket.blob("./78/")
#     blob.download_to_filename(selected_file)

