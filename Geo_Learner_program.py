import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import webbrowser
import json

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('GeoLearner.ui', self)


with open('geolearner.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

print(obj[0]['country'])

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())
