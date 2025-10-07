from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.change_title_label)

    def change_title_label(self):
        line_text = self.lineEdit.text()
        self.label_titulo.setText(f'Olá {line_text}!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
