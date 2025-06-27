# Introdução de Classes no PySide6
'''
QMainWindows e centralWidget
-> QApplication (app)
    -> QMainWindow (window -> setCentralWidget)
        -> CentralWidget (central_widget)
            -> Layout (layout)
                -> Widget 1 (botao1)
                -> Widget 2 (botao2)
                -> Widget 3 (botao3)
                etc
    -> show()
-> exec()
'''

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QGridLayout,
    QWidget,
    QMainWindow,
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Primeira Janela')

        # Button
        self.botao1 = self.criar_botao('Botao 1')
        self.botao1.clicked.connect(self.checa_se_esta_marcado)

        self.botao2 = self.criar_botao('Botão 2')

        self.botao3 = self.criar_botao('Botão 3')

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 2, 1, 1, 2)
        self.central_widget.setLayout(self.grid_layout)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mensagem na barra de status')

        # menuBar
        self.menu_bar = self.menuBar()
        self.primeiro_menu = self.menu_bar.addMenu('Primeiro Menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira Ação')
        # Executa algo após a ação for acionada.
        self.primeira_acao.triggered.connect(self.muda_mensagem_status_bar)
        self.segunda_acao = self.primeiro_menu.addAction('Segunda Ação')
        # .setCheckable faz com que a ação seja marcável
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.checa_se_esta_marcado)
        self.segunda_acao.hovered.connect(self.checa_se_esta_marcado)

    @Slot()
    def muda_mensagem_status_bar(self, status_bar):
        status_bar.showMessage('O slot example foi executado.')

    @Slot()
    def checa_se_esta_marcado(self):
        print('Está marcado?', self.segunda_acao.isChecked())

    def criar_botao(self, text):
        botao = QPushButton(text)
        botao.setStyleSheet('font-size: 40px')
        return botao


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
