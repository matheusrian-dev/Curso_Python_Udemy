from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_my_widget
import sys


class MyWidget(QWidget, Ui_my_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    app.exec()
