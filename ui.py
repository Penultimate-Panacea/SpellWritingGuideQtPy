# File: main.py
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QIcon
from mainwindow import Ui_MainWindow


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
        areas = ['Blank', 'Cube', 'Line', 'Multiple-Targets', 'Multiple-Targets/Sphere', 'Cone', 'Cone/Sphere', 'Square', 'Circle', 'Sphere', 'Sphere/Cylinder', 'Single-Target', 'Single-Target/Cube', 'Single-Target/Multiple-Targets', 'Single-Target/Cone', 'Single-Target/Sphere', 'Single-Target/Wall', 'Wall', 'Cylinder', 'None']
        levels = ['blank', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        dtypes = ['blank', 'acid', 'bludgeoning', 'cold', 'damage', 'extra', 'fire', 'force', 'lightning', 'necrotic', 'nonmagical', 'piercing', 'poison', 'psychic', 'radiant', 'slashing', 'thunder']
        ranges = ['blank', '10-feet radius', '100-feet line', '15-feet cone', '15-feet cube', '15-feet radius', '30-feet cone', '30-feet line', '30-feet radius', '5-feet radius', '60-feet cone', '60-feet line', 'Point (1 miles)', 'Point (10 feet)', 'Point (1000 feet)', 'Point (120 feet)', 'Point (150 feet)', 'Point (30 feet)', 'Point (300 feet)', 'Point (5 feet)', 'Point (500 feet)', 'Point (60 feet)', 'Point (90 feet)', 'Self', 'Sight', 'Special', 'Touch']
        schools = ['blank', 'Conjuration', 'Necromancy', 'Evocation', 'Abjuration', 'Transmutation', 'Divination', 'Enchantment', 'Illusion']
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

