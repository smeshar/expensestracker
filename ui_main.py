# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(898, 739)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 139, 63, 255), stop:1 rgba(74, 219, 45, 255));\n"
"font-family: Gotham Pro;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_balance = QLabel(self.balance_frame)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.balance = QLabel(self.balance_frame)
        self.balance.setObjectName(u"balance")
        self.balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icn_income = QLabel(self.balance_frame)
        self.icn_income.setObjectName(u"icn_income")
        self.icn_income.setMaximumSize(QSize(24, 16777215))
        self.icn_income.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icn_income.setPixmap(QPixmap(u":/icons/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.icn_income)

        self.lbl_income = QLabel(self.balance_frame)
        self.lbl_income.setObjectName(u"lbl_income")
        self.lbl_income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.lbl_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.income = QLabel(self.balance_frame)
        self.income.setObjectName(u"income")
        self.income.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.income)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icn_outcome = QLabel(self.balance_frame)
        self.icn_outcome.setObjectName(u"icn_outcome")
        self.icn_outcome.setMaximumSize(QSize(24, 16777215))
        self.icn_outcome.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icn_outcome.setPixmap(QPixmap(u":/icons/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.icn_outcome)

        self.lbl_outcome = QLabel(self.balance_frame)
        self.lbl_outcome.setObjectName(u"lbl_outcome")
        self.lbl_outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.lbl_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.outcome = QLabel(self.balance_frame)
        self.outcome.setObjectName(u"outcome")
        self.outcome.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.outcome)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.lbl_categories = QLabel(self.categories_frame)
        self.lbl_categories.setObjectName(u"lbl_categories")
        self.lbl_categories.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.lbl_categories)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icn_groceries = QLabel(self.categories_frame)
        self.icn_groceries.setObjectName(u"icn_groceries")
        self.icn_groceries.setMaximumSize(QSize(24, 16777215))
        self.icn_groceries.setStyleSheet(u"background-color: none;\n"
"border:none;\n"
"")
        self.icn_groceries.setPixmap(QPixmap(u":/icons/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icn_groceries)

        self.lbl_groceries = QLabel(self.categories_frame)
        self.lbl_groceries.setObjectName(u"lbl_groceries")
        self.lbl_groceries.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none\n"
"")

        self.horizontalLayout_5.addWidget(self.lbl_groceries)

        self.groceries = QLabel(self.categories_frame)
        self.groceries.setObjectName(u"groceries")
        self.groceries.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"border: none\n"
"")

        self.horizontalLayout_5.addWidget(self.groceries)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_entertainment_2 = QLabel(self.categories_frame)
        self.lbl_entertainment_2.setObjectName(u"lbl_entertainment_2")
        self.lbl_entertainment_2.setMaximumSize(QSize(24, 16777215))
        self.lbl_entertainment_2.setStyleSheet(u"background-color: none;\n"
"border:none;\n"
"")
        self.lbl_entertainment_2.setPixmap(QPixmap(u":/icons/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.lbl_entertainment_2)

        self.lbl_entertainment = QLabel(self.categories_frame)
        self.lbl_entertainment.setObjectName(u"lbl_entertainment")
        self.lbl_entertainment.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none\n"
"")

        self.horizontalLayout_4.addWidget(self.lbl_entertainment)

        self.entertainment = QLabel(self.categories_frame)
        self.entertainment.setObjectName(u"entertainment")
        self.entertainment.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"border: none\n"
"")

        self.horizontalLayout_4.addWidget(self.entertainment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icn_auto = QLabel(self.categories_frame)
        self.icn_auto.setObjectName(u"icn_auto")
        self.icn_auto.setMaximumSize(QSize(24, 16777215))
        self.icn_auto.setStyleSheet(u"background-color: none;\n"
"border:none;\n"
"")
        self.icn_auto.setPixmap(QPixmap(u":/icons/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icn_auto)

        self.lbl_auto = QLabel(self.categories_frame)
        self.lbl_auto.setObjectName(u"lbl_auto")
        self.lbl_auto.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none\n"
"")

        self.horizontalLayout_3.addWidget(self.lbl_auto)

        self.auto_2 = QLabel(self.categories_frame)
        self.auto_2.setObjectName(u"auto_2")
        self.auto_2.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"border: none\n"
"")

        self.horizontalLayout_3.addWidget(self.auto_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icn_other = QLabel(self.categories_frame)
        self.icn_other.setObjectName(u"icn_other")
        self.icn_other.setMaximumSize(QSize(24, 16777215))
        self.icn_other.setStyleSheet(u"background-color: none;\n"
"border:none;\n"
"")
        self.icn_other.setPixmap(QPixmap(u":/icons/icons/list_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icn_other)

        self.lbl_other = QLabel(self.categories_frame)
        self.lbl_other.setObjectName(u"lbl_other")
        self.lbl_other.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none\n"
"")

        self.horizontalLayout_6.addWidget(self.lbl_other)

        self.other = QLabel(self.categories_frame)
        self.other.setObjectName(u"other")
        self.other.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"border: none\n"
"")

        self.horizontalLayout_6.addWidget(self.other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_transaction = QPushButton(self.centralwidget)
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

        self.horizontalLayout_8.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)

        self.btn_delete_transaction = QPushButton(self.centralwidget)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_transaction.setIcon(icon2)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_delete_transaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 300))
        self.tableView.setMaximumSize(QSize(16777215, 400))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense Tracker", None))
        self.lbl_balance.setText(QCoreApplication.translate("MainWindow", u"Current balance", None))
        self.balance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.icn_income.setText("")
        self.lbl_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.income.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.icn_outcome.setText("")
        self.lbl_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.outcome.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.lbl_categories.setText(QCoreApplication.translate("MainWindow", u"Expense Categories", None))
        self.icn_groceries.setText("")
        self.lbl_groceries.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.groceries.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lbl_entertainment_2.setText("")
        self.lbl_entertainment.setText(QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.entertainment.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icn_auto.setText("")
        self.lbl_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.auto_2.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icn_other.setText("")
        self.lbl_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.other.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New Transaction", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit Transaction", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete Transaction", None))
    # retranslateUi

