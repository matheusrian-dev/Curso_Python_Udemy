# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sum_calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 60, 771, 471))
        self.main_grid_layout = QGridLayout(self.gridLayoutWidget)
        self.main_grid_layout.setObjectName(u"main_grid_layout")
        self.main_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.number_2 = QLineEdit(self.gridLayoutWidget)
        self.number_2.setObjectName(u"number_2")
        font = QFont()
        font.setPointSize(30)
        self.number_2.setFont(font)

        self.main_grid_layout.addWidget(self.number_2, 3, 0, 1, 1)

        self.sum_button = QPushButton(self.gridLayoutWidget)
        self.sum_button.setObjectName(u"sum_button")
        self.sum_button.setFont(font)

        self.main_grid_layout.addWidget(self.sum_button, 4, 0, 1, 1)

        self.result_label = QLabel(self.gridLayoutWidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setFont(font)

        self.main_grid_layout.addWidget(self.result_label, 5, 0, 1, 1)

        self.number_1 = QLineEdit(self.gridLayoutWidget)
        self.number_1.setObjectName(u"number_1")
        self.number_1.setFont(font)

        self.main_grid_layout.addWidget(self.number_1, 1, 0, 1, 1)

        self.number_1_label = QLabel(self.gridLayoutWidget)
        self.number_1_label.setObjectName(u"number_1_label")
        self.number_1_label.setFont(font)

        self.main_grid_layout.addWidget(self.number_1_label, 0, 0, 1, 1)

        self.nubmer_2_label = QLabel(self.gridLayoutWidget)
        self.nubmer_2_label.setObjectName(u"nubmer_2_label")
        self.nubmer_2_label.setFont(font)

        self.main_grid_layout.addWidget(self.nubmer_2_label, 2, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 771, 61))
        self.title_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sum_button.setText(QCoreApplication.translate("MainWindow", u"Calcular Soma", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"Resultado da Soma:", None))
        self.number_1_label.setText(QCoreApplication.translate("MainWindow", u"Insira o primeiro n\u00famero:", None))
        self.nubmer_2_label.setText(QCoreApplication.translate("MainWindow", u"Insira o segundo n\u00famero:", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Calculadora - Soma", None))
    # retranslateUi

