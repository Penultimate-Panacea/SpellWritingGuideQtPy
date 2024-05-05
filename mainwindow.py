# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 392)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"../../Downloads/icons8-magic-100.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generateSpell = QPushButton(self.centralwidget)
        self.generateSpell.setObjectName(u"generateSpell")
        self.generateSpell.setGeometry(QRect(20, 280, 200, 50))
        icon1 = QIcon(QIcon.fromTheme(u"emblem-synchronized"))
        self.generateSpell.setIcon(icon1)
        self.generateSpell.setFlat(False)
        self.saveSpellImage = QPushButton(self.centralwidget)
        self.saveSpellImage.setObjectName(u"saveSpellImage")
        self.saveSpellImage.setGeometry(QRect(270, 280, 200, 50))
        icon2 = QIcon(QIcon.fromTheme(u"document-save"))
        self.saveSpellImage.setIcon(icon2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(12, 32, 500, 44))
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(12, 82, 284, 25))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(16)
        self.label_7.setFont(font1)
        self.spellDisplayLabel = QLabel(self.centralwidget)
        self.spellDisplayLabel.setObjectName(u"spellDisplayLabel")
        self.spellDisplayLabel.setGeometry(QRect(530, 40, 400, 300))
        self.spellDisplayLabel.setPixmap(QPixmap(u"resources/default output.png"))
        self.spellDisplayLabel.setScaledContents(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 113, 461, 161))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.levelComboBox = QComboBox(self.layoutWidget)
        self.levelComboBox.setObjectName(u"levelComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.levelComboBox)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.rangeComboBox = QComboBox(self.layoutWidget)
        self.rangeComboBox.setObjectName(u"rangeComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rangeComboBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.areaComboBox = QComboBox(self.layoutWidget)
        self.areaComboBox.setObjectName(u"areaComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.areaComboBox)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.dtypeComboBox = QComboBox(self.layoutWidget)
        self.dtypeComboBox.setObjectName(u"dtypeComboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dtypeComboBox)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.schoolComboBox = QComboBox(self.layoutWidget)
        self.schoolComboBox.setObjectName(u"schoolComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.schoolComboBox)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 340, 461, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 461, 21))
        self.label_9.setTextFormat(Qt.TextFormat.AutoText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.generateSpell.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spell Scriber", None))
        self.generateSpell.setText(QCoreApplication.translate("MainWindow", u"Generate Spell", None))
        self.saveSpellImage.setText(QCoreApplication.translate("MainWindow", u"Save Spell Image", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gorilla of Destiny's Spell Scriber", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"UI by Penultimate_Panacea", None))
        self.spellDisplayLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Damage Type", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"UI Version: 0.1.3 Spell Writing Code from GoD's commit: b5fd502", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ALPHA PRODUCT", None))
    # retranslateUi

