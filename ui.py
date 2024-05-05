# File: main.py
import sys
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QFile, QIODevice

def generateSpellClicked():
    gen_level = "1"
    gen_range = "Sight".lower()
    gen_area = "Cylinder".lower()
    gen_dtype = "poison"
    gen_school = "evocation"
    os.system(f"python3 writer.py -level {gen_level} -range {gen_range} -area {gen_area} -dtype {gen_dtype} -school {gen_school}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)

    window.show()
    window.generateSpell.clicked.connect(generateSpellClicked())
    sys.exit(app.exec())
