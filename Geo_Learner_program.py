import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import json
import webbrowser



class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('GeoLearner.ui', self)
        addcountry(self)
        addcapital(self)
        language(self)
        

with open('geolearner.json', 'r') as myfile:
    data = json.load(myfile)


def addcountry(self):
    nation = data[0]['country']
    self.countryText.setPlainText(nation)
    
def addcapital(self):
    capital = data[0]['capital']
    self.capitalText.setPlainText(capital)

def language(self):
    languages = data[0]['languages']
    self.languageText.setPlainText(languages)


'''
obj = json.loads(data)
for (int i = 0 in obj:
    print(obj[i]['country'])
'''


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())
