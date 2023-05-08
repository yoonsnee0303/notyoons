from PyQt5.QtWidgets import QFileDialog, QApplication
import firebase_admin
from firebase_admin import credentials, storage


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

import os

import tempfile


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
# print([folder.name for folder in folder_names])
# print(folder_names)

for folder_name in folder_names:
    # folder_name = '135/'
    blobs = bucket.list_blobs(prefix=f'{folder_name}') 
    blob_list = []
    for file in blobs:
        print(file.name)
        blob = bucket.blob(f'{file.name}')
        try:
            blob.download_to_filename(f"{file.name.split('/')[1]}")
            print(f"{file.name.split('/')[1]}")
        except:
            pass
        # blob_list.append(file.name)



