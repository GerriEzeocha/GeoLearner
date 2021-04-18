import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import webbrowser
import json



with open('geolearner.json', 'r') as myfile:
    data = json.load(myfile)
        
class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('GeoLearner.ui', self)
        self.addcountry()
        self.addcapital()
        self.language()
        

        
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
    testing non working buttons/ attempting to load sample flag
    '''
    def nextButton(self):
        print("test text")
            
    def flagpic(self):
        pixmap = QPixmap('andorraFlag.gif')
        self.flagView.setPixmap(pixmap)
        



app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())
