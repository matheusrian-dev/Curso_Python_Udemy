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

from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QGridLayout,
    QWidget,
    QMainWindow,
)

app = QApplication()
window = QMainWindow()
layout = QGridLayout()


def slot_example(status_bar):
    status_bar.showMessage('O slot example foi executado.')


# Button
botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 40px')

botao2 = QPushButton('Texto do Botão 2')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('Texto do Botão 3')
botao3.setStyleSheet('font-size: 40px')

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem na barra de status')

# menuBar
menu_bar = window.menuBar()
primeiro_menu = menu_bar.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira Ação')
# Executa algo após a ação for acionada.
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Segunda Ação')
# .setCheckable faz com que a ação seja marcável
segunda_acao.setCheckable(True)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)

central_widget = QWidget()
central_widget.setLayout(layout)

window.setCentralWidget(central_widget)
window.setWindowTitle('Primeira Janela')
window.show()

app.exec()
