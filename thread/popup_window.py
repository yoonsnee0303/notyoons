import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar, QTextEdit, QPushButton, QMessageBox, QDialog
from PyQt5.QtCore import QThread

class WorkerThread(QThread):
    def run(self):
        # 파일 다운로드를 수행하는 작업을 여기에 추가하세요.
        pass

class PopupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Popup Window Example')

    def show_popup(self):
        reply = QMessageBox.question(self, '파일 다운로드', '파일을 다운로드하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 예 버튼을 눌렀을 때 새로운 팝업 창을 열고, 파일 다운로드 진행
            download_dialog = DownloadDialog()
            download_dialog.exec_()
        else:
            print("파일 다운로드를 취소합니다.")

class DownloadDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('다운로드')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        button_layout = QHBoxLayout()

        cancel_button = QPushButton('취소')
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        start_button = QPushButton('시작')
        start_button.clicked.connect(self.start_download)
        button_layout.addWidget(start_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setGeometry(200, 200, 400, 200)

    def start_download(self):
        # 파일 다운로드를 수행하는 함수
        # 여기에 필요한 코드를 추가하세요.
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.download_finished)

    def download_finished(self):
        # 파일 다운로드가 완료되었을 때 수행하는 작업을 추가하세요.
        pass

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Main Application')

        self.popup_window = PopupWindow()
        self.popup_window.show_popup()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
