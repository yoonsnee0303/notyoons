from PyQt5.QtWidgets import *
import sys
import urllib.request
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt

# app = QApplication(sys.argv)
# label = QLabel("Hello PyQt")
# label.show()
# app.exec_()

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initImageUI()

    def initImageUI(self):

        # menu_bar
        # exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # coupang
        cou_action = QAction(QIcon('coupang.png'), '&coupang', self)
        cou_action.setStatusTip('open application')
        cou_action.triggered.connect(self.test)

        # 11번가
        street_action = QAction(QIcon('11번가.png'), '&11번가', self)
        street_action.setStatusTip('open application')
        street_action.triggered.connect(self.test)

        # gmarket
        g_action = QAction(QIcon('gmarket.png'), '&지마켓', self)
        g_action.setStatusTip('open application')
        g_action.triggered.connect(self.test)

        # Naver
        naver_action = QAction(QIcon('naver.png'), '&네이버', self)
        naver_action.setStatusTip('open application')
        naver_action.triggered.connect(self.test)


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(cou_action)

        # toolbar
        self.setWindowTitle('이미지 표시')
        self.setGeometry(800, 800, 700, 400)
        self.toolbar = self.addToolBar('Exit')
        
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(cou_action)
        self.toolbar.addAction(g_action)
        self.toolbar.addAction(naver_action)
        self.toolbar.addAction(street_action)

        self.test = QLineEdit('line')


            # QHBoxLayout 인스턴스 생성
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        # QVBoxLayout 인스턴스 생성
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.test)
        
        vbox2.addLayout(hbox1)
        vbox2.addLayout(hbox2)

        # vbox2의 배경색을 노란색으로 설정
        vbox2_widget = QWidget()
        vbox2_widget.setStyleSheet("background-color: yellow;")
        vbox2_widget.setLayout(vbox2)

        # 기존 레이아웃 제거
        self.layout().deleteLater()

        # vbox2_widget를 메인 윈도우의 레이아웃으로 설정
        vbox1.addWidget(vbox2_widget)
        self.setLayout(vbox1)

        self.show()


    def test(self):
        print('test')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
