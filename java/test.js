<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Firebase Storage Example</title>
  <style>
    img {
      max-width: 100%;
      height: auto;
    }
  </style>
  <script src="https://www.gstatic.com/firebasejs/8.7.0/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/8.7.0/firebase-storage.js"></script>

  </head>
  <body>
    <h1>Upload an Image</h1>
    <form>
    <input type="file" id="fileInput">
    <button type="button" onclick="uploadFile()">Upload</button>

    </form>
    <h2>카테고리 지정</h2>
    <div id="imageContainer"></div>
    <select>
    <option value="all">전체</option>
    <option value="gmarket">지마켓</option>
    <option value="today">오늘의집</option>
    <option value="auction">옥션</option>
    <option value="coupang">쿠팡</option>
    <option value="sin">신세계</option>
    </select>

    <img id="myImage" src="" alt="Firebase 이미지">
    <script>
    
        const firebaseConfig = {
          apiKey: "AIzaSyB6dMSKarhM1mx-KtqoPhCVuTpxK9bMGuc",
          authDomain: "upload-img-5b02f.firebaseapp.com",
          projectId: "upload-img-5b02f",
          storageBucket: "upload-img-5b02f.appspot.com",
          messagingSenderId: "340480757228",
          appId: "1:340480757228:web:93af1bd1e54d2d13ddc4c9",
          measurementId: "G-MGGHQLGMFJ"
        };
              
        firebase.initializeApp(firebaseConfig);

        var storage = firebase.storage();
        var storageRef = storage.ref();

        // 다운로드할 파일의 참조 가져오기
        var imageRef = storageRef.child('78/auc_20230426_175549_B350773202.jpg');

        // 파일 다운로드 URL 가져오기
        imageRef.getDownloadURL().then(function(url) {

        // 다운로드 URL을 사용하여 이미지 표시
        var img = document.createElement('img');
        img.src = url;
        document.body.appendChild(img);
        }).catch(function(error) {
        console.log('Error downloading image:', error);
        });

    </script>
  </body>
  
</html>
