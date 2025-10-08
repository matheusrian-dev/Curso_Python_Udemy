# flake8: noqa
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_my_widget(object):
    def setupUi(self, my_widget):
        if not my_widget.objectName():
            my_widget.setObjectName(u"my_widget")
        my_widget.resize(521, 382)
        self.horizontalLayout = QHBoxLayout(my_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")
        self.label_1 = QLabel(my_widget)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(45)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_layout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QLabel(my_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_layout.addWidget(self.label_2, 0, 1, 1, 1)

        self.pushButton_1 = QPushButton(my_widget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        font1 = QFont()
        font1.setPointSize(40)
        self.pushButton_1.setFont(font1)

        self.grid_layout.addWidget(self.pushButton_1, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(my_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.grid_layout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.horizontalLayout.addLayout(self.grid_layout)

        self.retranslateUi(my_widget)

        QMetaObject.connectSlotsByName(my_widget)

    # setupUi

    def retranslateUi(self, my_widget):
        my_widget.setWindowTitle(
            QCoreApplication.translate("my_widget", u"Form", None)
        )
        self.label_1.setText(
            QCoreApplication.translate("my_widget", u"L1", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("my_widget", u"L2", None)
        )
        self.pushButton_1.setText(
            QCoreApplication.translate("my_widget", u"B1", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("my_widget", u"B2", None)
        )

    # retranslateUi
