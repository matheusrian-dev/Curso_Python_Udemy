'''
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6
'''

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 40px')
# Adiciona o Widget na Hierarquia e exibe a janela
botao.show()

# Gerar 2 objetos como 2 buttons gera duas janelas separadas
# uma para cada button.
# botao2 = QPushButton('Botão 2')
# botao2.show()

app.exec()
