#  Form  implementation  generated  from  reading  ui  file  '.\mainwindow.ui' 
 
# 
 
#  Created  by:  PyQt6  UI  code  generator  6.7.0 
 
# 
 
#  WARNING:  Any  manual  changes  made  to  this  file  will  be  lost  when  pyuic6  is 
 
#  run  again.    Do  not  edit  this  file  unless  you  know  what  you  are  doing. 
 
 
 
from  PySide6.QtWidgets import  QApplication,  QMainWindow,  QPushButton

from  PyQt6  import  QtCore,  QtGui,  QtWidgets
 
import  os
 
 
 
class  MainWindow(QMainWindow): 
 
        def  __init__(self): 
                 super().__init__()
                 self.setupUi()
                 self.generateSpell.clicked.connect(self.generateSpellClicked)
 

        def  generateSpellClicked(self):
            gen_level  =  "1"
            gen_range  =  "Sight".lower()
            gen_area  =  "Cylinder".lower()
                gen_dtype  =  "poison"
                gen_school  =  "evocation"
                os.system(f"python3  writer.py  -level  {gen_level}  -range  {gen_range}  -area  {gen_area}  -dtype  {gen_dtype}  -school  {gen_school}")
         def  setupUi(self,  MainWindow):
                MainWindow.setObjectName("MainWindow")

                MainWindow.resize(1414,  905)

                self.centralwidget  =  QtWidgets.QWidget(parent=MainWindow)

                self.centralwidget.setObjectName("centralwidget")
 
                self.generateSpell  =  QtWidgets.QPushButton(parent=self.centralwidget)
 
                self.generateSpell.setGeometry(QtCore.QRect(10,  760,  291,  51))
 
                self.generateSpell.setDefault(False)
 
                self.generateSpell.setFlat(False)
 
                self.generateSpell.setObjectName("generateSpell")
 
                self.spellDisplay  =  QtWidgets.QGraphicsView(parent=self.centralwidget)
 
                self.spellDisplay.setGeometry(QtCore.QRect(320,  10,  1067,  800))
 
                self.spellDisplay.setAutoFillBackground(False)
 
                self.spellDisplay.setLineWidth(6)
 
                self.spellDisplay.setObjectName("spellDisplay")
 
                self.saveSpellImage  =  QtWidgets.QPushButton(parent=self.centralwidget)
 
                self.saveSpellImage.setGeometry(QtCore.QRect(1190,  820,  191,  51))
 
                self.saveSpellImage.setObjectName("saveSpellImage")
 
                self.generateSpell_2  =  QtWidgets.QPushButton(parent=self.centralwidget)
 
                self.generateSpell_2.setGeometry(QtCore.QRect(10,  310,  291,  51))
 
                self.generateSpell_2.setObjectName("generateSpell_2")
 
                self.label_6  =  QtWidgets.QLabel(parent=self.centralwidget)
 
                self.label_6.setGeometry(QtCore.QRect(30,  30,  231,  31))
 
                self.label_6.setObjectName("label_6")
 
                self.label_7  =  QtWidgets.QLabel(parent=self.centralwidget)
 
                self.label_7.setGeometry(QtCore.QRect(30,  70,  221,  31))
 
                self.label_7.setObjectName("label_7")
 
                self.progressBar  =  QtWidgets.QProgressBar(parent=self.centralwidget)
 
                self.progressBar.setGeometry(QtCore.QRect(40,  370,  221,  23))
 
                self.progressBar.setProperty("value",  24)
 
                self.progressBar.setObjectName("progressBar")
 
                self.splitter  =  QtWidgets.QSplitter(parent=self.centralwidget)
 
                self.splitter.setGeometry(QtCore.QRect(130,  400,  171,  155))
 
                self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
 
                self.splitter.setObjectName("splitter")
 
                self.comboBox  =  QtWidgets.QComboBox(parent=self.splitter)
 
                self.comboBox.setObjectName("comboBox")
 
                self.comboBox_2  =  QtWidgets.QComboBox(parent=self.splitter)
 
                self.comboBox_2.setObjectName("comboBox_2")
 
                self.comboBox_3  =  QtWidgets.QComboBox(parent=self.splitter)
 
                self.comboBox_3.setObjectName("comboBox_3")
 
                self.comboBox_4  =  QtWidgets.QComboBox(parent=self.splitter)
 
                self.comboBox_4.setObjectName("comboBox_4")
 
                self.comboBox_5  =  QtWidgets.QComboBox(parent=self.splitter)
 
                self.comboBox_5.setObjectName("comboBox_5")
 
                self.splitter_2  =  QtWidgets.QSplitter(parent=self.centralwidget)
 
                self.splitter_2.setGeometry(QtCore.QRect(12,  400,  111,  151))
 
                self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
 
                self.splitter_2.setObjectName("splitter_2")
 
                self.label  =  QtWidgets.QLabel(parent=self.splitter_2)
 
                self.label.setObjectName("label")
 
                self.label_2  =  QtWidgets.QLabel(parent=self.splitter_2)
 
                self.label_2.setObjectName("label_2")
 
                self.label_3  =  QtWidgets.QLabel(parent=self.splitter_2)
 
                self.label_3.setObjectName("label_3")
 
                self.label_4  =  QtWidgets.QLabel(parent=self.splitter_2)
 
                self.label_4.setObjectName("label_4")
 
                self.label_5  =  QtWidgets.QLabel(parent=self.splitter_2)
 
                self.label_5.setObjectName("label_5")
 
                MainWindow.setCentralWidget(self.centralwidget)
 
                self.statusbar  =  QtWidgets.QStatusBar(parent=MainWindow)
 
                self.statusbar.setObjectName("statusbar")
 
                MainWindow.setStatusBar(self.statusbar)
 
 
 
                self.retranslateUi(MainWindow)
 
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
 
 
        def  retranslateUi(self,  MainWindow): 
 
                _translate  =  QtCore.QCoreApplication.translate 
 
                MainWindow.setWindowTitle(_translate("MainWindow",  "MainWindow")) 
 
                self.generateSpell.setText(_translate("MainWindow",  "Generate  Spell")) 
 
                self.saveSpellImage.setText(_translate("MainWindow",  "Save  Spell  Image")) 
 
                self.generateSpell_2.setText(_translate("MainWindow",  "Load  Attributes")) 
 
                self.label_6.setText(_translate("MainWindow",  "Gorilla  of  Destiny\'s  Spell  Scriber")) 
 
                self.label_7.setText(_translate("MainWindow",  "UI  by  Penultimate_Panacea")) 
 
                self.label.setText(_translate("MainWindow",  "Level")) 
 
                self.label_2.setText(_translate("MainWindow",  "Range")) 
 
                self.label_3.setText(_translate("MainWindow",  "Area")) 
 
                self.label_4.setText(_translate("MainWindow",  "Damage  Type")) 
 
                self.label_5.setText(_translate("MainWindow",  "School"))

