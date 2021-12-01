# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\konda\envs\kub\lib\site-packages\pyqt5_tools\oknoTworzeniaBramki.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from Klasy import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 340)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.macierzTekst = QtWidgets.QTextEdit(Dialog)
        self.macierzTekst.setObjectName("macierzTekst")
        self.gridLayout_2.addWidget(self.macierzTekst, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ileQub = QtWidgets.QSpinBox(self.frame_2)
        self.ileQub.setMinimum(1)
        self.ileQub.setMaximum(40)
        self.ileQub.setProperty("value", 1)
        self.ileQub.setObjectName("ileQub")
        self.horizontalLayout.addWidget(self.ileQub)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.nazwaPole = QtWidgets.QLineEdit(Dialog)
        self.nazwaPole.setObjectName("nazwaPole")
        self.gridLayout_2.addWidget(self.nazwaPole, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tworzenie bramki"))
        self.macierzTekst.setToolTip(_translate("Dialog", "<html><head/><body><p>Wprowadź parametry wierszami, oddzielone przecinkami, lub średnikami</p></body></html>"))
        self.macierzTekst.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,1</p></body></html>"))
        self.label.setText(_translate("Dialog", "Wybierz liczbę kubitów wejściowych bramki"))
        self.label_2.setText(_translate("Dialog", "Symbol:"))
        self.label_3.setText(_translate("Dialog", "Parametry"))

        #####################
        self.okno = Dialog
        self.init()
    def init( self ):
        self.macierzTekst.setHtml(QtCore.QCoreApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,1</p></body></html>"))
        self.ileQub.setMaximum( 5 )
        self.buttonBox.accepted.connect( self.potwierdz )
        self.program = None
        self.valChanged = self.ileQub.mousePressEvent
        self.ileQub.mousePressEvent = self.korekta
        self.wsp = 0.001
        self.bazaOut = None
    def czyDobraMacierz( self ):
        box = QtWidgets.QMessageBox( self.okno )
        strMacierz = self.macierzTekst.toPlainText()
        akumulatorLiczby = ''
        macierz = []
        if not len( strMacierz ):
            if self.program.englishMode == True:
                self.program.PutError( 'Missing data.', okno = box )    
            else:
                self.program.PutError( "Wprowadź symbol i parametry.", okno = box )        
            return 
        for i in range( len( strMacierz ) ):

            if strMacierz[ i ] in [ ';', ',', ':', '\n' ] and akumulatorLiczby: 
                #tutaj można dodać jakiś inny separator macierzy
                liczba = self.program.strToComplex( akumulatorLiczby, QtWidgets.QMessageBox( self.okno ) )
                akumulatorLiczby = ''
                if liczba is not None:
                    macierz.append( liczba )
                else:
                    return None
            elif strMacierz[ i ] == ' ':
                continue
            else:
                akumulatorLiczby += strMacierz[ i ]
        if akumulatorLiczby != '':
            liczba = self.program.strToComplex( akumulatorLiczby, QtWidgets.QMessageBox( self.okno ) )
            if liczba is not None:
                macierz.append( liczba )
            else:
                return None

        print( str( macierz ) )
        size = len( macierz ) ** 0.5
        if size == 0 or int( size ) != size:
            return False
        macierz = np.array( macierz, dtype = np.complex128 ).reshape( int( size ), int( size ) )
        nowaBaza = Baza( macierz, None )
        if nowaBaza.macierz is None:
            return False
        self.bazaOut = nowaBaza
        return True
    def korekta( self, ev = None ):
        print( 'korekta' )
        self.valChanged( ev )
        ileKu = self.ileQub.value()
        macierz = np.eye( 2 ** ileKu )
        konvers = ""
        for i in range( macierz.shape[ 1 ] ):
            for liczba in macierz[ :, i ]:
                konvers += str( liczba ) + ", "   
            konvers += "\n"
        if ileKu == 1:
            self.macierzTekst.setFontPointSize( 26 )
        elif ileKu == 2:
            self.macierzTekst.setFontPointSize( 15 )
        elif ileKu == 3:
            self.macierzTekst.setFontPointSize( 10 )
        elif ileKu > 0:
            self.macierzTekst.setFontPointSize( 8 )


        
        self.macierzTekst.setText( konvers[ :-3 ] )
    def potwierdz( self, x = None ):
        box = QtWidgets.QMessageBox( self.okno )
        _translate = QtCore.QCoreApplication.translate
        if not self.nazwaPole.text():
            if self.program.englishMode == True:
                self.program.PutError( "Write a symbol.", okno = box )
            else:
                self.program.PutError( "Podaj symbol bramki.", okno = box )
            return
        if self.nazwaPole.text() not in self.program.bramki.keys():
            stan = self.czyDobraMacierz()
            if stan is True:
                self.bazaOut.symbol = self.nazwaPole.text()
                self.program.stworzBramke( self.bazaOut )
                return self.okno.accept()
            elif stan is None:
                return
            else:
                if self.program.englishMode == True:
                    self.program.PutError( "Wrong parameters.", okno = box )
                else:
                    self.program.PutError( "Podane parametry nie tworzą bramki unitarnej.", okno = box )
        else:
            if self.program.englishMode == True:
                self.program.PutError( "This symbol is already in use.", okno = box )
            else:
                self.program.PutError( "Ten symbol jest już zajęty.", okno = box )




class Ui_Dialog_kubit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 340)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.macierzTekst = QtWidgets.QTextEdit(Dialog)
        self.macierzTekst.setObjectName("macierzTekst")
        self.gridLayout_2.addWidget(self.macierzTekst, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ileQub = QtWidgets.QSpinBox(self.frame_2)
        self.ileQub.setMinimum(1)
        self.ileQub.setMaximum(40)
        self.ileQub.setProperty("value", 1)
        self.ileQub.setObjectName("ileQub")
        self.horizontalLayout.addWidget(self.ileQub)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.nazwaPole = QtWidgets.QLineEdit(Dialog)
        self.nazwaPole.setObjectName("nazwaPole")
        self.gridLayout_2.addWidget(self.nazwaPole, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tworzenie bramki"))
        self.macierzTekst.setToolTip(_translate("Dialog", "<html><head/><body><p>Wprowadź parametry wierszami, oddzielone przecinkami, lub średnikami</p></body></html>"))
        self.macierzTekst.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,1</p></body></html>"))
        self.label.setText(_translate("Dialog", "Wybierz liczbę kubitów wejściowych bramki"))
        self.label_2.setText(_translate("Dialog", "Symbol:"))
        self.label_3.setText(_translate("Dialog", "Parametry"))

        #####################
        self.okno = Dialog
        self.init()
    def init( self ):
        self.macierzTekst.setHtml(QtCore.QCoreApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,1</p></body></html>"))
        self.ileQub.setMinimum( 2 )
        self.ileQub.setMaximum( 6 )
        self.ileQub.setProperty( "value", 2 )

        self.buttonBox.accepted.connect( self.potwierdz )
        self.program = None
        self.valChanged = self.ileQub.mousePressEvent
        self.ileQub.mousePressEvent = self.korekta
        self.wsp = 0.001
        self.bazaOut = None
        self.korekta()
    def czyDobraMacierz( self ):
        box = QtWidgets.QMessageBox( self.okno )
        strMacierz = self.macierzTekst.toPlainText()
        akumulatorLiczby = ''
        macierz = []
        if not len( strMacierz ):
            if self.program.englishMode == True:
                self.program.PutError( 'Missing data.', okno = box )    
            else:
                self.program.PutError( "Wprowadź symbol i parametry.", okno = box )        
            return 
        for i in range( len( strMacierz ) ):

            if strMacierz[ i ] in [ ';', ',', ':', '\n' ] and akumulatorLiczby: 
                #tutaj można dodać jakiś inny separator macierzy
                liczba = self.program.strToComplex( akumulatorLiczby, QtWidgets.QMessageBox( self.okno ) )
                
                if liczba is not None:
                    macierz.append( liczba )
                else:
                    print('xd', akumulatorLiczby)
                    return None
                akumulatorLiczby = ''
            elif strMacierz[ i ] == ' ':
                continue
            else:
                akumulatorLiczby += strMacierz[ i ]
        if akumulatorLiczby != '':
            liczba = self.program.strToComplex( akumulatorLiczby, QtWidgets.QMessageBox( self.okno ) )
            if liczba is not None:
                macierz.append( liczba )
            else:
                return None

        print( str( macierz ) )
        size = len( macierz ) ** 0.5
        if len( macierz ) < 2 or log( len( macierz ), 2 ) != int( log( len( macierz ), 2 ) ):
            return False
        macierz = np.array( macierz, dtype = np.complex128 )
        nowaBaza = Kubit( macierz, None )
        if nowaBaza.macierz is None:
            return False
        self.bazaOut = nowaBaza
        return True
    def korekta( self, ev = None ):
        print('korekta')
        if ev:
            self.valChanged( ev )
        ileKu = self.ileQub.value()
        macierz = np.zeros( [ 2 ** ileKu, 1 ] )
        konvers = ""
        for i in range( max( macierz.shape ) ):
            konvers += str( 0 ) + ", "   
            konvers += "\n"
        if ileKu == 1:
            self.macierzTekst.setFontPointSize( 26 )
        elif ileKu == 2:
            self.macierzTekst.setFontPointSize( 15 )
        elif ileKu == 3:
            self.macierzTekst.setFontPointSize( 10 )
        elif ileKu > 0:
            self.macierzTekst.setFontPointSize( 8 )


        
        self.macierzTekst.setText( konvers[ :-3 ] )
    def potwierdz( self, x = None ):
        box = QtWidgets.QMessageBox( self.okno )
        _translate = QtCore.QCoreApplication.translate
        if not self.nazwaPole.text():
            if self.program.englishMode == True:
                self.program.PutError( "Write a symbol.", okno = box )
            else:
                self.program.PutError( "Podaj symbol bramki.", okno = box )
            return
        if self.nazwaPole.text() not in self.program.kubity.keys():
            stan = self.czyDobraMacierz()
            if stan is True:
                self.bazaOut.symbol = self.nazwaPole.text()
                self.program.zapiszKubit( self.bazaOut )
                return self.okno.accept()
            elif stan is None:
                return
            else:
                if self.program.englishMode == True:
                    self.program.PutError( "Wrong parameters.", okno = box )
                else:
                    self.program.PutError( "Podane parametry nie tworzą kubitu zespolonego.", okno = box )
        else:
            if self.program.englishMode == True:
                self.program.PutError( "This symbol is already in use.", okno = box )
            else:
                self.program.PutError( "Ten symbol jest już zajęty.", okno = box )
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_kubit()
    ui.setupUi( Dialog )
    Dialog.show()
    sys.exit(app.exec_())

