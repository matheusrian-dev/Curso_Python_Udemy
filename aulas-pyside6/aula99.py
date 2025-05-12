# Introdução ao PySide6

import sys
from PySide6.QtWidgets import QApplication, QLabel

# Testando a Instalação do PySide6
app = QApplication(sys.argv)
label = QLabel("PySide6 está funcionando!")
label.show()
app.exec()
