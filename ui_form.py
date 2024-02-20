# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_anaSayfa(object):
    def setupUi(self, anaSayfa):
        if not anaSayfa.objectName():
            anaSayfa.setObjectName(u"anaSayfa")
        anaSayfa.resize(411, 333)
        self.lineEdit = QLineEdit(anaSayfa)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 100, 113, 24))
        self.radioButton_C = QRadioButton(anaSayfa)
        self.radioButton_C.setObjectName(u"radioButton_C")
        self.radioButton_C.setGeometry(QRect(220, 70, 91, 22))
        self.radioButton_F = QRadioButton(anaSayfa)
        self.radioButton_F.setObjectName(u"radioButton_F")
        self.radioButton_F.setGeometry(QRect(220, 100, 91, 22))
        self.radioButton_K = QRadioButton(anaSayfa)
        self.radioButton_K.setObjectName(u"radioButton_K")
        self.radioButton_K.setGeometry(QRect(220, 130, 91, 22))
        self.pushButton = QPushButton(anaSayfa)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 150, 80, 24))
        self.label_C = QLabel(anaSayfa)
        self.label_C.setObjectName(u"label_C")
        self.label_C.setGeometry(QRect(90, 200, 49, 16))
        self.label_F = QLabel(anaSayfa)
        self.label_F.setObjectName(u"label_F")
        self.label_F.setGeometry(QRect(170, 200, 49, 16))
        self.label_K = QLabel(anaSayfa)
        self.label_K.setObjectName(u"label_K")
        self.label_K.setGeometry(QRect(240, 200, 49, 16))

        self.retranslateUi(anaSayfa)

        QMetaObject.connectSlotsByName(anaSayfa)
    # setupUi

    def retranslateUi(self, anaSayfa):
        anaSayfa.setWindowTitle(QCoreApplication.translate("anaSayfa", u"anaSayfa", None))
        self.radioButton_C.setText(QCoreApplication.translate("anaSayfa", u"C", None))
        self.radioButton_F.setText(QCoreApplication.translate("anaSayfa", u"F", None))
        self.radioButton_K.setText(QCoreApplication.translate("anaSayfa", u"K", None))
        self.pushButton.setText(QCoreApplication.translate("anaSayfa", u"Hesapla", None))
        self.label_C.setText(QCoreApplication.translate("anaSayfa", u"... C", None))
        self.label_F.setText(QCoreApplication.translate("anaSayfa", u"... F", None))
        self.label_K.setText(QCoreApplication.translate("anaSayfa", u"... K", None))
    # retranslateUi

