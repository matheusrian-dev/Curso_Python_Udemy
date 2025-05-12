'''
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6
QVBoxLayout -> Layout na vertival
QHBoxLayout -> Layout na horizontal
QGridLayout -> Layout baseado em linhas e colunas
'''

from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication()

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 60px')

botao2 = QPushButton('Texto do Botão 2')
botao2.setStyleSheet('font-size: 60px')

botao3 = QPushButton('Texto do Botão 3')
botao3.setStyleSheet('font-size: 60px')

# É possível utilizar o QWidget genérico para receber o layout.
# Porém é importante lembrar que ele não recebe outros widgets
# diretamente!

# Ponto interessante do Grid:
# por padrão row span e column span (span vindo de expansão)
# vem com o valor 1: 1,1,1,1 -> linha, coluna, row span, column span
layout = QGridLayout()
layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 2, 1)

central_widget = QWidget()
central_widget.setLayout(layout)
central_widget.show()

app.exec()
