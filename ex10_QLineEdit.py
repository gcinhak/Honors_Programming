### Example10. QlineEdit ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        vbox = QVBoxLayout()

        self.label = QLabel()

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(100)
        self.line_edit.setPlaceholderText("Enter your text")

        # uncomment this to make read only
        self.readonly_line_edit = QLineEdit()
        self.readonly_line_edit.setReadOnly(True)

        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        vbox.addWidget(self.readonly_line_edit)
        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit)

        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.setWindowTitle("QLineEdit")

    def return_pressed(self):
        print("Return pressed!!!!")
        print(self.line_edit.cursorPosition())
        self.label.setText(self.line_edit.text())

    def editing_finished(self):
        print("Tediting finished...")

    def selection_changed(self):
        print("Selection changed")
        self.label.setText(self.line_edit.selectedText())
        print(self.line_edit.selectedText())

    def text_changed(self, txt):
        print("Text changed...")
        print(txt)

    def text_edited(self, txt):
        print("Text edited...")
        print(txt)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())