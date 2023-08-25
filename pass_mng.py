# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from mydesign import Ui_Dialog  # импорт нашего сгенерированного файла
import sys
from PyQt5.QtWidgets import QFileDialog
new = []
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.add_func)
        self.ui.Save.clicked.connect(self.save_func)
        self.ui.Delete.clicked.connect(self.delete_func)
        self.ui.Open.clicked.connect(self.rewrite_func)
        global g_file
    def add_func(self):
        try:
            login = self.ui.login_line_edit.text()
            password = self.ui.password_line_edit.text()
            surname = self.ui.surname_line_edit.text()
            self.ui.listWidget.addItem(login + " "+ password +" "+ surname+'\n')

        except:
            print("")
    def save_func(self):

        
        global g_file
        myfile = QFileDialog.getOpenFileName()
        print(str(myfile[0]))
        g_file = str(myfile[0])
        list = self.ui.listWidget
        file = open(g_file, "w", encoding="utf-8")
        for x in range(list.count()):
            s = list.item(x)
            file.write(s.text())            
        file.close()   


    def delete_func(self):

        listItems=self.ui.listWidget.selectedItems()
        if not listItems: return
        for item in listItems:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def rewrite_func(self):

        
        myfile = QFileDialog.getOpenFileName()
        print(str(myfile[0]))
        g_file = str(myfile[0])

            
        file_reading = open(g_file, "r", encoding="utf-8")
        for line in file_reading:
            self.ui.listWidget.addItem(line)
        file_reading.close()


 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())