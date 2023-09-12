import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup
# import numpy as np
import pandas as pd
import os
import datetime


##### 메인윈도우
class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)

        ##### 메인화면 꾸미기 함수 실행
        self.initUi()

        ##### 위젯클래스 메인윈도우의 센터에 셋팅
        self.mywidget = Widgets(self)
        self.setCentralWidget(self.mywidget)

    ##### 메인화면 꾸미기
    def initUi(self):
        self.setWindowTitle("naver news")
        self.setGeometry(300, 300, 700, 300)


##### 위젯영역
##########################################################################################################
class Widgets(QWidget):
    def __init__(self, parent):
        super(Widgets, self).__init__(parent)

        ##### 위젯 함수 실행
        self.initWidget()

        ##### 검색버튼 클릭시 serch함수 실행
        self.search_button.clicked.connect(self.search)

        ##### 저장버튼 클릭시 save_to_file함수 실행
        self.save_button.clicked.connect(self.save_to_file)

    ##### 위젯셋팅
    def initWidget(self):
        ##### 검색어라벨
        self.label = QLabel("검색어 :", self)

        ##### 라인에디트, 검색어 입력용도
        self.lineedit = QLineEdit(self)

        ##### 텍스트브라우저
        self.textedit = QTextBrowser(self)
        self.textedit.setOpenExternalLinks(True)
        self.textedit.setAcceptRichText(True)

        ##### 문자앞에 &표시는 단축키를 지정함, 단축키는 Alt + S
        ##### 버튼에 텍스트를 입력하지 않고 생성만 한후 setText('&Search')로 지정해도 됨
        self.search_button = QPushButton('&Search', self)

        ##### 검색결과를 띄우는 창위에 라벨하나 추가해서 검색어 띄우기
        self.search_label = QLabel(self)

        ##### 검색결과를 저장하는 매체를 체크박스로 선택
        self.save_check1 = QCheckBox('&xlsx', self)
        self.save_check2 = QCheckBox('&csv', self)
        self.save_check3 = QCheckBox('&txt', self)

        self.groupcheck = QButtonGroup(self)
        self.groupcheck.addButton(self.save_check1)
        self.groupcheck.addButton(self.save_check2)
        self.groupcheck.addButton(self.save_check3)

        ##### 체크박스를 선택 후 저장버튼 클릭
        self.save_button = QPushButton('Sa&ve', self)

        ############# 레이이아웃
        ##########################################################################################################

        ##### 그룹박스는 자체가 라벨을 가진 위젯으로 레이아웃 자체를 묶어줄수는 없다
        ##### 다만 레이아웃되어있는것을 그룹박스레이아웃에 넣어줘서 라벨을가진 UI를 꾸며줄수 있다.
        ##### 따라서 그룹박스안에 넣기 전에 묶고자 하는 레이아웃끼리 박스로 묶은뒤에 마지막에 그룹박스를 사용한다.
        ##### 주의해야할점은 각각 배치시킬때 사용하는 메서드가 다르다는 점이다.
        ##### addWidget : 위젯을 박스레이아웃에 넣을때 사용(그룹박스위젯을 레이아웃안에 배치할때도 사용)
        ##### addLayout : 박스레이아웃을 다른 박스레이아웃에 넣을때 사용
        ##### setLayout : 박스레이아웃을 그룹박스위젯에 넣을때 사용

        groupbox1 = QGroupBox('네이버 뉴스 검색')  # 그룹박스 생성

        group_boxlayout1 = QVBoxLayout()  # 그룹박스에 넣기 전에 두개의 박스를 묶어줄 새로운박스 생성

        boxlayout1 = QHBoxLayout()  # 첫번째 박스
        boxlayout1.addWidget(self.label)
        boxlayout1.addWidget(self.lineedit)
        boxlayout1.addWidget(self.search_button)

        boxlayout2 = QVBoxLayout()  # 두번째 박스
        boxlayout2.addWidget(self.search_label)
        boxlayout2.addWidget(self.textedit)

        group_boxlayout1.addLayout(boxlayout1)  # 첫번째 박스를 묶음박스에 넣음(이때 메서드는 addLayout을 사용)
        group_boxlayout1.addLayout(boxlayout2)

        groupbox1.setLayout(group_boxlayout1)  # 박스를 그룹박스에 넣음(이때 메서드는 setLayout을 사용)

        groupbox3 = QGroupBox('네이버 뉴스 검색 결과 저장')
        boxlayout3 = QHBoxLayout()
        boxlayout3.addWidget(self.save_check1)
        boxlayout3.addWidget(self.save_check2)
        boxlayout3.addWidget(self.save_check3)
        boxlayout3.addWidget(self.save_button)
        groupbox3.setLayout(boxlayout3)

        layouts = QVBoxLayout()
        layouts.addWidget(groupbox1)  # 그룹박스를 박스레이아웃에 넣을 땐 addWidget사용(이유는 그룹박스 자체가 위젯이기때문)
        layouts.addStretch(1)
        layouts.addWidget(groupbox3)

        self.setLayout(layouts)

    ##########################################################################################################

    ##### 기능영역
    ##########################################################################################################

    ##### 네이버뉴스 검색 실행
    def search(self):

        ##### 처음시작할때 기존에 검색했던것 삭제, 검색했던부분을 두고 계속적으로 검색하려면 주석처리
        self.textedit.clear()

        self.keyword = self.lineedit.text()
        url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}".format(self.keyword)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        myurls = soup.find_all('a', attrs={'class':'news_tit'})

        ##### 텍스트만 뽑아서 데이타프레임에 담기(나중에 저장매체에 저장할때 사용할예정)
        myurls_text = []
        for myurl in myurls:
            myurls_text.append(myurl.attrs['title'])
            myurls_text.append(myurl.attrs['href'])

        self.news_search = pd.DataFrame(myurls_text, columns=None)

        ##### 리스트형태를 없애고 텍스트브라우저에 결과값 띄우기
        for num, myurl in enumerate(myurls):
            myurls_text = myurl.attrs['title']
            myurls_url = myurl.attrs['href']

            ##### 텍스트브라우저에 검색결과 띄우기
            self.textedit.append(
                str(num + 1) + '. ' + myurls_text + ' (' + '<a href="' + myurls_url + '">Link</a>' + ')')

        ##### 검색을 완료 했음으로 검색어를 입력한 라인에디트의 텍스트 삭제
        self.lineedit.clear()

        ##### 무엇을 검색했는지 알려주기 위해 라벨로 표시 해줌
        self.search_label.setText('{} 검색 결과 :'.format(self.keyword))

        return self.keyword, self.news_search

    ##### 저장매체 체크박스에 따라 각각의 저장매체 실행 함수로 연결
    def save_to_file(self):

        ##### 폴더생성하기
        path = os.getcwd()
        now = datetime.datetime.now()
        folder_name = '{}{}{}_{}시{}분{}초_뉴스수집'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        folder_path = path + '/' + folder_name + '/'
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

        ##### 체크박스 상태에 따라서 저장매체 바뀜
        if self.save_check1.isChecked() == True:
            self.news_search.to_excel(folder_path + '검색어({})뉴스수집.xlsx'.format(self.keyword), index=False, header=None)
            self.save_check1.click()  # 완료 후 클릭된것을 해제하기 위해 한번더 클릭
        if self.save_check2.isChecked() == True:
            self.news_search.to_csv(folder_path + '검색어({})뉴스수집.csv'.format(self.keyword), index=False, header=None,
                                    sep="\t", encoding='utf-8-sig')
            self.save_check2.click()
        if self.save_check3.isChecked() == True:
            self.news_search.to_csv(folder_path + '검색어({})뉴스수집.txt'.format(self.keyword), index=False, header=None,
                                    sep="\t")
            self.save_check3.click()


############################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = Mainwindow()
    mywindow.show()
    app.exec_()