from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow
from typing import cast
import sys

"""
Exemplo do comando para gerar o arquivo .py utilizando o arguivo
.ui:
pyside6-uic aulas-qthread/aula-106/workerui.ui -o
    aulas-qthread/aula-106/workerui.py

Nota importante sobre o arquivo .py criado através do
arquivo .ui:

Evitar ao máximo alterar diretamente no arquivo .py
gerado (no caso dessa aula sendo o window.py), pois
caso recompile o arquivo .ui (mesmo que sem querer),
todas as alterações serão apagadas.
"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.change_title_label)
        self.lineEdit.installEventFilter(self)

    def change_title_label(self):
        line_text = self.lineEdit.text()
        self.label_titulo.setText(f'Olá {line_text}!')

    """
    O eventFilter serve para interceptar eventos específicos (como KeyPress)
    antes que o widget os processe, permitindo realizar ações personalizadas
    ou bloquear o evento.
    """

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            # nesse caso tenho certeza que o tipo é KeyPress
            # então é possível realizar o cast conforme
            # realizado abaixo para evitar o erro de tipagem
            event = cast(QKeyEvent, event)
            text = self.lineEdit.text()
            self.label_titulo.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
