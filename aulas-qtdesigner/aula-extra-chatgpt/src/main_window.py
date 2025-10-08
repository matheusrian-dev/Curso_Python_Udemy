from PySide6.QtWidgets import QMainWindow, QApplication
from ui_sum_calculator import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sum_button.clicked.connect(self.sum_numbers)

    def sum_numbers(self):
        try:
            first_number = float(self.number_1.text())
            second_number = float(self.number_2.text())
            result = first_number + second_number
            self.result_label.setText(f'O resultado da soma é: {result}')
        except ValueError:
            self.result_label.setText('Insira números válidos.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
