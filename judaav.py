# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Judaav.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from ctypes import CDLL

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)

class Ui_Judaav(object):
    def setupUi(self, Judaav):
        Judaav.setObjectName("Judaav")
        Judaav.resize(1144, 575)
        Judaav.setMinimumSize(QtCore.QSize(784, 0))
        self.gridLayout = QtWidgets.QGridLayout(Judaav)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.upload = QtWidgets.QPushButton(Judaav)
        self.upload.setObjectName("upload")
        self.verticalLayout.addWidget(self.upload)
        self.textEdit = QtWidgets.QTextEdit(Judaav)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.vcf = QtWidgets.QPushButton(Judaav)
        self.vcf.setObjectName("vcf")
        self.vcf.clicked.connect(self.generatevcf)
        self.upload.clicked.connect(self.uploadfile)
        self.verticalLayout.addWidget(self.vcf)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Judaav)
        QtCore.QMetaObject.connectSlotsByName(Judaav)

    def retranslateUi(self, Judaav):
        _translate = QtCore.QCoreApplication.translate
        Judaav.setWindowTitle(_translate("Judaav", "Form"))
        self.upload.setText(_translate("Judaav", "Upload CSV"))
        self.textEdit.setHtml(_translate("Judaav", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; font-weight:600;\">How to use this tool</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> The format of the excel sheet of the contacts should be like Name; Phone1; Phone2;Phone3;mailid </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Now download the .csv version of the excel sheet of the contacts </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Click on the upload file button and push the downloaded csv file</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">A new .vcf file will be created in the  folder and u can put extra information too if  u want which will be asked.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Put this in your moblie phone and all the contacts would be saved in your moblie phone.</span></p></body></html>"))
        self.vcf.setText(_translate("Judaav", "Generate VCF"))

    def uploadfile(self):
        filename=QtWidgets.QFileDialog.getOpenFileName(None,  'Open File' ,'',  ("CSV Files (*.csv)"))
        print(filename)
        file=open(filename[0], 'r')
        csvfile=open("Judaavcsv.csv", 'w')
        csvfile.write(file.read())
        csvfile.close()
        file.close()
        file.close()
        print("filehandling done")

    def generatevcf(self):
        vcfgen=CDLL("/home/taneesh/Development/Judaav/vcf.so")
        numlines = sum(1 for line in open('/home/taneesh/Development/Judaav/Judaavcsv.csv'))
        vcfgen.genvcf(numlines-1)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Judaav = QtWidgets.QWidget()
    ui = Ui_Judaav()
    ui.setupUi(Judaav)
    Judaav.show()
    sys.exit(app.exec_())

