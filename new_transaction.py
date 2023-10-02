# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

import resnewwindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(492, 419)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 139, 63, 255), stop:1 rgba(74, 219, 45, 255));\n"
"font-family: Gotham Pro;")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setMaximumSize(QSize(16777215, 50))
        self.lbl_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"	font-size: 18pt;\n"
"	color: white\n"
"}\n"
"\n"
"QComboBox:item {\n"
"	color: white;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.lbl_date = QDateEdit(self.frame)
        self.lbl_date.setObjectName(u"lbl_date")
        self.lbl_date.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")
        self.lbl_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lbl_date.setDateTime(QDateTime(QDate(2023, 9, 30), QTime(9, 31, 23)))
        self.lbl_date.setMinimumDate(QDate(2023, 9, 30))

        self.verticalLayout.addWidget(self.lbl_date)

        self.lbl_description = QLineEdit(self.frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lbl_description)

        self.lbl_balance = QLineEdit(self.frame)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.cb_2 = QComboBox(self.frame)
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.setObjectName(u"cb_2")
        self.cb_2.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.cb_2)

        self.btn_new_transaction = QPushButton(self.frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"	font-size: 18pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_transaction)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New Transaction", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.lbl_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.lbl_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_2.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_2.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

