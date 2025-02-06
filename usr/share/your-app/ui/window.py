# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(608, 71))
        self.frame1.setMaximumSize(QSize(16777215, 71))
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.net_btn = QPushButton(self.frame1)
        self.net_btn.setObjectName(u"net_btn")
        self.net_btn.setMinimumSize(QSize(141, 51))
        self.net_btn.setMaximumSize(QSize(141, 51))

        self.horizontalLayout.addWidget(self.net_btn)

        self.disk_btn = QPushButton(self.frame1)
        self.disk_btn.setObjectName(u"disk_btn")
        self.disk_btn.setMinimumSize(QSize(141, 51))
        self.disk_btn.setMaximumSize(QSize(141, 51))

        self.horizontalLayout.addWidget(self.disk_btn)

        self.cpu_btn = QPushButton(self.frame1)
        self.cpu_btn.setObjectName(u"cpu_btn")
        self.cpu_btn.setMinimumSize(QSize(141, 51))
        self.cpu_btn.setMaximumSize(QSize(141, 51))

        self.horizontalLayout.addWidget(self.cpu_btn)


        self.verticalLayout_2.addWidget(self.frame1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.net_btn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \n"
" \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435", None))
        self.disk_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0435 \n"
" \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e", None))
        self.cpu_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \n"
" \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430", None))
    # retranslateUi

