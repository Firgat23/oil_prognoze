# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forma.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1210, 541)
        self.OilDensity = QTextEdit(Dialog)
        self.OilDensity.setObjectName(u"OilDensity")
        self.OilDensity.setGeometry(QRect(970, 180, 141, 31))
        self.Permeability = QTextEdit(Dialog)
        self.Permeability.setObjectName(u"Permeability")
        self.Permeability.setGeometry(QRect(200, 180, 151, 31))
        self.Porosity = QTextEdit(Dialog)
        self.Porosity.setObjectName(u"Porosity")
        self.Porosity.setGeometry(QRect(10, 180, 151, 31))
        self.Depth = QTextEdit(Dialog)
        self.Depth.setObjectName(u"Depth")
        self.Depth.setGeometry(QRect(390, 180, 151, 31))
        self.Label_2 = QLabel(Dialog)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setGeometry(QRect(200, 150, 161, 16))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(970, 150, 111, 16))
        self.Tectonic = QComboBox(Dialog)
        self.Tectonic.setObjectName(u"Tectonic")
        self.Tectonic.setGeometry(QRect(200, 100, 151, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(580, 150, 161, 16))
        self.Structural = QComboBox(Dialog)
        self.Structural.setObjectName(u"Structural")
        self.Structural.setGeometry(QRect(390, 100, 151, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 60, 111, 31))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(770, 150, 55, 16))
        self.Gross = QTextEdit(Dialog)
        self.Gross.setObjectName(u"Gross")
        self.Gross.setGeometry(QRect(580, 180, 151, 31))
        self.result = QTextEdit(Dialog)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(20, 340, 161, 31))
        self.Lithology = QComboBox(Dialog)
        self.Lithology.setObjectName(u"Lithology")
        self.Lithology.setGeometry(QRect(580, 100, 151, 31))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 300, 101, 31))
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 150, 161, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 70, 111, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 150, 161, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(580, 70, 131, 16))
        self.Netpay = QTextEdit(Dialog)
        self.Netpay.setObjectName(u"Netpay")
        self.Netpay.setGeometry(QRect(770, 180, 161, 31))
        self.Type = QComboBox(Dialog)
        self.Type.setObjectName(u"Type")
        self.Type.setGeometry(QRect(10, 100, 151, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 49, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Label_2.setText(QCoreApplication.translate("Dialog", u"Permeability", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u" Oil Density(for oil)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Gross", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Tectonic regime", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u" Net Pay", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Prediction RF", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"Porosity", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Structural setting", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Depth", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Lithology", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Type", None))
    # retranslateUi

