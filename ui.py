# File: main.py
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from mainwindow import Ui_MainWindow
import win32api

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.populateAttributesfromTxt()
        self.generateSpell.clicked.connect(self.generateSpellClicked)
        self.saveSpellImage.clicked.connect(self.save_file)
        self.spellPixmap = QPixmap('resources\default output.png')

    @Slot()
    def generateSpellClicked(self):
        gen_level = self.levelComboBox.currentText().lower()
        gen_range = '"{}"'.format(self.rangeComboBox.currentText().lower())
        gen_area = self.areaComboBox.currentText().lower()
        gen_dtype = self.dtypeComboBox.currentText().lower()
        gen_school = self.schoolComboBox.currentText().lower()
        os.system(
            f"python3 writer.py -level {gen_level} -range {gen_range} -area {gen_area} -dtype {gen_dtype} -school {gen_school}")
        self.pixmap = QPixmap('output.png')
        self.spellDisplayLabel.setPixmap(self.pixmap)


    @Slot()
    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "output.png", "PNG Files (*.png);;All Files (*)", options=options)
        if file_name:
            # Save pixmap to selected file_name
            self.pixmap.save(file_name, "PNG")
            print("File saved as:", file_name)

    def populateAttributesfromTxt(self):
        with open("Attributes/area_types.txt", 'r') as file:
            areas = [line.strip() for line in file.readlines()]
        with open("Attributes/levels.txt", 'r') as file:
            levels = [line.strip() for line in file.readlines()]
        with open("Attributes/damage_types.txt", 'r') as file:
            dtypes = [line.strip() for line in file.readlines()]
        with open("Attributes/range.txt", 'r') as file:
            ranges = [line.strip() for line in file.readlines()]
        with open("Attributes/school.txt", 'r') as file:
            schools = [line.strip() for line in file.readlines()]

        for area in areas:
            self.areaComboBox.addItem(area)
        for level in levels:
            self.levelComboBox.addItem(level)
        for dtype in dtypes:
            self.dtypeComboBox.addItem(dtype)
        for range in ranges:
            self.rangeComboBox.addItem(range)
        for school in schools:
            self.schoolComboBox.addItem(school)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources\magic.png'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

