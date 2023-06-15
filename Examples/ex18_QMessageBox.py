import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # About_button
        self.btn_about = QPushButton()
        self.btn_about.setText("About")
        self.btn_about.clicked.connect(self.About_event)

        # Information_button
        self.btn_information = QPushButton()
        self.btn_information.setText("Information")
        self.btn_information.clicked.connect(self.Information_event)

        # Warning_button
        self.btn_warning = QPushButton()
        self.btn_warning.setText("Warning")
        self.btn_warning.clicked.connect(self.Warning_event)

        # Question_button
        self.btn_question = QPushButton()
        self.btn_question.setText("Question")
        self.btn_question.clicked.connect(self.Question_event)

        # Critical_button
        self.btn_critical = QPushButton()
        self.btn_critical.setText("Critical")
        self.btn_critical.clicked.connect(self.Critical_event)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_about)
        hbox.addWidget(self.btn_information)
        hbox.addWidget(self.btn_warning)
        hbox.addWidget(self.btn_question)
        hbox.addWidget(self.btn_critical)

        widget = QWidget(self)
        widget.setLayout(hbox)
        self.setCentralWidget(widget)

    ### Slot 정의 ###
    # About 버튼 클릭 이벤트 slot
    def About_event(self):
        QMessageBox.about(self, 'About Title', 'About Message')

    # Information 버튼 클릭 이벤트 slot
    def Information_event(self):
        buttonReply = QMessageBox.information(
            self, 'Information Title', "Information Message",
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No,
            QMessageBox.Cancel
        )

        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reset clicked.')
        elif buttonReply == QMessageBox.No:
            print('No clicked.')

    # Warning 버튼 클릭 이벤트 slot
    def Warning_event(self):
        buttonReply = QMessageBox.warning(
            self, 'Warning Title', "Warning Message",
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No,
            QMessageBox.Cancel
        )

        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reset clicked.')
        elif buttonReply == QMessageBox.No:
            print('No clicked.')

    # Question 버튼 클릭 이벤트 slot
    def Question_event(self):
        buttonReply = QMessageBox.question(
            self, 'Question Title', "Question Message",
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No,
            QMessageBox.Cancel
        )

        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reset clicked.')
        elif buttonReply == QMessageBox.No:
            print('No clicked.')

    # Critical 버튼 클릭 이벤트 slot
    def Critical_event(self):
        buttonReply = QMessageBox.critical(
            self, 'Critical Title', "Critical Message",
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No,
            QMessageBox.Cancel
        )

        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reset clicked.')
        elif buttonReply == QMessageBox.No:
            print('No clicked.')

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    # print(app.exec_())
    # sys.exit(app.exec_())