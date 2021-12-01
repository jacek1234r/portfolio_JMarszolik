# coding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from Bramka import *
import time, sys, string, os, math
app = QtWidgets.QApplication( sys.argv ) #
QubitInterfaceWindow = QtWidgets.QMainWindow()  #instancja okna
import ctypes
np.set_printoptions( threshold = sys.maxsize )   #parametr potrzebny, aby poprawnie zapisywać do pliku duże macierze
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID( myappid ) #komenda windowsa, aby poprawnie wyświetlał ikonę programu
except:
    pass
#komenda konwersji .ui na .py:
#!python -m PyQt5.uic.pyuic -x E:\konda\envs\kub\lib\site-packages\pyqt5_tools\kub_int_new.ui -o interface3.py 
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join( base_path, relative_path )

def P( X ): 
    """Zwraca pierwiastek z argumentu"""
    return sqrt( X )

class Ui_newKubitWindow(object):
    def setupUi(self, newKubitWindow):
        newKubitWindow.setObjectName("newKubitWindow")
        newKubitWindow.resize(250, 174)
        self.frame = QtWidgets.QFrame(newKubitWindow)
        self.frame.setGeometry(QtCore.QRect(38, 30, 181, 94))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.symb = QtWidgets.QLabel(self.frame)
        self.symb.setObjectName("symb")
        self.gridLayout.addWidget(self.symb, 0, 0, 1, 1)
        self.symbPole = QtWidgets.QLineEdit(self.frame)
        self.symbPole.setObjectName("symbPole")
        self.gridLayout.addWidget(self.symbPole, 0, 1, 1, 1)
        self.zeroPole = QtWidgets.QLineEdit(self.frame)
        self.zeroPole.setObjectName("zeroPole")
        self.gridLayout.addWidget(self.zeroPole, 1, 1, 2, 1)
        self.jedenPole = QtWidgets.QLineEdit(self.frame)
        self.jedenPole.setObjectName("jedenPole")
        self.gridLayout.addWidget(self.jedenPole, 3, 1, 1, 1)
        self.jeden = QtWidgets.QLabel(self.frame)
        self.jeden.setObjectName("jeden")
        self.gridLayout.addWidget(self.jeden, 3, 0, 1, 1)
        self.zero = QtWidgets.QLabel(self.frame)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 1, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.OKButton = QtWidgets.QPushButton(newKubitWindow)
        self.OKButton.setGeometry(QtCore.QRect(50, 140, 75, 23))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(newKubitWindow)
        self.CancelButton.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.CancelButton.setObjectName("CancelButton")

        self.retranslateUi(newKubitWindow)
        QtCore.QMetaObject.connectSlotsByName(newKubitWindow)

    def retranslateUi(self, newKubitWindow):
        _translate = QtCore.QCoreApplication.translate
        newKubitWindow.setWindowTitle(_translate("newKubitWindow", "Nowy kubit"))
        self.symb.setText(_translate("newKubitWindow", "Symbol:"))
        self.jeden.setText(_translate("newKubitWindow", "|1>"))
        self.zero.setText(_translate("newKubitWindow", "|0>"))
        self.OKButton.setText(_translate("newKubitWindow", "Potwierdź"))
        self.CancelButton.setText(_translate("newKubitWindow", "Anuluj"))
          
        ####
        self.init()
        self.qwid = newKubitWindow
    def init( self ):
        self.CancelButton.mousePressEvent = self.zamknij
        self.OKButton.mousePressEvent = self.czyPoprawnie
        self.OKButton.setEnabled( False )
        self.KPE1 = self.jedenPole.keyPressEvent
        self.KPE2 = self.zeroPole.keyPressEvent
        self.KPE3 = self.symbPole.keyPressEvent
        self.jedenPole.keyPressEvent = self.wpisywanie1
        self.zeroPole.keyPressEvent = self.wpisywanie2
        self.symbPole.keyPressEvent = self.wpisywanie3
        self.wsp = 0.001
        self.wyjscie = []
    def wpisywanie1( self, ev ):
        self.KPE1( ev )
        self.weryfi()

    def wpisywanie2( self, ev ):
        self.KPE2( ev )
        self.weryfi()
    def wpisywanie3( self, ev ):
        self.KPE3( ev )
        self.weryfi()
    def weryfi( self ):
        try:
            zero = eval( self.zeroPole.text().replace( 'i', 'j' ) )
            jeden =  eval( self.jedenPole.text().replace( 'i', 'j' ) )
            if abs( abs( zero ** 2 ) + abs( jeden **  2 ) - 1 ) < self.wsp:
                if self.symbPole.text():
                    self.OKButton.setEnabled( True )
                    return True
        except:
            pass
        self.OKButton.setEnabled( False )
        return False
    def czyPoprawnie( self, ev ):
        if self.weryfi():
            #self.wyjscie.append( eval( self.zeroPole.text() ) )
            #self.wyjscie.append( eval( self.jedenPole.text() ) )
            #self.wyjscie.append( self.symbPole.text() )
            self.qwid.close()
            self.wyjscie.zapiszKubit( Kubit( eval( self.zeroPole.text()), eval( self.jedenPole.text() ), self.symbPole.text() ) )
    def zamknij( self, ev = None ):
        self.qwid.close()
    


#poniżej jest kawałek kodu utworzony programem PyQt5.uic.pyuic z pliku programu Qt Designer

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\konda\envs\kub\lib\site-packages\pyqt5_tools\kub_int_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Interfejs(object):
    def setupUi(self, Interfejs):
        Interfejs.setObjectName("Interfejs")
        Interfejs.resize(781, 657)
        self.centralwidget = QtWidgets.QWidget(Interfejs)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.darkButton = QtWidgets.QPushButton(self.frame_5)
        self.darkButton.setObjectName("darkButton")
        self.gridLayout.addWidget(self.darkButton, 0, 8, 1, 1)
        self.Title = QtWidgets.QLabel(self.frame_5)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.KubitLList = QtWidgets.QListWidget(self.frame)
        self.KubitLList.setTabletTracking(True)
        self.KubitLList.setDragEnabled(True)
        self.KubitLList.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.KubitLList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.KubitLList.setSelectionRectVisible(True)
        self.KubitLList.setObjectName("KubitLList")
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.KubitLList.addItem(item)
        self.horizontalLayout_2.addWidget(self.KubitLList)
        self.GateList = QtWidgets.QListWidget(self.frame)
        self.GateList.setMouseTracking(True)
        self.GateList.setDragEnabled(True)
        self.GateList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.GateList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.GateList.setObjectName("GateList")
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.GateList.addItem(item)
        self.horizontalLayout_2.addWidget(self.GateList)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setKerning(False)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.gridLayout_2.addWidget(self.frame, 6, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 12, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 1)
        Interfejs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Interfejs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        self.Actions = QtWidgets.QMenu(self.menubar)
        self.Actions.setObjectName("Actions")
        self.menuAdd = QtWidgets.QMenu(self.Actions)
        self.menuAdd.setObjectName("menuAdd")
        self.menu_bramki = QtWidgets.QMenu(self.menubar)
        self.menu_bramki.setObjectName("menu_bramki")
        self.menuDefault = QtWidgets.QMenu(self.menu_bramki)
        self.menuDefault.setObjectName("menuDefault")
        self.menuAdvanced = QtWidgets.QMenu(self.menu_bramki)
        self.menuAdvanced.setObjectName("menuAdvanced")
        Interfejs.setMenuBar(self.menubar)
        self.Push_Kubit_to_Gate = QtWidgets.QAction(Interfejs)
        self.Push_Kubit_to_Gate.setEnabled(True)
        self.Push_Kubit_to_Gate.setObjectName("Push_Kubit_to_Gate")
        self.Push_Gate = QtWidgets.QAction(Interfejs)
        self.Push_Gate.setEnabled(True)
        self.Push_Gate.setObjectName("Push_Gate")
        self.actionPrev_Gate = QtWidgets.QAction(Interfejs)
        self.actionPrev_Gate.setEnabled(False)
        self.actionPrev_Gate.setObjectName("actionPrev_Gate")
        self.actionRemove_Kubit = QtWidgets.QAction(Interfejs)
        self.actionRemove_Kubit.setEnabled(False)
        self.actionRemove_Kubit.setObjectName("actionRemove_Kubit")
        self.actionReset = QtWidgets.QAction(Interfejs)
        self.actionReset.setObjectName("actionReset")
        self.actionRun = QtWidgets.QAction(Interfejs)
        self.actionRun.setObjectName("actionRun")
        self.actionSWAP = QtWidgets.QAction(Interfejs)
        self.actionSWAP.setObjectName("actionSWAP")
        #self.actionTEST = QtWidgets.QAction(Interfejs)
        #self.actionTEST.setObjectName("actionTEST")
        self.actionGate = QtWidgets.QAction(Interfejs)
        self.actionGate.setObjectName("actionGate")
        self.actionKubit = QtWidgets.QAction(Interfejs)
        self.actionKubit.setObjectName("actionKubit")
        self.actionCCNOT = QtWidgets.QAction(Interfejs)
        self.actionCCNOT.setObjectName("actionCCNOT")
        self.actionGate_2 = QtWidgets.QAction(Interfejs)
        self.actionGate_2.setObjectName("actionGate_2")
        self.actionKibut = QtWidgets.QAction(Interfejs)
        self.actionKibut.setObjectName("actionKibut")
        self.actionRemove_Gate = QtWidgets.QAction(Interfejs)
        self.actionRemove_Gate.setObjectName("actionRemove_Gate")
        self.actionAdd_Gate = QtWidgets.QAction(Interfejs)
        self.actionAdd_Gate.setObjectName("actionAdd_Gate")
        self.actionEntangled_Kubit = QtWidgets.QAction(Interfejs)
        self.actionEntangled_Kubit.setObjectName("actionEntangled_Kubit")
        self.actionCreate_Bool_Gate = QtWidgets.QAction(Interfejs)
        self.actionCreate_Bool_Gate.setObjectName("actionCreate_Bool_Gate")
        self.actionHelp = QtWidgets.QAction(Interfejs)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSWAP_2 = QtWidgets.QAction(Interfejs)
        self.actionSWAP_2.setObjectName("actionSWAP_2")
        self.actionQubit_Teleportation = QtWidgets.QAction(Interfejs)
        self.actionQubit_Teleportation.setObjectName("actionQubit_Teleportation")
        self.actionDeutsch_Jozsa_circuit = QtWidgets.QAction(Interfejs)
        self.actionDeutsch_Jozsa_circuit.setObjectName("actionDeutsch_Jozsa_circuit")
        self.actionDark_Mode = QtWidgets.QAction(Interfejs)
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionExit = QtWidgets.QAction(Interfejs)
        self.actionExit.setObjectName("actionExit")
        self.actionGroover_algoritm = QtWidgets.QAction(Interfejs)
        self.actionGroover_algoritm.setObjectName("actionGroover_algoritm")
        self.actionControlled_U_Gate = QtWidgets.QAction(Interfejs)
        self.actionControlled_U_Gate.setObjectName("actionControlled_U_Gate")
        self.actionRemove_Gate_2 = QtWidgets.QAction(Interfejs)
        self.actionRemove_Gate_2.setObjectName("actionRemove_Gate_2")
        self.actionFourier_Transform = QtWidgets.QAction(Interfejs)
        self.actionFourier_Transform.setObjectName("actionFourier_Transform")
        self.actionGate_from_circuit = QtWidgets.QAction(Interfejs)
        self.actionGate_from_circuit.setObjectName("actionGate_from_circuit")
        self.actionCompare_circiut = QtWidgets.QAction(Interfejs)
        self.actionCompare_circiut.setObjectName("actionCompare_circiut")
        self.menuAdd.addAction(self.actionGate_2)
        self.menuAdd.addAction(self.actionControlled_U_Gate)
        self.menuAdd.addAction(self.actionGate_from_circuit)
        self.menuAdd.addAction(self.actionCreate_Bool_Gate)
        self.menuAdd.addSeparator()
        self.menuAdd.addAction(self.actionKibut)
        self.menuAdd.addAction(self.actionEntangled_Kubit)
        self.Actions.addAction(self.actionReset)
        self.Actions.addAction(self.menuAdd.menuAction())
        self.Actions.addAction(self.actionRemove_Gate_2)
        self.Actions.addAction(self.actionCompare_circiut)
        self.Actions.addSeparator()
        self.Actions.addAction(self.actionDark_Mode)
        self.Actions.addAction(self.actionHelp)
        self.Actions.addAction(self.actionExit)
        self.menuDefault.addAction(self.actionSWAP_2)
        self.menuAdvanced.addAction(self.actionQubit_Teleportation)
        self.menuAdvanced.addAction(self.actionDeutsch_Jozsa_circuit)
        self.menuAdvanced.addAction(self.actionGroover_algoritm)
        self.menuAdvanced.addAction(self.actionFourier_Transform)
        #self.menu_bramki.addAction(self.actionTEST)
        self.menu_bramki.addAction(self.menuDefault.menuAction())
        self.menu_bramki.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.Actions.menuAction())
        self.menubar.addAction(self.menu_bramki.menuAction())

        self.retranslateUi(Interfejs)
        QtCore.QMetaObject.connectSlotsByName(Interfejs)

    def retranslateUi(self, Interfejs):
        _translate = QtCore.QCoreApplication.translate
        Interfejs.setWindowTitle(_translate("Interfejs", "MainWindow"))
        self.label_4.setText(_translate("Interfejs", "  Qubits"))
        self.label.setText(_translate("Interfejs", "   Gates"))
        self.label_3.setText(_translate("Interfejs", "  Matrtix"))
        self.pushButton_3.setText(_translate("Interfejs", "Add qubit"))
        self.pushButton_2.setText(_translate("Interfejs", "Run"))
        self.darkButton.setText(_translate("Interfejs", "Test button"))
        self.Title.setText(_translate("Interfejs", "Qantum simulator"))
        self.pushButton.setText(_translate("Interfejs", "Remove qubit"))
        __sortingEnabled = self.KubitLList.isSortingEnabled()
        self.KubitLList.setSortingEnabled(False)
        item = self.KubitLList.item(0)
        item.setText(_translate("Interfejs", "1"))
        item = self.KubitLList.item(1)
        item.setText(_translate("Interfejs", "0"))
        item = self.KubitLList.item(2)
        item.setText(_translate("Interfejs", "+"))
        item = self.KubitLList.item(3)
        item.setText(_translate("Interfejs", "-"))
        item = self.KubitLList.item(4)
        item.setText(_translate("Interfejs", "i"))
        item = self.KubitLList.item(5)
        item.setText(_translate("Interfejs", "-i"))
        self.KubitLList.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.GateList.isSortingEnabled()
        self.GateList.setSortingEnabled(False)
        item = self.GateList.item(0)
        item.setText(_translate("Interfejs", "I"))
        item = self.GateList.item(1)
        item.setText(_translate("Interfejs", "X"))
        item = self.GateList.item(2)
        item.setText(_translate("Interfejs", "Y"))
        item = self.GateList.item(3)
        item.setText(_translate("Interfejs", "Z"))
        item = self.GateList.item(4)
        item.setText(_translate("Interfejs", "H"))
        item = self.GateList.item(5)
        item.setText(_translate("Interfejs", "S"))
        item = self.GateList.item(6)
        item.setText(_translate("Interfejs", "T"))
        item = self.GateList.item(7)
        item.setText(_translate("Interfejs", "CNOT"))
        item = self.GateList.item(8)
        item.setText(_translate("Interfejs", "revCNOT"))
        self.GateList.setSortingEnabled(__sortingEnabled)
        self.textEdit.setHtml(_translate("Interfejs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Mongolian Baiti\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">1    0   </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">0    1   </span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Interfejs", "0"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Interfejs", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Interfejs", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Interfejs", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Interfejs", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Interfejs", "vvv"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Interfejs", "bb"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Interfejs", "4"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Interfejs", "5"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Interfejs", "8"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Interfejs", "9"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Interfejs", "a"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("Interfejs", "axc"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("Interfejs", "d"))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("Interfejs", "kk"))
        item = self.tableWidget.item(0, 11)
        item.setText(_translate("Interfejs", "x"))
        item = self.tableWidget.item(0, 12)
        item.setText(_translate("Interfejs", "z"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Interfejs", "2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Interfejs", "///"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Interfejs", ",,,"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Interfejs", "3"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Interfejs", "6"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("Interfejs", "7"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("Interfejs", "9"))
        item = self.tableWidget.item(1, 7)
        item.setText(_translate("Interfejs", "vb"))
        item = self.tableWidget.item(1, 8)
        item.setText(_translate("Interfejs", "f"))
        item = self.tableWidget.item(1, 9)
        item.setText(_translate("Interfejs", "gf"))
        item = self.tableWidget.item(1, 10)
        item.setText(_translate("Interfejs", "h"))
        item = self.tableWidget.item(1, 11)
        item.setText(_translate("Interfejs", "u"))
        item = self.tableWidget.item(1, 12)
        item.setText(_translate("Interfejs", "po"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Actions.setTitle(_translate("Interfejs", "Actions"))
        self.menuAdd.setTitle(_translate("Interfejs", "Define New"))
        self.menu_bramki.setTitle(_translate("Interfejs", "Gates"))
        self.menuDefault.setTitle(_translate("Interfejs", "Default"))
        self.menuAdvanced.setTitle(_translate("Interfejs", "Advanced"))
        self.Push_Kubit_to_Gate.setText(_translate("Interfejs", "Push  Kubit"))
        self.Push_Gate.setText(_translate("Interfejs", "Next Gate"))
        self.actionPrev_Gate.setText(_translate("Interfejs", "Prev Gate"))
        self.actionRemove_Kubit.setText(_translate("Interfejs", "Remove Kubit"))
        self.actionReset.setText(_translate("Interfejs", "Clear"))
        self.actionRun.setText(_translate("Interfejs", "Run"))
        self.actionSWAP.setText(_translate("Interfejs", "SWAP"))
        #self.actionTEST.setText(_translate("Interfejs", "TEST"))
        self.actionGate.setText(_translate("Interfejs", "New Gate"))
        self.actionKubit.setText(_translate("Interfejs", "New Kubit"))
        self.actionCCNOT.setText(_translate("Interfejs", "CCNOT"))
        self.actionGate_2.setText(_translate("Interfejs", "Gate"))
        self.actionKibut.setText(_translate("Interfejs", "Qubit"))
        self.actionRemove_Gate.setText(_translate("Interfejs", "Remove Gate"))
        self.actionAdd_Gate.setText(_translate("Interfejs", "Push Gate"))
        self.actionEntangled_Kubit.setText(_translate("Interfejs", "Entangled qubit"))
        self.actionCreate_Bool_Gate.setText(_translate("Interfejs", "Bool gate"))
        self.actionHelp.setText(_translate("Interfejs", "Help"))
        self.actionSWAP_2.setText(_translate("Interfejs", "SWAP"))
        self.actionQubit_Teleportation.setText(_translate("Interfejs", "Qubit Teleportation"))
        self.actionDeutsch_Jozsa_circuit.setText(_translate("Interfejs", "Deutsch–Jozsa circuit"))
        self.actionDark_Mode.setText(_translate("Interfejs", "Dark Mode"))
        self.actionExit.setText(_translate("Interfejs", "Exit"))
        self.actionGroover_algoritm.setText(_translate("Interfejs", "Grover algoritm"))
        self.actionControlled_U_Gate.setText(_translate("Interfejs", "Controlled-U gate"))
        self.actionRemove_Gate_2.setText(_translate("Interfejs", "Remove Gate"))
        self.actionFourier_Transform.setText(_translate("Interfejs", "Fourier Transform"))
        self.actionGate_from_circuit.setText(_translate("Interfejs", "Gate from circuit"))
        self.actionCompare_circiut.setText(_translate("Interfejs", "Compare circiut"))


        ##### do tego miejsca jest generowany kod
        self.MainWindow = Interfejs
        self.init()
        
    def setNames( self, newKubits = None ):
        """ Wstawia elementy z self.inpVector jako nagłówki wierszy w tabeli """
        if newKubits is not None:
            self.tableWidget.setVerticalHeaderLabels( newKubits  + [ '0' ] * ( self.pojKub - len( newKubits  ) ) )
            return
        self.tableWidget.setVerticalHeaderLabels( self.inpVector + [ '0' ] * ( self.pojKub - len( self.inpVector ) ) )
            
    def init( self ):
        """ Definiowanie interfejsu """
        self.GateList.clicked.connect( self.rysujBramke )
        self.KubitLList.clicked.connect( self.rysujKubit )
        self.actionGate_2.triggered.connect( self.stworzBramke ) 
        self.actionKibut.triggered.connect( self.stworzKubit )  
        self.actionEntangled_Kubit.triggered.connect( self.stworzKubitZespolony )  
        self.Push_Kubit_to_Gate.triggered.connect( self.dodajKubit )  
        self.actionRemove_Kubit.triggered.connect( self.usunKubit ) 
        self.actionCreate_Bool_Gate.triggered.connect( self.booleanGateCreator )
        self.darkButton.clicked.connect( self.zmienjezyk )  
        self.actionDark_Mode.triggered.connect( self.darkMode )  
        self.pushButton_2.clicked.connect( self.symuluj )   #run
        self.actionHelp.triggered.connect( self.help )
        self.actionReset.triggered.connect( self.reset )  
        self.pushButton_3.clicked.connect( self.dodajKubit )
        self.pushButton.clicked.connect( self.usunKubit )
        self.actionExit.triggered.connect( self.leave )
        self.actionSWAP_2.triggered.connect( self.swapGate )
        #self.actionTEST.triggered.connect( self.setTest)
        self.actionQubit_Teleportation.triggered.connect( self.teleportacja )
        self.actionDeutsch_Jozsa_circuit.triggered.connect( self.dojcza )
        self.actionGroover_algoritm.triggered.connect( self.groover )
        self.actionControlled_U_Gate.triggered.connect( self.kontrol1qGate )
        self.actionRemove_Gate_2.triggered.connect( self.remGate )
        self.actionFourier_Transform.triggered.connect( self.Fourier )
        self.actionCompare_circiut.triggered.connect( self.generujBramkeZObwodu2 )
        self.actionGate_from_circuit.triggered.connect( self.generujBramkeZObwodu1 )
        self.pojObwodu = 150 #ilość kolumn
        self.pojKub = 15 #maksymalna ilość wierszy
        self.inpVector = []
        self.variables = {}
        self.textEdit.setEnabled( True )
        self.actionRemove_Kubit.setEnabled( True )
        self.darkModeFlag = False
        self.filename = 'Kubits&Gates.txt' #plik z bramkami i kubitami
        self.kubity = {}
        self.bramki = {}
        self.getInstances() 
        jakieSortowanie = self.KubitLList.isSortingEnabled()
        self.KubitLList.setSortingEnabled( False )
        self.KubitLList.clear()
        for e in self.kubity:
            item = QtWidgets.QListWidgetItem( e )
            self.KubitLList.addItem( item )
        self.KubitLList.setSortingEnabled( jakieSortowanie )
        self.GateList.clear()
        for i in self.bramki.keys():
            self.GateList.addItem( QtWidgets.QListWidgetItem( i ) )
        self.tableWidget.dragEnterEvent = self.enterItem
        self.tableWidget.dropEvent = self.dropItem
        self.GateList.dropEvent = self.takeOut
        self.kubitTime = time.time()
        self.bramkaTime = time.time()
        self.tableWidget.setAcceptDrops( True )
        font = QtGui.QFont( "Courier" )
        self.textEdit.setCurrentFont(  font )   
        self.MainWindow.setWindowTitle( 'Qantum Computer Simulator' )
        sciez = resource_path( os.path.join( "images", 'icon_QS.png') )
        self.ikonaProgramu = QtGui.QIcon( sciez )
        self.MainWindow.setWindowIcon( self.ikonaProgramu )
        
        self.tableWidget.setColumnCount( self.pojObwodu )        
        self.tableWidget.horizontalHeader().setVisible( False )
        self.wymiaryPola = [ 80, 60 ] #w tabeli
        self.tableWidget.horizontalHeader().setDefaultSectionSize( self.wymiaryPola[ 0 ] )
        self.tableWidget.verticalHeader().setDefaultSectionSize( self.wymiaryPola[ 1 ] )
                
        self.inpVector = [ '0', '0' ]        
        self.setNames() 
        self.tableWidget.setRowCount( 2 )
        self.newdragMoveEvent = self.tableWidget.dragMoveEvent
        self.tableWidget.dragMoveEvent = self.dragEv
        self.matrixShow = None

        self.englishMode = True#False#
        ################################
        self.initWidgets()
        self.matrixPrint = {}
        font = QtGui.QFont()
        font.setPointSize( 8 )
        self.tableWidget.setFont( font )
        self.tableWidget.setCurrentCell( 0, 0 )
        self.newmousePressEvent = self.tableWidget.mousePressEvent
        self.tableWidget.mousePressEvent = self.mousePressEvent
        self.pojemnik = None #do porównywania obwodów
        self.tableWidget.setVerticalScrollBarPolicy( QtCore.Qt.ScrollBarAsNeeded )
        self.tableWidget.setHorizontalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOn )
        self.tableWidget.setSizeAdjustPolicy( QtWidgets.QAbstractScrollArea.AdjustIgnored )
        self.silentMode = True#False#

        self.ui = Ui_newKubitWindow()
        self.newKubitWindow = QtWidgets.QWidget( )
        self.newKubitWindow.setWindowIcon( self.ikonaProgramu )
        self.ui.setupUi( self.newKubitWindow )
        self.ui.wsp = self.kubity[ '0' ].wsp
        self.ui.wyjscie = self

        self.bramkaDialog = Ui_Dialog()
        self.Dialog = QtWidgets.QDialog()
        self.bramkaDialog.setupUi( self.Dialog )
        self.Dialog.setWindowIcon( self.ikonaProgramu )
        self.bramkaDialog.program = self
        self.bramkaDialog.wsp = self.kubity[ '0' ].wsp

        self.kubitZespDialog = Ui_Dialog_kubit()        
        self.Dialog_kub = QtWidgets.QDialog()
        self.kubitZespDialog.setupUi( self.Dialog_kub )
        self.Dialog_kub.setWindowIcon( self.ikonaProgramu )
        self.kubitZespDialog.program = self
        self.kubitZespDialog.wsp = self.kubity[ '0' ].wsp

        self.zmienjezyk()
        self.wiadomoscBox = QtWidgets.QMessageBox( self.MainWindow )

        try:
            file = open( self.filename, 'w', newline = '' )
        except:

            self.PutError( """Nie można w tej lokalizacji tworzyć plików zewnętrznych, 
aby móc zapamiętywać storzone stany kubitów i bramki 
przenieś program na dysk i uruchom ponownie.""" )
    def leave( self ): #zamknięcie programu przyciskiem Exit
        """ Wywołuje funkcję self.save() i zamyka program """
        print( 'Exited' )
        self.save()
        sys.exit( )
        
    def help( self ):
        if self.englishMode == True:
            helpStr = """Initial state of qubits ​​can be set by dragging the appropriate qubit state symbol over the correct line.
Circuit creation is similar, you need to drag the selected gate from the tray over the target field (first from the top if the gate is multi-qubit).
The 'Run' button starts the operation of the circuit, after its completion the initial state of the circuit and after passing through all the gates will be shown.
        """
            self.PutError( helpStr, "Help" )
        else: 
            helpStr = """Wartości początkowe można ustawić poprzez przciągnięcie symbolu odpowiedniego stanu kubitu nad właściwy wiersz.
Tworzenie obwodu jest analogiczne, trzeba przeciągnąć wybraną bramkę z zasobnika nad docelowe pole(pierwsze od góry jeśli bramka jest wielokubitowa). 
Przycisk 'Run' rozpoczyna pracę obwodu, po jej zakończeniu wyswietli się początkowy stan obwodu, oraz po przejściu przez wszystkie bramki.
"""
            self.PutError( helpStr, "Pomoc" )
        
    def reverseKron( self, kubit, pokaz = True ):
        """ Sprawdza, czy z zdefiniowanych stanów znajdujących się w self.kubity można utworzyć zmienną wektor"""
        if not kubit.kubity:
            return
        wektor = kubit.macierz.ravel()
        stanyPodstawowe = list( self.kubity.values() )
        mozliweWyniki = []
        poprawka = None
        for i in range( kubit.kubity - 1, -1, -1 ):
            print( 'kubit ', kubit.kubity - i )
            mozliweWynikiAkt = []
            rozmiarKroku = 2 ** i
            sprawdzaj = -1
            dopas = None
            WektorGora = sum( [ abs( k ) ** 2 for inde, k in enumerate( wektor ) if ( 2 ** ( kubit.kubity - i ) ) * inde // ( 2 ** kubit.kubity ) % 2 == 0 ] )
            if WektorGora == 1 or WektorGora == 0:
                for j in stanyPodstawowe:
                    temp = j.macierz.ravel()
                    a = sum( abs( temp[ : int( len( temp ) / 2 ) ] ) ** 2 )
                    if j.kubity == 1 and a == WektorGora:
                            mozliweWynikiAkt.append( j )
                            print( 'dopas a', a, j.symbol )
                            dopas = j.symbol
            for ind, el in enumerate( wektor ):
                czyZnalazl = False
                #wekt =  ( 2 ** ( kubit.kubity - i ) ) * ind // ( 2 ** kubit.kubity ) % 2
                #if wekt == 0:
                #    WektorGora += abs( el ) ** 2
                if ind + 2 ** i >= len( wektor ) :
                    czyZnalazl = True
                    continue
                if ind % rozmiarKroku == 0:
                    sprawdzaj *= -1
                if sprawdzaj == 1 and el != 0:
                    para = wektor[ ind + 2 ** i ]
                    for j in stanyPodstawowe:
                        j.macierz = j.macierz.ravel()
                        if j.kubity == 1:                 
                            if j.macierz[ 0 ] != 0 and abs( para / el - j.macierz[ 1 ] / j.macierz[ 0 ] ) < j.wsp:
                                if j not in mozliweWynikiAkt:
                                    mozliweWynikiAkt.append( j )
                                czyZnalazl = True
                                dopas = j.symbol
                                print( 'dopas b', j.symbol )
                else:
                    czyZnalazl = True   
            if not dopas:
                if poprawka is None:
                    poprawka = i
                else:
                    poprawka  = False
                print('nie ma dopasowania w kubicie nr', i )

            mozliweWyniki.append( mozliweWynikiAkt )
        if poprawka is not None and poprawka is not False:
            print( 'poprawka', poprawka )
            wektorBezPoprawki = Kubit( [ i[ 0 ] for i in mozliweWyniki if i ] )
            wektorBezPoprawki = wektorBezPoprawki.macierz.ravel()
            ind1 = 0
            ind2 = 0
            for ind, el in enumerate( wektor ):
                wekt =  ( 2 ** ( kubit.kubity - poprawka ) ) * ind // ( 2 ** kubit.kubity ) % 2
                if wekt == 0:
                    if el != 0 and wektorBezPoprawki[ ind1 ] != 0:
                        wsp1 = el / wektorBezPoprawki[ ind1 ]
                    ind1 += 1
                elif wekt == 1:
                    if el != 0 and wektorBezPoprawki[ ind2 ] != 0:
                        wsp2 = el / wektorBezPoprawki[ ind2 ]
                    ind2 += 1
            #print( 'brakujące współczynniki:', wsp1, wsp2 )
            nowyKubit = Kubit( wsp1, wsp2 )
            nowySymbol = 'K1'
            for i in range( 1, 9 ):
                nowySymbol = 'K' + str( i )
                if nowySymbol not in self.kubity.keys():
                    nowyKubit.symbol = nowySymbol
                    self.zapiszKubit( nowyKubit )
                    if self.englishMode:
                        self.PutError( "One of qubit is in undeclared state, that state just got created.", 'Information' )
                    else:
                        self.PutError( "Jeden z kubitów jest w niezdefiniowanym stanie, ten stan został właśnie zdefiniowany.", "Powiadomienie" )
                    mozliweWyniki[ kubit.kubity - poprawka - 1 ].append( nowyKubit )
                    break
            print( nowyKubit.macierz )
        
        stanyPodstawowe = mozliweWyniki
        print('stany mozliwe:', stanyPodstawowe)
        ileStanow = np.prod( [ len( i ) for i in stanyPodstawowe ] )
        
        if ileStanow == 1:
            aktB = [ i[ 0 ] for i in stanyPodstawowe ]
            sprawdzanyWektor = Kubit( aktB )
            sprawdzanyWektor.macierz = sprawdzanyWektor.macierz.reshape( wektor.shape )
            if np.allclose( sprawdzanyWektor.macierz, wektor ):
                return aktB
            else:
                return False
        elif ileStanow == 0: 
            if self.englishMode:
                self.PutError( 'State not recognized.' )
            else:
                self.PutError( 'Conajmniej 1 ze stanów kubitów nierozpoznany.' )
            return
        indeksy = [ len( i ) for i in stanyPodstawowe ] 
        aktIndeks = [ 0 ] * kubit.kubity
        mozliweWyniki = []
        sizeWektor = 0
        indeks = 0
        while True:
            aktualnaBaza = []
            sizeWektor = 0
            for i in range( kubit.kubity ):
                aktualnaBaza.append( stanyPodstawowe[ i ][ aktIndeks[ i ] ] )
                sizeWektor += stanyPodstawowe[ i ][ aktIndeks[ i ] ].kubity
            if wektor.kubity == sizeWektor:
                sprawdzanyWektor = Kubit( aktualnaBaza )
                sprawdzanyWektor.macierz = sprawdzanyWektor.macierz.reshape( wektor.macierz.shape )
                if np.allclose( sprawdzanyWektor.macierz, wektor.macierz ):
                    return aktualnaBaza
            aktIndeks[ -1 ] += 1
            for k in range( len( indeksy ) -1, -1, -1 ):
                if indeksy[ k ] == aktIndeks[ k ]:
                    aktIndeks[ k ] = 0
                    aktIndeks[ k - 1 ] += 1
                else:
                    break
            else:
                break
    def darkMode( self, zwroc = False ):
        """ Zamienia motyw kolorystyczny programu na jasny, lub ciemny, zależnie od aktualnego(na przeciwny) """
        palette = QtGui.QPalette()
        if self.darkModeFlag == True:
            self.darkModeFlag = False
            self.MainWindow.setPalette( palette )
            self.pushButton_2.setPalette( palette )
            self.GateList.setPalette( palette )
            self.KubitLList.setPalette( palette )
            self.tableWidget.setPalette( palette )
            self.MainWindow.setPalette( palette )
            self.textEdit.setPalette( palette )
            return
        self.darkModeFlag = True
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 8, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 20, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 39, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 38, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 8, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 20, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 39, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 38, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 8, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 20, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 27, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 38, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 38, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        
        self.MainWindow.setPalette( palette )
        self.pushButton_2.setPalette( palette )
        self.GateList.setPalette( palette )
        self.KubitLList.setPalette( palette )
        self.tableWidget.setPalette( palette )
        self.MainWindow.setPalette( palette )
        self.textEdit.setPalette( palette )
        
    def updateFocus( self, row, col, repeat = 1 ):
        """ Zmienia wskaźnik self.tableWidget.currentCell, na następną komórkę w kolumnie, 
jeśli aktualna była ostatnią, to przechodzi do następnej kolumny i zerowego wierszu"""
        for i in range( repeat ):
            if self.tableWidget.rowCount() <= row + 1:
                self.tableWidget.setCurrentCell( 0, col + 1 )
                return False
            row += 1
        self.tableWidget.setCurrentCell( row, col )
        return True
        
    def _konvert( self, lista_str ): 
        """ Zmienia listę symboli stanów kubitów, na listę instancji klasy Kubit """
        wynik = []
        akumulator = 0
        for i in lista_str:
                kub = self.kubity[ i ]
                if akumulator == 0 and kub.kubity > 1:
                    akumulator = kub.kubity - 1
                    kubitZespolony = kub.macierz
                    wynik.append( kub )
                elif akumulator:
                    if np.array_equal( kub.macierz, kubitZespolony ):
                        akumulator -= 1
                    else:
                        if self.englishMode == True:
                            self.PutError( "Circuit have some issues in entangled kubits." )
                        else:
                            self.PutError( "Źle osadzono splątane kubity w wektorze wejściowym." )
                        return False
                else:
                    wynik.append( kub )
        if akumulator:
            if self.englishMode == True:
                self.PutError( "Problem with started vector." )
            else:
                self.PutError( "Problem z początkowym wektorem." )
            return False
        return wynik
    def usunKubit( self ):
        """ Usuwa ostatni wiersz z self.tableWidget """
        if self.tableWidget.rowCount() > 1:
            self.tableWidget.setRowCount( self.tableWidget.rowCount() - 1 )
            self.inpVector.pop( -1 )
        
    def dodajKubit( self ):
        """ Dodaje kolejny wiersz do tabeli i wypełnia go symbolem bramki 'I' """
        row = self.tableWidget.rowCount()
        if row >= self.pojKub:
            if self.englishMode == True:
                self.PutError( 'Maximum qubits reached.' )
            else:
                self.PutError( "Osiągnięto maksymalną dopuszczalną ilość kubitów." )
            return
        self.tableWidget.setRowCount( row + 1 )
        for i in range( self.tableWidget.columnCount() ):
            I = Widget( self.bramki[ 'I' ].widget.retInit() )
            I.wstaw( [ row, i ] )
        self.inpVector.append( '0' )
        self.setNames()
        return row + 1
    def setGate( self, row, col, item, swap = False ):
        """ Wstawia na podane współrzędne podany item, 
        a jeśli swap jest true to zamienia item z pola docelowego z podanym itemem"""
        if type( item ) == Baza:
            item = Widget( item.widget.retInit() )
        if item and item.wspolrzedne is not None and row == item.wspolrzedne[ 0 ] and col == item.wspolrzedne[ 1 ]:
            item = Widget( item.retInit() )
            item.wstaw( [ row, col ] )
            return
        targetItem = self.tableWidget.cellWidget( row, col )
        if type( targetItem.instancja ) != str and targetItem.instancja.symbol == 'Measurement':
            self.setPomiar( targetItem.wspolrzedne, False )
        if item is None:
            if type( targetItem.instancja ) == str:
                if type( self.tableWidget.cellWidget( row, 84 ).instancja ) == str:
                    zmi = targetItem.instancja[ -1 ]
                    targetItem.cleanWhenMove( self.afterPomiar )
                    self.tableWidget.cellWidget( row, col ).instancja = 'k' + zmi
                else:
                    targetItem.cleanWhenMove( self.bramki[ 'I' ].widget )
                return
            elif targetItem.instancja.symbol == 'Measurement':
                self.setPomiar( [ row, col ], False )
            targetItem.cleanWhenMove( self.bramki[ 'I' ].widget )
            return
        if not swap and item.wspolrzedne is not None:
            item = Widget( item.retInit() )
        if targetItem:
            targetItem.cleanWhenMove( self.bramki[ 'I' ].widget, usuwanie = False )
        item.cleanWhenMove( self.bramki[ 'I' ].widget, usuwanie = False )
        swap = item.wstaw( targetItem, usuwanie = False ) 
        if swap:
            targetItem.wspolrzedne, item.wspolrzedne = item.wspolrzedne, targetItem.wspolrzedne
        if type( item.instancja ) == Baza and item.instancja.symbol == 'Measurement' and item.wspolrzedne:
            print( 'poke2' )
            self.setPomiar( item.wspolrzedne, True )
        if type( targetItem.instancja ) == Baza and targetItem.instancja.symbol == 'Measurement':
            print('poke89')
            self.setPomiar( targetItem.wspolrzedne, True )
    def swapGate( self ):
        """ Ustawia stan obwodu tak, aby zamieniał pierwszy i drugi kubit stanami. """
        self.reset()
        self.setKub( 2 )
        self.setGate( 0, 0, self.bramki[ 'CNOT' ] )
        self.setGate( 0, 1, self.bramki[ 'revCNOT' ] )
        self.setGate( 0, 2, self.bramki[ 'CNOT' ] )
        
    def reset( self ):
        """ Wstawia symbol bramki 'I' na wszystkie wyświetlane pola """
        for i in range( self.tableWidget.rowCount() ):
            for j in range( self.tableWidget.columnCount() ):
                item = Widget( self.bramki[ 'I' ].widget.retInit() )
                item.wstaw( [ i, j ] )
        return
        
    def strToComplex( self, string, Okno = None ):
        """ Konwertuje argument typu str na liczbę, jeśli nie potrafi przekonwertować argumentu, 
        zwraca None i wyświetla komunikat o tym"""
        if not string:
            return None
        string = string.replace( 'i', 'j' )
        try:
            try:
                try:
                    wynik = float( string ) 
                except:
                    wynik = eval( string ) 
            except:
                img = ''
                real = ''
                druga_liczba = False
                zespo = False
                for i, el in enumerate( string ):
                    if i >= 1 and ( el == '-' or el == '+' ): #0-0.5j
                        druga_liczba = True
                        if el == '+':
                            continue
                    if el == 'j':
                        zespo = True
                        
                        break
                    if druga_liczba:
                        img += el
                    else:
                        real += el
                if zespo and len( img ) == 0 and len( real ) == 0:
                    real = '0'
                    img = '1'
                elif real == '':
                    real = '0'
                elif zespo and len( img ) == 0:
                    img = real
                    real = 0.
                if druga_liczba and not zespo:
                    print( string )
                    self.PutError( 'Not imaginary symbol founded' )
                    wynik = 0
                else:
                    wynik = float( real ) + float( img ) * 1.j
                
        except Exception as e:
            if self.englishMode == True:
                self.PutError( 'Error conversion.', okno = Okno )
            else:
                self.PutError( "Nie zinterpretowano parametrów poprawnie.", okno = Okno )
            print( e, string )
            return None
        return wynik
    def spacjaClear( self, string ):
        """ Usuwa znaki spacji z argumentu """
        wynik = ''
        for i in string:
            if i != ' ' and i != '[' and i != ']':
                wynik += i
        return wynik
    def stworzBramke( self, baza = None ):
        """ Jeśli podano argument i jest on instancją klasy Baza, to tworzy dla niej instancję(1 lub więcej) 
klasy Widget i odpowiednio konfiguruje łącza miedzy nimi. Jeśli nie podano argumentu, wywołuje okno zdefiniowane w Bramka.py """
        if type( baza ) == Baza:
            if baza.symbol not in self.bramki.keys():
                self.GateList.addItem( baza.symbol )
            self.bramki[ baza.symbol ] = baza
            obecny = self.tableWidget.cellWidget( 0, 0 )
            if baza.rozmiar == 1:
                baza.widget = Widget( self.emptyWidget.retInit() )
                baza.widget.instancja = baza
                baza.widget.wstaw( [ 0, 0 ] )
            else:
                baza.widget = Widget( self.emptyControl.retInit() )
                baza.widget.instancja = baza
                baza.widget.wstaw( [ 0, 0 ], True )
                widgets = baza.widget
                for i in range( baza.rozmiar - 2 ):
                    insideWidget = Widget( self.betwenGate.retInit() ) 
                    widgets.connect( insideWidget )
                    insideWidget.instancja = baza
                    widgets = insideWidget
                    insideWidget.wstaw( [ 0, 0 ], True )
                lastWidget = Widget( self.emptyControlDown.retInit() )  
                widgets.connect( lastWidget )
                lastWidget.instancja = baza
                lastWidget.wstaw( [ 0, 0 ] )
            #baza.widget.wstaw( [ 0, 0 ], True ) 
            self.setGate( 0, 0, obecny )
            return
        self.Dialog.show()

    def stworzKubitZespolony( self ):
        """ Wywołuje okno do definiowania stanu kubitu zespolonego"""        
        self.Dialog_kub.show()


    def PutError( self, komunikat, tytul = "Error", okno = None ):
        """ Wywołuje okno z podanym komunikatem """
        if okno is None:
            okno = self.wiadomoscBox
        if tytul == "Error" and self.englishMode == False:
            tytul = "Błąd"
        okno.setWindowTitle( tytul )
        okno.setStandardButtons( QtWidgets.QMessageBox.Ok )
        okno.setText( komunikat )
        okno.exec_()
    def zapiszKubit( self, kubit ):
        """ Jeśli argument spełnia wszystkie warunki, wstawia go do listy stanów kubitów """
        if kubit.macierz is None:
            if self.englishMode == True:
                self.PutError( "Not correct parameters." )
            else:
                self.PutError( "Błędne dane." )
            return
        if kubit.symbol not in self.kubity.keys():
            for ind, el in self.kubity.items():

                if el.kubity == kubit.kubity and np.allclose( el.macierz, kubit.macierz, kubit.wsp ):
                    if self.englishMode == True:
                        self.PutError( "That state of qubit is already defined." )
                    else:
                        self.PutError( "Kubit o podanych wartościach już istnieje." )
                    return

            self.KubitLList.addItem( kubit.symbol )
            self.kubity[ kubit.symbol ] = kubit
        elif ( self.kubity[ kubit.symbol ].macierz == kubit.macierz ).all():
            if self.englishMode == True:
                self.PutError( "That qubit is already defined." )
            else:
                self.PutError( "Ten kubit już istnieje." )
        else:
            if self.englishMode == True:
                self.PutError( "This name is already used, pick another one, or remove kubit first." )
            else:
                self.PutError( "Ta nazwa jest zest zajęta, podaj inną, lub najpierw usuń kubit z tą nazwą." )
        return
        if name in self.kubity.keys():
            if self.englishMode == True:
                self.PutError( 'Symbol is already used.' )
            else:
                self.PutError( "Symbol już wykorzystany, jeśli chcesz nadpisać usuń wpierw istniejący." )
            return

            if nowyKubit.DlugoscJeden():
                for i in self.kubity.values():
                    if np.allclose( i.macierz, nowyKubit.macierz ):
                        if self.englishMode:
                            self.PutError( "State already defined." )
                        else:
                            self.PutError( "Kubit o takich paramatrach juz istnieje." )
                        return


    def stworzKubit( self ):
        """ Wywołuje okno do definiowania stanu kubitu """        
        self.newKubitWindow.show()
        return
         
            
    def rysujBramke( self ):
        """ Wstawia symbol i macierz zaznaczonej bramki  z listy GateList do pola tekstowego w prawym dolnym 
rogu okna, jeśli na bramkę kliknięto drugi raz w ciągu sekundy wstawia ją do obwodu na zaznaczone pole """
        nowyCzas = time.time()
        coKlikniete = self.GateList.item( self.GateList.currentRow() ).text() 
        
        if nowyCzas - self.bramkaTime < 1:
            self.poprawStan( self.GateList.objectName() )
        if self.matrixShow != coKlikniete:
            print( 'Rysuj bramke: ', coKlikniete)
            if coKlikniete not in self.matrixPrint.keys():
                self.matrixPrint[ coKlikniete ] =  self.updateMatrix( self.bramki[ coKlikniete ] )
            self.textEdit.setText( self.matrixPrint[ coKlikniete ] )
        self.matrixShow = coKlikniete
        self.bramkaTime = nowyCzas
    def rysujKubit( self ):
        """ Wstawia symbol i wektor zaznaczonego stanu kubitu z listy KubitLList do pola tekstowego w prawym dolnym rogu okna """
        nowyCzas = time.time()
        if nowyCzas - self.kubitTime < 1:
            self.poprawStan( self.KubitLList.objectName() )
        coKlikniete = self.KubitLList.item( self.KubitLList.currentRow() ).text()
        if self.matrixShow != coKlikniete:
            print( 'Rysuj kubit', coKlikniete )
            self.updateMatrix( self.kubity[ coKlikniete ] )
        self.kubitTime = nowyCzas
        self.matrixShow = coKlikniete

    def updateMatrix( self, bazainst ): 
        konvers = bazainst.symbol + "\n"
        if type( bazainst ) == Baza:
            limit = 6
            bramkaList = []
            dlugoscstr = []
            separator = ","
            for i in range( bazainst.macierz.shape[ 1 ] ):
                if i + 1 == bazainst.macierz.shape[ 1 ]:
                    separator = ';'
                wartosci  = []
                dlugoscstr.append( 0 )
                for liczba in bazainst.macierz[ :, i ]:
                    if type( liczba ) in [ complex, np.complex128 ] and liczba.imag != 0: 
                        liczbaR = round( liczba.real, limit )
                        liczbaI = round( liczba.imag, limit )
                        if liczbaI > 0 and liczbaR != 0:
                            liczbaI =  ' + ' + str( liczbaI ) + 'j'
                        elif liczbaI > 0 and liczbaR == 0:
                            if liczbaI == int( liczbaI ):
                                liczbaI = str( int( liczbaI ) ) + 'j'
                            else:
                                liczbaI = str( liczbaI ) + 'j'
                        elif liczbaI == 0:
                            liczbaI = ' '
                        else: 
                            if liczbaI == int( liczbaI ):
                                liczbaI = str( int( liczbaI ) ) + 'j'
                            else:
                                liczbaI = str( liczbaI ) + 'j'
                        if liczbaR == 0:
                            liczbaR = ''
                        znak = str( liczbaR )[ :limit ] + str( liczbaI )
                    elif type( liczba ) in [ complex, np.complex128 ] and liczba.imag == 0:
                        if liczba.real == 0 or liczba.real == 1:
                            znak = str( int( float( liczba.real ) ) )
                        else:
                            znak = str( round( float( liczba.real ), limit ) )
                    else: 
                        znak = str( round( liczba, limit ) )
                    dlugoscstr[ -1 ] = max( dlugoscstr[ -1 ], len( znak ) )
                    wartosci.append( znak + separator )
                bramkaList.append( wartosci[ : ] )
            bramkaList[ -1 ][ -1 ] = bramkaList[ -1 ][ -1 ][ :-1 ]
            bramkaList = np.array( bramkaList ).T
            for i in range( bramkaList.shape[ 0 ] ):
                for j in range( bramkaList.shape[ 1 ] ): 
                    #print('spac:', dlugoscstr[ j ] - len( bramkaList[ i, j ] ) + 2 )
                    konvers += str( bramkaList[ i, j ] + " " * ( dlugoscstr[ j ] - len( bramkaList[ i, j ] ) + 2 ) )   
                konvers += "\n"
            #print( konvers )   
        elif type( bazainst ) == Kubit:
            macierz = bazainst.macierz.ravel()
            limit = 17
            przyblizenie = int( limit / 2 ) + 2 
            for i in range( macierz.shape[ 0 ] ):
                if macierz[ i ] == 0:
                    znak = "0.0"
                elif type( macierz[ i ] ) in [ complex, np.complex128 ]:
                    
                    if macierz[ i ].imag < 0 and macierz[ i ].real == 0:
                        znak = str( round( macierz[ i ].imag, przyblizenie ) ) + "j"
                    elif macierz[ i ].imag == 0:
                        znak = str( round( float( macierz[ i ].real ), przyblizenie ) )
                    else:
                        znak = str( round( macierz[ i ], przyblizenie ) )
                else:
                    znak = str( round( macierz[ i ], przyblizenie ) )
                konvers += znak + "\n"
        self.textEdit.setText( konvers )
        return konvers
    def setTest( self ):
        self.reset()
        self.setKub( 2 )
        self.setGate( 0, 0, self.bramki[ 'H' ] )
        self.setGate( 1, 0, self.bramki[ 'H' ] )
        self.setGate( 0, 1, self.bramki[ 'X' ] )
        self.setGate( 1, 1, self.bramki[ 'Z' ] )
        self.setGate( 0, 2, self.bramki[ 'CNOT' ] )
        self.setGate( 0, 3, self.bramki[ 'Z' ] )
    def setKub( self, howMuch ):
        """ Ustawia ilość wierszy w tabeli na zgodną z argumntem funkcji """
        row = self.tableWidget.rowCount()
        if howMuch == row: 
            return
        if howMuch > row:
            while self.dodajKubit() < howMuch: 
                pass
            return
        self.tableWidget.setRowCount( howMuch )
        self.inpVector = self.inpVector[ :howMuch ]
    def teleportacja( self ):
        """ Układa obwód reprezentujący protokół teleportacji kwantowej z teleportowanym kubitem w stanie '1' """
        self.setKub( 3 )
        self.inpVector = [ '1', 'Bel1', 'Bel1' ]
        self.reset()
        self.setNames()
        self.setGate( 0, 0, self.bramki[ 'CNOT' ] )
        self.setGate( 0, 1, self.bramki[ 'H' ] )

        self.setGate( 0, 2, self.bramki[ 'Measurement' ] )
        self.setGate( 1, 2, self.bramki[ 'Measurement' ] )

        self.setGate( 2, 3, self.bramki[ 'X' ] )
        self.setGate( 2, 4, self.bramki[ 'Z' ] )
        
        item = Widget( self.narzedziaWidget[ "BitControl" ].retInit() )
        item.wstaw( [ 1, 3 ] )
        item.instancja = "BControlk2"
        
        item = Widget( self.bitcross.retInit() )
        item.wstaw( [ 1, 4 ] )
        item.instancja = "BControlk1"
                
        item = Widget( self.narzedziaWidget[ "BitControl" ].retInit() )
        item.wstaw( [ 0, 4 ] )
        item.instancja = "BControlk1" 
        
    def askInt( self, message, title = 'Put an integer'):
        """ Wywołuje okno z polem do podania liczby, a po akceptacji zwraca tą liczbę """
        if self.englishMode != True:
            title = 'Wpisz liczbę'
                #setIntRange(int min, int max)
        variabl = QtWidgets.QInputDialog.getInt( QtWidgets.QMessageBox( self.MainWindow ), title, message )
        if not variabl[ 1 ]:
            return
        try:
            tryKonvert = int( variabl[ 0 ] )
            return tryKonvert
        except:
            if self.englishMode == True:
                self.PutError( "Write an integer." )
            else:
                self.PutError( "Podaj liczbę całkowitą, dodatnią" )
    def dojcza( self ):
        """ Pyta o ilość kubitów w obwodzie, a następnie tworzy wyrocznię reprezentujacą 2 funkcje i 1 zbalansowaną 
        i układa odpowiednio bramki w algorytm Deutscha-Jozsy """
        if self.englishMode:
            qbitsForDJ = self.askInt( "How many Qubits?", "D-J algoritm" )
        else:
            qbitsForDJ = self.askInt( "Ile kubitów umieścić w obwodzie?", "D-J algorytm" )
        if not qbitsForDJ:
            return
        self.setKub( qbitsForDJ )
        self.reset()
        self.inpVector = [ "0" ] * ( qbitsForDJ - 1 ) + [ "1" ]
        self.setNames()
        toolsName = str( qbitsForDJ ) + "q:0"   
        gat = boolGate( "0", qbitsForDJ, toolsName )
        self.stworzBramke( gat )
        toolsName = str( qbitsForDJ ) + "q:1"  
        gat = boolGate( "1", qbitsForDJ, toolsName )
        self.stworzBramke( gat )
        toolsName = str( qbitsForDJ ) + "q:i/2"
        gat = boolGate( "i%2", qbitsForDJ, toolsName )
        self.stworzBramke( gat )
        self.setGate( 0, 1,  self.bramki[ toolsName ] )
        
        for i in range( qbitsForDJ - 1 ):
            self.setGate( i, 0,  self.bramki[ 'H' ] )
            self.setGate( i, 2,  self.bramki[ 'H' ] )
            self.setGate( i, 3,  self.bramki[ 'Measurement' ] )

        self.setGate( qbitsForDJ - 1, 0,  self.bramki[ 'H' ] )
        self.setGate( qbitsForDJ - 1, 3,  self.bramki[ 'Measurement' ] )

    def groover( self ):
        """Tworzy wyrocznie kwantową wskazującą na losowy wektor i układa obwód w algorytm Grovera """
        if self.englishMode:
            qbitsForGroover = self.askInt( "How many Qubits?", "Grover's algoritm" )
        else:
            qbitsForGroover = self.askInt( "Ile kubitów umieścić w obwodzie?", " Algorytm Grover'a" )
        if not qbitsForGroover:
            return
        self.setKub( qbitsForGroover )
        self.reset()
        self.inpVector = [ "0" ] * qbitsForGroover 
        self.setNames()
        liczbakubitow = qbitsForGroover
        N = int( P( 2 ** liczbakubitow ) * pi / 4 )
        oracleName = str( liczbakubitow ) + "Qoracle"
        #boolf = '1 if i != ' + str( choice( list( range( 2 ** liczbakubitow ) ) ) ) + ' else 0'
        boolf = '1 if i != ' + str( choice( range( 2 ** liczbakubitow ) ) ) + ' else 0'
        print( 'boolf', boolf )
        gat = boolGate( boolf, liczbakubitow, oracleName )
        self.stworzBramke( gat )

        wymiar = 2 ** liczbakubitow
        gateName = 'inversion' + str( qbitsForGroover ) + 'q'
        inversion = Baza( 2 * np.full( ( wymiar, wymiar ), 1 / wymiar ) - np.eye( wymiar ), gateName )
        self.stworzBramke( inversion )
        item = []
        for i in range( liczbakubitow ):
            self.setGate( i, 0,  self.bramki[ 'H' ] )
            self.setGate( i, N * 2 + 1, self.bramki[ 'Measurement' ] )
        for i in range( N ):
            self.setGate( 0, i * 2 + 1, self.bramki[ oracleName ] )
            self.setGate( 0, i * 2 + 2, self.bramki[ gateName ] )
    def getGates( self ):
        """ Odczytuje stan tabeli i uzupełnia odpowiednie zmienne przygotowując program do wykonania właściwej symulacji """
        dlugosc = None
        listaBramek = []
        self.kontrolaBitowa = {}
        ilepomiarow = 0
        rows = self.tableWidget.rowCount()
        for i in self.variables.keys():
            self.variables[ i ] = None
        pomiar = [ None ] * rows
        for i in range( self.tableWidget.columnCount() ):
            bramkiTymczasowe = []
            nietrywialny = False
            for j in range( rows ):
                item = self.tableWidget.cellWidget( j, i )
                bramkiTymczasowe.append( item.instancja )  
            bramkiZweryfikowane = []
            akumulator = 0
            kolumna = len( listaBramek )  
            if ilepomiarow == rows:
                break
            #aktualnyElement = bramkiTymczasowe[ ilepomiarow ]
            
            if type( bramkiTymczasowe[ ilepomiarow - 1 ] ) == str:
                if bramkiTymczasowe[ ilepomiarow - 1 ][ :8 ] == 'BControl':
                    self.kontrolaBitowa[ kolumna ] = bramkiTymczasowe[ ilepomiarow - 1 ][ 8: ]
            akumulator = 0
            poke = []
            szukajkontroli = False
            for k in range( rows ):
                if type( bramkiTymczasowe[ k ] ) == Baza and bramkiTymczasowe[ k ].symbol == 'Measurement':
                    if kolumna == 0:
                        listaBramek.append( [self.bramki[ 'I' ] ] * rows )
                        kolumna += 1
                    if pomiar[ k ] is None:
                        dotychczasowePomiary = sum( 1 for x in range( len( pomiar ) ) if pomiar[ x ] is not None and x < k )
                        pomiar[ k ] = [ kolumna,  k - dotychczasowePomiary ] 
                    else:
                        print("!#$^#$%^%@#$%#@$ martwy kod")
                    ilepomiarow += 1
                    print('pomiar sie dodaje do bramek' )
                    self.variables[ 'k' + str( ilepomiarow ) ] = None
                    continue
                #if type( bramkiTymczasowe[ k ] ) == str:
                    #print( 'pomiar', pomiar )
                    #if not szukajkontroli:
                        #szukajkontroli = True
                elif type( bramkiTymczasowe[ k ] ) == str and bramkiTymczasowe[ k ][ :8 ] == 'BControl':
                    self.kontrolaBitowa[ kolumna ] = bramkiTymczasowe[ k ][ 8: ]
                    if pomiar[ k ] is not None:
                        continue
                    bramkiTymczasowe[ k ] = self.bramki[ "I" ]

                elif type( bramkiTymczasowe[ k ] ) == str and bramkiTymczasowe[ k ][ 0 ] == 'k':
                    continue
                if akumulator == 0 and bramkiTymczasowe[ k ].rozmiar > 1:
                    nietrywialny = True
                    akumulator = bramkiTymczasowe[ k ].rozmiar - 1
                    maciesz = bramkiTymczasowe[ k ].macierz
                    bramkiZweryfikowane.append( bramkiTymczasowe[ k ] )
                elif akumulator:
                    if np.array_equal( bramkiTymczasowe[ k ].macierz, maciesz ):
                        akumulator -= 1
                    else:
                        if bramkiTymczasowe[ k ].symbol == 'I' and not poke:
                            poke.append( len( bramkiZweryfikowane ) - 1 )
                        else:
                            if self.englishMode == True:
                                self.PutError( "Circuit have some issues in gates." )
                            else:
                                self.PutError( "Nieodpowiedni sposób budowania obwodu." )
                            return False, False
                else:
                    if bramkiTymczasowe[ k ].symbol != 'I':
                        nietrywialny = True
                    bramkiZweryfikowane.append( bramkiTymczasowe[ k ] )
            if akumulator:
                if self.englishMode == True:
                    self.PutError( "Circuit have some issues in gates." )
                else:
                    self.PutError( "Bramka wielokubitowa źle umieszczona." )
                return False, False
            if poke:
                print('przypadek I w srodku')
                source = bramkiTymczasowe[ poke[ 0 ] ]
                bramkaI = self.bramki[ 'I' ].macierz
                newMatrix = self.mulMatrix( source.macierz, bramkaI, source.rozmiar + len( poke ) )
                newBaza = Baza( newMatrix )
                if newBaza.macierz is None:
                    if self.englishMode == True:
                        self.PutError( "Circuit have some issues in gates." )
                    else:
                        self.PutError( "Bramka wielokubitowa źle umieszczona." )
                    return False, False
                bramkiZweryfikowane[ poke[ 0 ] ] = newBaza
            if nietrywialny:
                listaBramek.append( bramkiZweryfikowane ) 
        return listaBramek, pomiar
    def symuluj( self ):
        """  """
        odczytaneBramki, pomiar = self.getGates()
        Qbits = self._konvert( self.inpVector )
        if Qbits == False or odczytaneBramki == False or pomiar == False:
            return
        if not self.silentMode:
            print( Qbits )
        Result = self.calculate( odczytaneBramki, pomiar )
        if Result is not False:
            self.popupResult( Qbits, Result )
        
    def generujBramkeZObwodu1( self ):
        """ Tworzy bramkę tożsamą z stanem tabeli """
        listaResult = self.generujBramkeZObwodu()
        if self.englishMode:
            variabl = QtWidgets.QInputDialog.getText( self.wiadomoscBox, "Creating a gate", 'Name a creating gate' )
        else:
            variabl = QtWidgets.QInputDialog.getText( self.wiadomoscBox, "Tworzenie bramki z obwodu", 'Nazwij tworzoną bramkę.' )
        if variabl[ 0 ] and variabl[ 1 ]:
            macierz = []
            for i in listaResult:
                macierz.append( i.macierz.ravel() ) 
            matrix = np.array( macierz, dtype = np.complex128 )
            baza = Baza( matrix, variabl[ 0 ] )
            self.stworzBramke( baza )
    def generujBramkeZObwodu2( self ):
        """ Sprawdza, czy aktualny układ bramek jest tożsamy z układem bramek zapisanym w self.pojemnik"""
        listaResult = self.generujBramkeZObwodu()
        if self.pojemnik is None:
            self.pojemnik = listaResult
            if self.englishMode == True:
                self.PutError( "Remembered.", "Compare circuit" )
            else:
                self.PutError( "Zapamietano, ułóż drugi porównywany obwód.", "Porównywanie obwodów" )
            return listaResult
        for i, el in enumerate( listaResult ):
            print( self.pojemnik[ i ].macierz, el.macierz )
            if ( self.pojemnik[ i ] != el ):
                if self.englishMode == True:
                    self.PutError( "Diffrent.", "Compare circiut" )
                else:
                    self.PutError( "Obwody są różne.", "Porównywanie obwodów" )
                break
        else:
            if self.englishMode == True:
                self.PutError( "The same.", "Compare circuit" )
            else:
                self.PutError( "Obwody działają w ten sam sposób.", "Porównywanie obwodów" )
            
        self.pojemnik = None
    def generujBramkeZObwodu( self ):
        """ Liczy stan końcowy kubitów dla kolejnych stanów wejściowych """
        listaResult = []
        odczytaneBramki, pomiar = self.getGates()
        if odczytaneBramki == False:
            return
        if pomiar is not False and sum( x is not None for x in pomiar ):
            if self.englishMode == True:
                self.PutError( "Can only combine a circuit without measurement" )
            else:
                self.PutError( "Nie można dokonać tej czynności z obwodem, w którym jest umieszczony pomiar" )
            return
        
        ileKubitow = len( self.inpVector )
        #if tryb == "generujBramke":
        kubity = [ self.kubity[ "0" ], self.kubity[ "1" ] ]
        stanyPodstawowe = [ i for i in kubity if i.kubity == 1 ]
        #elif tryb == "sprawdzZgodnosc":
        #    stanyPodstawowe = [ i for i in list( self.kubity.values() ) if i.kubity == 1 ]
        ileStanow = len( stanyPodstawowe )        
        pokaz = ''
        for i in range(  ileStanow ** ileKubitow  ):
            konkretnyWektor = []
            for j in range( ileKubitow ):
                aktualnaBaza = stanyPodstawowe[ ( int( i / ileStanow ** j ) % ileStanow ) ]
                konkretnyWektor.append( aktualnaBaza )
                pokaz += aktualnaBaza.symbol
            pokaz = ''
            Result = self.calculate( odczytaneBramki.copy(), pomiar, konkretnyWektor[ :: -1 ] ) 

            listaResult.append( Result )
        return listaResult
        

                
    def calculate( self, Gates, pomiar, obecneKubity = None ):
        """ Wysyła bramki i stany kubitów do klasy System, a następnie zwraca wynik
        (po zdrodze dokonując pomiarów jeśli zdefiniowane) """
        if obecneKubity is None:
            obecneKubity = self._konvert( self.inpVector )
        
        if sum( x is not None for x in pomiar ):

            if not self.silentMode:
                print( 'pomiar', pomiar )
                print( len( Gates ) )
        
            zmierzoneKubity = 0
            zasieg = sorted( x[ 0 ] for x in pomiar if x )
            zasieg = list( set( [ 0 ] + zasieg + [ len( Gates ) ] ) )
            if not self.silentMode:
                print( 'zasiegi:', zasieg )
                print( 'konbuit', self.kontrolaBitowa )
            for i in range( 1, len( zasieg ) ):
                for j in range( zasieg[ i - 1 ], zasieg[ i ] ):
                    for kolumna, zmienna in self.kontrolaBitowa.items():
                        if j == kolumna:
                            if self.variables[ zmienna ] == 0:
                                for k, bramk in enumerate( Gates[ j ] ):
                                    if bramk.symbol != "I":
                                        Gates[ j ][ k ] = self.bramki[ "I" ]
                                        break
                    
                if not self.silentMode:
                    print('sumalcon',zasieg[ i - 1 ], zasieg[ i ])
                symulator = System( Gates[ zasieg[ i - 1 ]: zasieg[ i ] ], obecneKubity )
                obecneKubity = symulator.Symuluj()

                #####################################################all pomiary sprawdz
                #if i + 1 == len( zasieg ) and pomiar[ zasieg[ i ] ] == obecneKubity.kubity:
                #    print( 'nasz punkt docelowy gj', obecneKubity.kubity )
                #    odp = obecneKubity.pomiar( pomiar[ zasieg[ i ] ] )
                #    if not self.silentMode:
                #        print( 'wynik:', odp )
                #    for indeks, elem in enumerate( odp ):
                #        self.variables[ 'k' + str( indeks + 1 ) ] = str( elem )
                #    return 
                #else:
                for j, ele in enumerate( pomiar ):
                    if ele is not None and ele[ 0 ] == zasieg[ i ]:
                        stankubitu = obecneKubity.pomiar( [ ele[ 1 ] ] )[ 0 ]
                        #zmierzoneKubity += pomiar[ zasieg[ i ] ]
                        self.variables[ 'k' + str( j + 1 ) ] = stankubitu
                if obecneKubity.macierz is None:
                    obecneKubity = None
                    if not self.silentMode:
                        print( 'ostatni na placu boju' )
                    break  
                            
                        
        else:    
            symulator = System( Gates )
            symulator.UstawKubity( obecneKubity )
            obecneKubity = symulator.Symuluj()
        return obecneKubity
    def popupResult( self, wektorWej, Result ):
        """ Konstuuje okno z wynikiem(wartości zmiennych, 
        wynik funkcji reverseKron i parametry z Result.macierz) i je wyświetla """
        Qubi = Kubit( wektorWej )
        stanPoczatkowy = Qubi.macierz
        if self.englishMode:
            self.wiadomoscBox.setWindowTitle( "Result of simulation" )
        else:
            self.wiadomoscBox.setWindowTitle( "Wynik" )
        self.wiadomoscBox.setTextInteractionFlags( QtCore.Qt.TextSelectableByMouse )

        self.wiadomoscBox.setStandardButtons( QtWidgets.QMessageBox.Ok )
        font = QtGui.QFont( "Courier" )
        self.textEdit.setCurrentFont(  font ) 
        self.wiadomoscBox.setFont( font )
        #if self.darkModeFlag: ##!@$#@%$^
            #print('dark mode working')
            #self.wiadomoscBox1.setPalette( self.darkMode( True ) )  #poke
        ResultToPrint = ""
        varToPrint = ""
        kronToPrint = ""
        liczbaPrzyblizenie = 25
        anyVar = False
        for i, j in sorted( self.variables.items() ):
            if j != None:
                if not anyVar:
                    anyVar = True
                    if self.englishMode:
                        kubi = "Qubit " 
                        varToPrint += 'Measured qubits:\n'
                    else:
                        kubi = "Kubit " 
                        varToPrint += 'Zmierzone kubity:\n'
                varToPrint += kubi + str( i[ -1 ] ) + ' : ' + str( j ) + '\n'        
        if Result and Result.macierz is not None:
            if not self.silentMode:
                print( 'czy jeden:', sum( Result.macierz ** 2 ) )
                print( 'pomiary:', self.variables )
                print( Result.macierz )

            kubityWynikowe = self.reverseKron( Result )
            if kubityWynikowe:
                if not self.silentMode:
                    print('znaleziono dopasowanie')
                    print( kubityWynikowe )
                spacja = " " * liczbaPrzyblizenie #odległosc miedzy wejsciem a wyjsciem
                slen = len( spacja )
                if self.englishMode:
                    kronToPrint += "State of qubits before:" + " " * ( slen - 23 ) + "State of qubits after: \n"
                else:
                    kronToPrint += "Stany kubitów przed:" + " " * ( slen - 20 ) + "Stany kubitów po: \n"
                indeksKWynikowe = 0
                for i, e in enumerate( self.inpVector ):
                    if 'k' + str( i + 1 ) in self.variables.keys() and self.variables[ 'k' + str( i + 1 ) ] is not None:
                    #if kubityWynikowe[ i ] is None:
                        kronToPrint += str( e ) + spacja[ : slen - len( e ) ] + '----' + '\n'
                    else:
                        kronToPrint += str( e ) + spacja[ : slen - len( e ) ] + str( kubityWynikowe[ indeksKWynikowe ].symbol ) + '\n'
                        indeksKWynikowe += 1
                kronToPrint += '\n'
            if self.englishMode:
                ResultToPrint += "Qubit before:" + " " * ( liczbaPrzyblizenie - 14 ) + "Qubit after: \n"
            else:
                ResultToPrint += "Kubity na wejściu:" + " " * ( liczbaPrzyblizenie - 19 ) + "Kubity na wyjściu: \n"
            wejscie = stanPoczatkowy.reshape( max(stanPoczatkowy.shape ), 1 )
            wyjscie = Result.wyczyscSzum().reshape( max( Result.macierz.shape ), 1 )
            maxznak = 10
            for i in range( wejscie.shape[ 0 ] ):
                if i > 35:
                    ResultToPrint += " ... " + "\n"
                    break
                if type( wejscie[ i , 0 ] ) in [ complex, np.complex128 ] and wejscie[ i, 0 ].imag == 0:
                    kubitStartowy =  str( wejscie[ i, 0 ].real )[ :maxznak ]
                elif type( wejscie[ i , 0 ] ) in [ complex, np.complex128 ] and wejscie[ i, 0 ].real == 0:
                    kubitStartowy = str( wejscie[ i, 0 ].imag )[ :maxznak ] + 'j'
                elif str( wejscie[ i, 0 ] )[ 0 ] == '(':
                    kubitStartowy =  str( wejscie[ i, 0 ] )[ 1: -1 ][ :maxznak ]
                else:
                    kubitStartowy =  str( wejscie[ i, 0 ] ) 
                
                if wyjscie.shape[ 0 ] <= i:
                    kubitWynikowy = ""
                else:
                    flagareal = False
                    
                    kubitWynikowy = ""
                    if type( wyjscie[ i, 0 ] ) in [ complex, np.complex128 ]:
                        if wyjscie[ i, 0  ].real == wyjscie[ i, 0  ].imag == 0:
                            kubitWynikowy = '0.0'
                        else:
                            if wyjscie[ i, 0  ].real != 0:
                                flagareal = True
                                kubitWynikowy = str( wyjscie[ i, 0 ].real )[ :maxznak ]
                            if wyjscie[ i, 0  ].imag != 0:
                                if flagareal and wyjscie[ i, 0 ].imag > 0:
                                    kubitWynikowy += '+'
                                kubitWynikowy += str( wyjscie[ i, 0 ].imag )[ :maxznak ] + "j"
                    else:
                        kubitWynikowy =  str( wyjscie[ i, 0 ] ) 
                aktWektor = str( bin( i ) )[ 2: ]
                aktWektor1 = '|' + '0' * ( Qubi.kubity - len( aktWektor ) ) + aktWektor + '>: '
                aktWektor2 = '|' + '0' * ( Result.kubity - len( aktWektor ) ) + aktWektor + '>: '
                formatowanieWyjscia =  '|' + '0' * ( Result.kubity - len( aktWektor1 ) ) + aktWektor1 + '>: '
                wektorLen = len( aktWektor1 )
                formatowanieWyjscia = aktWektor1 + kubitStartowy + " " * ( liczbaPrzyblizenie - len( kubitStartowy ) - wektorLen ) 
                if not kubitWynikowy:
                    ResultToPrint += formatowanieWyjscia + "\n"
                else:
                    ResultToPrint += formatowanieWyjscia + aktWektor2 + kubitWynikowy + "\n"
        Result = varToPrint + kronToPrint + ResultToPrint
        self.wiadomoscBox.setText( Result )
        retval = self.wiadomoscBox.exec_()
    def enterItem(self, e):
        e.accept()
    def booleanGateCreator( self ): 
        """ Wywołuje okno żądające ilości kubitów, a później definicję bramki, która jest wysyłana do funkcji 'boolGate',
        a następnie tworzy bramkę, o ile 'boolGate' zwrócił instancję Bazy """
        oknoBoolean = QtWidgets.QMessageBox( self.MainWindow )
        if self.englishMode:
            inp = QtWidgets.QInputDialog.getInt( oknoBoolean, 'Boolgate creator', "Number of input qubits." )
        else:
            inp = QtWidgets.QInputDialog.getInt( oknoBoolean, 'Tworzenie bramki boolowskiej', "Na ile kubitów chcesz stworzyć bramkę?" )
        if inp[ 1 ]:
            print( inp )
            ileKubitow = inp[ 0 ] 
            try:
                if self.englishMode == True:
                    V2 = QtWidgets.QInputDialog.getText( oknoBoolean, 'Boolgate creator', 'Bool function' )
                else:
                    V2 = QtWidgets.QInputDialog.getText( oknoBoolean, 'Tworzenie bramki boolowskiej', 'Podaj definicję bramki.' )
                if V2[ 1 ] == False:
                    return
                toolsName = str( ileKubitow ) + "q:" + V2[ 0 ] 
                print( V2[ 0 ] )
                createdGate = boolGate( V2[ 0 ], ileKubitow, toolsName )
            except:
                if self.englishMode == True:
                    self.PutError( "Failed bool function." )
                else:
                    self.PutError( "Nie odało się utworzyć boolowskiej bramki przy pomocy podanej definicji." )
                return
            if V2[ 1 ]:
                print( 'tworzenie bramki na ', ileKubitow, 'kubitów wykrzystujac funkcje ', V2[ 0 ] )
                self.stworzBramke( createdGate )
        return
    def Fourier( self, ileKubitow = 4 ):
        """ Tworzy niezbędne bramki i układa transformatę Fouriera """
        if self.englishMode:
            ileKubitow = self.askInt( "How many Qubits?", "Fourier transform" )
        else:
            ileKubitow = self.askInt( "Ile kubitów umieścić w obwodzie?", "Transformata Fouriera" )
        if not ileKubitow:
            return
        self.setKub( ileKubitow )
        self.inpVector = [ '0' ] * ileKubitow
        self.setNames()
        self.reset()
        e = math.e
        newMatrixList = []
        N = 2 ** ileKubitow
        for k in range( 2, ileKubitow + 1 ):
            newMatrix = np.eye( 2 ** k, dtype = np.complex128 )
            for i in range( int( newMatrix.shape[ 0 ] / 2 ), newMatrix.shape[ 0 ], 2 ):
                newMatrix[ i, i ] = 1
                wsp =  e ** (2.j * pi * 2 ** ( -1 * k ) )
                newMatrix[ i + 1, i + 1 ] = wsp
            aktBaza = Baza( newMatrix[ :, : ], 'R' + str( k ) )
            newMatrixList.append( aktBaza )
            self.stworzBramke( aktBaza )
        ileBramek = ileKubitow + int( ( ( ileKubitow - 1) * ileKubitow ) / 2 ) + 2 #int( ileKubitow / 2 ) + 1
        print( ileBramek )
        swapName = 'SWAP' + str( ileKubitow ) + 'k'
        swapMatrix = np.zeros( [ N, N ], dtype = np.complex128 )
        for i in range( int( N / 2 ) ):
            byte = str( bin( i ) )[ 2: ]
            ansByte = int( byte[ :: -1 ] + '0' * ( ileKubitow - len( byte ) ), 2 )
            swapMatrix[ i, ansByte ] = 1
            swapMatrix[ N - i - 1, N - 1 - ansByte ] = 1
        swapGate = Baza( swapMatrix, swapName )
        self.stworzBramke( swapGate )

        kolumna = 0
        for i in range( ileKubitow ):
            self.setGate( i, kolumna, self.bramki[ 'H' ] )
            kolumna += 1
            for j in range( ileKubitow - 1 - i ):
                self.setGate( i, kolumna, newMatrixList[ j ] )
                kolumna += 1
        self.setGate( 0, kolumna, swapGate )

    def kontrol1qGate( self ):
        """ Wywołuje okienko, przy pomocy którego można zdefiniować bramkę kontrolowaną(jak CNOT). """
        print('U-controlled')
        items = []
        for e in self.bramki.values():
            if e.rozmiar == 1:
                items.append( e.symbol )
        if self.englishMode:
            item, acc = QtWidgets.QInputDialog.getItem( self.MainWindow, "Select a gate", "gates", items, 0, False )
        else:
            item, acc = QtWidgets.QInputDialog.getItem( self.MainWindow, "Wybierz bramkę", "bramki", items, 0, False )
        if acc:
            if item == 'Measurement':
                if self.englishMode == True:
                    self.PutError( "Take another gate." )
                else:
                    self.PutError( "Niedozwolona bramka." )
                return
            oldGate = self.bramki[ item ]
            newGate = np.eye( 4, dtype = np.complex128 )
            newGate[ 2, 2 ] = oldGate.macierz[ 0, 0 ]
            newGate[ 2, 3 ] = oldGate.macierz[ 0, 1 ]
            newGate[ 3, 2 ] = oldGate.macierz[ 1, 0 ]
            newGate[ 3, 3 ] = oldGate.macierz[ 1, 1 ]
            newName = 'Contr-' + item
            self.stworzBramke( Baza( newGate, newName ) )
    def _tempMul( self, macierz, x, y, e ):
        macierz[ y, x ] = e
        macierz[ y, x + 1 ] = e
        macierz[ y + 1, x ] = e
        macierz[ y + 1, x + 1 ] = e
    def tempMul( self, macierz, x, y ):
        self._tempMul( macierz, x, y, 1)
        self._tempMul( macierz, x + 2, y, 0)
        self._tempMul( macierz, x, y + 2, 0)
        self._tempMul( macierz, x + 2, y + 2, 1)
    def mulMatrix( self, bramka1, bramka2, rozmiar):
        wynik1 = np.array( [ 0 ] * ( 2 ** rozmiar ) ** 2, dtype = np.complex128 ).reshape([ 2 ** rozmiar, 2 ** rozmiar ] )
        wynik2 = np.array( [ 0 ] * ( 2 ** rozmiar ) ** 2, dtype = np.complex128 ).reshape([ 2 ** rozmiar, 2 ** rozmiar ] )
        for i, e in np.ndenumerate( bramka1 ):
            x = 4 * ( i[ 0 ] // 2 ) + i[ 0 ] % 2
            y = 4 * ( i[ 1 ] // 2 ) + i[ 1 ] % 2
            wynik1[ y, x ] = e
            wynik1[ y, x + 2 ] = e
            wynik1[ y + 2, x ] = e
            wynik1[ y + 2, x + 2 ] = e
        wynik1 = wynik1.T
        for i, e in np.ndenumerate( bramka2 ):
            x = 4 * i[ 0 ]
            y = 4 * i[ 1 ]
            self.tempMul( wynik2, x, y)
        return wynik1 * wynik2
    def getInstances( self ):
        """ Wczytuje domyślne bramki i kubity, oraz jeśli istnieje plik zewnętrzny to uzupełnia je o kubity i bramki tam przechowywane"""
        K_0 = Kubit( 1, 0, '0' )
        K_1 = Kubit( 0, 1, '1' )
        K_plus = Kubit( 1/P(2), 1/P(2), '+' )
        K_minus = Kubit( 1/P(2), -1/P(2), '-' )
        K_i = Kubit( 1/P(2), 1j/P(2), 'i' )
        K__i = Kubit( 1/P(2), -1j/P(2), '-i' )
        Bella0 = Kubit( [ 1/P(2), 0, 0, 1/P(2) ], symbol = 'Bel1' )
        Bella1 = Kubit( [ 1/P(2), 0, 0, -1/P(2) ], symbol = 'Bel2' )
        Bella2 = Kubit( [ 0, 1/P(2), 1/P(2), 0 ], symbol = 'Bel3' )
        Bella3 = Kubit( [ 0, 1/P(2), -1/P(2), 0 ], symbol = 'Bel4' )

        Y = Baza( np.array( [ [ 0, -1j ], 
                              [ 1j, 0 ] ], dtype = np.complex128 ), 'Y' )
        X = Baza( np.array( [ [ 0, 1 ],
                              [ 1, 0 ] ], dtype = np.complex128 ), 'X' )
        I = Baza( np.array( [ [ 1, 0 ],
                              [ 0, 1 ] ], dtype = np.complex128 ), 'I' )
        Z = Baza( np.array( [ [ 1, 0 ],
                              [ 0, -1 ] ], dtype = np.complex128 ), 'Z' )
        H = Baza( np.array( [ [ 1/P(2), 1/P(2) ],
                              [ 1/P(2), -1/P(2) ] ], dtype = np.complex128 ), 'H' )
        
        S = Baza( np.array( [ [ 1, 0 ],
                              [ 0, 1j ] ], dtype = np.complex128 ), 'S' )
        S.widget = None

        T = Baza( np.array( [ [ 1, 0 ],
                              [ 0,  e ** ( pi * 1j / 4 ) ] ], dtype = np.complex128 ), 'T' ) 
        T.widget = None

        CNOT = Baza( np.array([ [ 1, 0, 0, 0 ],
                                [ 0, 1, 0, 0 ],
                                [ 0, 0, 0, 1 ],
                                [ 0, 0, 1, 0 ] 
                               ], dtype = np.complex128 ), 'CNOT' )
        revCNOT = Baza( np.array([ [ 1, 0, 0, 0 ],
                                 [ 0, 0, 0, 1 ],
                                 [ 0, 0, 1, 0 ],
                                 [ 0, 1, 0, 0 ] 
                                ], dtype = np.complex128 ), 'revCNOT' )
        revCNOT.widget = None

        CCNOT = Baza( np.array(
                   [ [ 1, 0, 0, 0, 0, 0, 0, 0 ],
                     [ 0, 1, 0, 0, 0, 0, 0, 0 ],
                     [ 0, 0, 1, 0, 0, 0, 0, 0 ],
                     [ 0, 0, 0, 1, 0, 0, 0, 0 ],
                     [ 0, 0, 0, 0, 1, 0, 0, 0 ],
                     [ 0, 0, 0, 0, 0, 1, 0, 0 ],
                     [ 0, 0, 0, 0, 0, 0, 0, 1 ],
                     [ 0, 0, 0, 0, 0, 0, 1, 0 ] ], dtype = np.complex128 
                    ), 'CCNOT' )

        CCNOT.widget = None

        SWAP = Baza( np.array([  [ 1, 0, 0, 0 ],
                                 [ 0, 0, 1, 0 ],
                                 [ 0, 1, 0, 0 ],
                                 [ 0, 0, 0, 1 ] 
                                ], dtype = np.complex128 ), 'SWAP' )
        mes = Baza( np.array( [ [ 1, 0 ],
                              [ 0, 1 ] ] ), 'Measurement' )
        self.kubity = {  
                K_0.symbol : K_0, K_1.symbol : K_1,
                K_plus.symbol : K_plus, K_minus.symbol : K_minus,
                K_i.symbol : K_i, K__i.symbol :  K__i,
                Bella0.symbol : Bella0, Bella1.symbol : Bella1, 
                Bella2.symbol : Bella2, Bella3.symbol : Bella3 }

        self.bramki = { "Measurement" : mes,
                Y.symbol : Y, X.symbol : X, I.symbol : I, Z.symbol : Z, H.symbol : H, 
                S.symbol : S, T.symbol : T, CNOT.symbol : CNOT, 
                revCNOT.symbol : revCNOT, CCNOT.symbol : CCNOT, SWAP.symbol : SWAP }

        if os.path.isfile( self.filename ):
            with open( self.filename, 'r' ) as f:
                reader = f.readlines()
                for row1 in reader:
                    row = row1.split( ';' )
                    if row[ 0 ] == '0':
                        self.kubity[ row[ 1 ] ] = eval( row[ 2 ][ : -1 ] )
                    elif row[ 0 ] == '1':
                        self.bramki[ row[ 1 ] ] = eval( row[ 2 ][ : -1 ] )  #wczytaj widgety?
                        self.bramki[ row[ 1 ] ].widget = None
                    elif row[ 0 ] == '\n':
                        continue
                    else:
                        print( "error get inst, shoudn't happen", row)
    def save( self ):
        """ Zapisuje aktualny stan zmiennych self.kubity i self.bramki do pliku zewnętrznego """
        to_file = ""
        for j, e in self.kubity.items():
            if e.kubity != 0:
                el = ";Kubit(np." + "".join( repr( e.macierz ).split( '\n' ) ) + ",symbol='" + e.symbol + "')"
                to_file +=  '0;' + str( j ) + el + "\n"
        for j, e in self.bramki.items():
            if e.rozmiar != 0:
                el = ";Baza(np." + "".join( repr( e.macierz ).split( '\n' ) ) + ",'" + e.symbol + "')"
                to_file +=  '1;' + str( j ) + el + "\n" 
        #print( to_file ) 
        try:
            with open( self.filename, 'w', newline = '' ) as f:
                f.write( to_file )
        except:
            pass
    def remGate( self ):
        """ Okienko do usuwania zdefiniowanych kubitów i bramek """
        print( 'remove gate' )
        items = []
        for e in self.bramki.values():
            items.append( e.symbol )
        for e in self.kubity.values():
            items.append( e.symbol )
            
        if self.englishMode:
            item, acc = QtWidgets.QInputDialog.getItem( self.MainWindow, "Select gate/qubit", "gates and qubits", items, 0, False )
        else:
            item, acc = QtWidgets.QInputDialog.getItem( self.MainWindow, "Wybierz bramkę/kubit", "bramki i kubity", items, 0, False )
        print( item, acc )  
        if acc:
            if item == "0" or item == "1":
                if self.englishMode:
                    self.PutError( "Can't remove that fundamental kubit." )
                else:
                    self.PutError( "Nie można usunąć tego podstawowego stanu." )
                return
            if item in [ "I", "Measurement", 'H', "CNOT", "revCNOT", "X", 'Z' ]:
                if self.englishMode:
                    self.PutError( "Can't remove that fundamental gate." )
                else:
                    self.PutError( "Nie można usunąć tej podstawowej bramki." )
                return
            if item in self.kubity.keys():
                for j in range( self.KubitLList.count() ):
                    it = self.KubitLList.item( j )
                    if it.data( 0 ) == item:
                        del self.kubity[ item ]
                        self.KubitLList.takeItem( j )
                        for i, el in enumerate( self.inpVector ):
                            if el == item:
                                self.inpVector[ i ] = '0'
                                self.setNames()
                        return
                else:
                    return
            elif item in self.bramki.keys():
                for j in range( self.GateList.count() ):
                    it = self.GateList.item( j )
                    if it.data( 0 ) == item:
                        del self.bramki[ item ]
                        self.GateList.takeItem( j )
                        return
                else:
                    return
                
    def dropItem( self, e ):  
        """ Obsługuje wydarzenia związane z mechanizmem drag&drop wykonywane w programie """
        try:
        #if 1:
            korekta = 0
            rangeScroll = self.tableWidget.verticalScrollBar().maximum()
            if rangeScroll != 0 and self.tableWidget.verticalScrollBar().value() == rangeScroll:
                scrollSize = 17
                korekta = ( self.tableWidget.frameSize().height() - scrollSize ) % self.wymiaryPola[ 1 ] 
            wspolrzedne = [ int( ( e.pos().y() - korekta ) / self.wymiaryPola[ 1 ] ), int( e.pos().x() / self.wymiaryPola[ 0 ] ) ]
            wspolrzedne[ 0 ] += self.tableWidget.verticalScrollBar().value() 
            wspolrzedne[ 1 ] += self.tableWidget.horizontalScrollBar().value()
            if e.source().objectName() == 'tableWidget':
                itemSource = e.source().cellWidget( e.source().currentRow(), e.source().currentColumn() ) 
                itemTarget = self.tableWidget.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] )

                if type( itemSource.instancja ) == str:
                    if itemTarget is None:
                        self.setGate( e.source().currentRow(), e.source().currentColumn(), itemTarget, True )
                        return
                    if itemSource.instancja in self.variables.keys() and type( itemTarget.instancja ) == Baza and itemTarget.instancja.symbol != "I":
                        if type( self.tableWidget.cellWidget( itemSource.wspolrzedne[ 0 ], wspolrzedne[ 1 ] ).instancja ) == str:
                            print('wstawia KONTROLE')
                            for i in range( itemSource.wspolrzedne[ 0 ] + 1, itemTarget.wspolrzedne[ 0 ] ):
                                itemWidget = Widget( self.bitcross.retInit() )
                                itemWidget.wstaw( [ i, itemTarget.wspolrzedne[ 1 ] ] )
                                itemWidget.instancja = "BControl" + itemSource.instancja

                            itemWidget = Widget( self.controlstart.retInit() )
                            itemWidget.wstaw( [ itemSource.wspolrzedne[ 0 ], wspolrzedne[ 1 ] ] )
                            itemWidget.instancja = "BControl" + itemSource.instancja

                    return
                if itemTarget and type( itemTarget.instancja ) == Baza and itemTarget.instancja.symbol == "Measurement":
                    itemTarget, itemSource = itemSource, itemTarget
                if type( itemSource.instancja ) == Baza and itemSource.instancja.symbol == "Measurement":
                    if itemTarget and itemTarget.wspolrzedne[ 0 ] == itemSource.wspolrzedne[ 0 ]:
                        if itemTarget and itemTarget.wspolrzedne[ 1 ] > itemSource.wspolrzedne[ 1 ]:
                            self.setPomiar( itemSource.wspolrzedne, False )
                        itemSource.cleanWhenMove( self.bramki[ 'I' ].widget )
                        self.setGate( itemTarget.wspolrzedne[ 0 ], itemTarget.wspolrzedne[ 1 ], itemSource ) 
                    elif itemTarget is None:
                        self.setPomiar( itemSource.wspolrzedne, False )
                        itemSource.cleanWhenMove( self.bramki[ 'I' ].widget )
                    else:
                        self.setPomiar( itemSource.wspolrzedne, False )
                        self.setGate( itemTarget.wspolrzedne[ 0 ], itemTarget.wspolrzedne[ 1 ], itemSource, True ) 
                    return
                 
                self.setGate( e.source().currentRow(), e.source().currentColumn(), itemTarget, True )
            else:
                self.poprawStan( e.source().objectName(), wspolrzedne )
        except Exception as e:
            print( e )
            if self.englishMode:
                self.PutError( "Something went wrong." )
            else:
                self.PutError( "Niepoprawna czynność." )
    def takeOut( self, e ):
        """ Nadpisuje obecnie zaznaczone pole w tabeli domyślną bramką(I) """
        if e.source().objectName() == 'tableWidget':
            itemSource = e.source().cellWidget( e.source().currentRow(), e.source().currentColumn() ) 
            self.setGate( e.source().currentRow(), e.source().currentColumn(), None )
            if type( itemSource.instancja ) != str and itemSource.instancja.symbol == "Measurement":
                self.setPomiar( [ e.source().currentRow(), e.source().currentColumn() ], False )
        return
    def dragEv( self, e ):
        e.accept()
        self.newdragMoveEvent( e )
    
    def poprawStan( self, source, targetField = None ):
        """ Wstawia zaznaczony element z source do tabeli na obecnie zaznaczone pole, 
        lub na pole przyporządkowane do targetField(jeśli podane)"""
        if targetField is None:
            row = self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn() 
        else:
            row = targetField[ 0 ] 
            column = targetField[ 1 ] 
        if self.tableWidget.cellWidget( row, column ) is None:
            return
        if source == "GateList":
            symbol = self.GateList.item( self.GateList.currentRow() ).text()
            self.setGate( row, column, self.bramki[ symbol ] )

            if not self.updateFocus( row, column, self.bramki[ symbol ].rozmiar ):
                return

        elif source == "KubitLList":
            symbol = self.KubitLList.item( self.KubitLList.currentRow() ).text()
            size = self.kubity[ symbol ].kubity
            if row + size > len( self.inpVector ):
                if self.englishMode == True:
                    self.PutError( "Can't put that entangled Qubit here." )
                else:
                    self.PutError( "Niewystarczajaca ilość kubitów, aby umieścić tu splątany kubit." )
                return
            for i in range( row, row + size ):
                self.inpVector[ i ] = symbol
            self.setNames()
    def setPomiar( self, wspolrzedne, tworz = True ):
        """ Zamienia za bramką pomiaru pola na podwójne linie, lub wstawia domyślną bramkę(I) jeśli zmienna tworz to False """
        if self.tableWidget.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] ).instancja.symbol != 'Measurement':
            print('erros?',wspolrzedne)
            return
        
        if tworz:
            variable = 'k' + str( wspolrzedne[ 0 ] + 1 )        
            item = QtWidgets.QTableWidgetItem( variable )
            self.tableWidget.setItem( wspolrzedne[ 0 ], wspolrzedne[ 1 ] + 1, item )
            self.variables[ variable ] = None
            newItem = self.afterPomiar.retInit()
            newItem[ 1 ] = variable
        else:
            newItem = self.bramki[ 'I' ].widget.retInit()
        for i in range( wspolrzedne[ 1 ] + 1, self.tableWidget.columnCount() ):
            item = Widget( newItem )
            item.wstaw( [ wspolrzedne[ 0 ], i ] )
    def mousePressEvent(self, e):
        """ Dodanie pod PPM zmianę stanu kubitu w klikniętym wierszu """
        print( int( e.pos().y() / self.wymiaryPola[ 1 ] ), int( e.pos().x() / self.wymiaryPola[ 0 ] ) )
        if e.button() == QtCore.Qt.RightButton:
            poz = int( e.pos().y() / self.wymiaryPola[ 1 ] ) + self.tableWidget.verticalScrollBar().value()
            if poz < self.tableWidget.rowCount():
                wektor = self.tableWidget.verticalHeaderItem( poz ).text() 
                if wektor == '0':
                    self.inpVector[ poz ] = '1'
                else:
                    self.inpVector[ poz ] = '0'
                self.setNames()
        return self.newmousePressEvent( e )        

    def initWidgets( self ):
        """ Definiowanie widżetów i podpinanie ich w odpowiednie struktury """
        resourc = "images" #zaszyty w programie folder
        itemI = Widget( self.tableWidget, self.bramki[ 'I' ], resource_path( os.path.join(resourc, "IGate.png" ) ) )
        self.bramki[ 'I' ].widget = itemI
        itemI.wstaw( [ 0, 0 ] )
        itemH = Widget( self.tableWidget, self.bramki[ 'H' ], resource_path( os.path.join(resourc, "hadamardGate.png" ) ) )
        self.bramki[ 'H' ].widget = itemH
        itemH.wstaw( [ 1, 2 ] )
        
        itemX = Widget( self.tableWidget, self.bramki[ 'X' ], resource_path( os.path.join(resourc, "xGate.png" ) ) )
        self.bramki[ 'X' ].widget = itemX
        itemX.wstaw( [ 0, 1 ] )

        itemZ = Widget( self.tableWidget, self.bramki[ 'Z' ], resource_path( os.path.join(resourc, "ZGate.png" ) ) )
        self.bramki[ 'Z' ].widget = itemZ
        itemZ.wstaw( [ 0, 2 ] )
        itemY = Widget( self.tableWidget, self.bramki[ 'Y' ], resource_path( os.path.join(resourc, "YGate.png" ) ) )
        self.bramki[ 'Y' ].widget = itemY
        itemY.wstaw( [ 1, 3 ] )
        
        itemS = Widget( self.tableWidget, self.bramki[ 'S' ], resource_path( os.path.join(resourc, "SGate.png" ) ) )
        self.bramki[ 'S' ].widget = itemS
        itemS.wstaw( [ 1, 0 ] )
        
        itemCNOT1 = Widget( self.tableWidget, self.bramki[ 'CNOT' ], resource_path( os.path.join(resourc, "ControlledGate1.png" ) ) )
        self.emptyControl = Widget( itemCNOT1.retInit() )
        self.bramki[ 'CNOT' ].widget = itemCNOT1
        itemCNOT1.wstaw( [ 0, 3 ] )
        self.emptyControl.wstaw( [ 0, 7 ] )
        
        itemCNOT2 = Widget( self.tableWidget, self.bramki[ 'CNOT' ], resource_path( os.path.join(resourc, "ConrolledNOTGate.png" ) ) )
        itemCNOT1.connect( itemCNOT2 )
        itemCNOT2.wstaw( [ 1, 3 ] )
        
        itemSWAP = Widget( self.tableWidget, self.bramki[ 'SWAP' ], resource_path( os.path.join(resourc, "swapGate1.png" ) ) )
        self.bramki[ 'SWAP' ].widget = itemSWAP
        itemSWAP.wstaw( [ 0, 4 ] )
        
        itemSWAP1 = Widget( self.tableWidget, self.bramki[ 'SWAP' ], resource_path( os.path.join(resourc, "swapGate2.png" ) ) )
        itemSWAP.connect( itemSWAP1 )
        itemSWAP1.wstaw( [ 0, 5 ] )
        
        itemComtrol1 = Widget( self.tableWidget, self.bramki[ 'revCNOT' ], resource_path( os.path.join(resourc, "controlUup.png" ) ) )
        self.bramki[ 'revCNOT' ].widget = itemComtrol1
        itemComtrol1.wstaw( [ 0, 6 ] )
        
        itemComtrol2 = Widget( self.tableWidget, self.bramki[ 'revCNOT' ], resource_path( os.path.join(resourc, "controlEMPTYdown.png" ) ) )
        self.emptyControlDown = itemComtrol2
        itemComtrol1.connect( itemComtrol2 )
        itemComtrol2.wspolrzedne = [ 0, 7 ]
        self.tableWidget.setCellWidget( 0, 1, itemComtrol2 )
        #itemComtrol2.wstaw( [ 1, 0 ] )

        midGate = Widget( self.tableWidget, None, resource_path( os.path.join(resourc, "betweenGate.png" ) ) )
        self.betwenGate = midGate
        midGate.wstaw( [ 0, 8 ] )
        self.narzedziaWidget = {}

        pomiar = Widget( self.tableWidget, self.bramki[ "Measurement" ], resource_path( os.path.join(resourc, "measurement.png" ) ) )
        self.bramki[ "Measurement" ].widget = pomiar
        pomiar.wstaw( [ 1, 9 ] )
        self.narzedziaWidget[ "Measurement" ] = pomiar
        self.afterPomiar = Widget( self.tableWidget, None, resource_path( os.path.join(resourc, "doubleLine.png" ) ), 84, 35 )
        self.afterPomiar.wstaw( [ 0, 10 ] )
        
        self.emptyWidget = Widget( self.tableWidget, None, resource_path( os.path.join(resourc, "emptyGate.png" ) )  )
        
        bControl = Widget( self.tableWidget, "BitControl", resource_path( os.path.join(resourc, "bitcontrol1.png" ) ) )
        self.narzedziaWidget[ "BitControl" ] = bControl
        bControl.wstaw( [ 0, 9 ] )
        self.controlstart = bControl
        bControl1 = Widget( self.tableWidget, "BitControl", resource_path( os.path.join(resourc, "bitcontrol2.png" ) ) )
        self.bitcross = bControl1
        bControl1.wstaw( [ 0, 12 ] )
        
        self.emptyWidget.wspolrzedne = [ 0, 13 ]
        self.tableWidget.setCellWidget( 0, 1, self.emptyWidget ) #wyjątkowo, tak zostawić
        
        for i in self.bramki.values(): #definiowanie domyślnych widżetów dla pozostałych bramek
            if i.widget is None:
                self.stworzBramke( i )
        self.reset()
    def zmienjezyk( self ):
        """ Tłumaczy komunikaty i nazwy przycisków z angielskiego na polski i odwrotnie """
        _translate = QtCore.QCoreApplication.translate
        Interfejs = self.MainWindow
        if self.englishMode:
            self.englishMode = False
            Interfejs.setWindowTitle(_translate("Interfejs", "Symulator obwodów kwantowych"))
            self.label_4.setText(_translate("Interfejs", "    Kubity"))
            self.label.setText(_translate("Interfejs", "  Bramki"))
            self.label_3.setText(_translate("Interfejs", "Macierz"))
            self.pushButton_3.setText(_translate("Interfejs", "Dodaj kubit"))
            self.pushButton_2.setText(_translate("Interfejs", "Uruchom"))
            self.darkButton.setText(_translate("Interfejs", "Switch to English"))
            self.Title.setText(_translate("Interfejs", "Symulator obwodów kwantowych"))
            self.pushButton.setText(_translate("Interfejs", "Usuń kubit"))
            self.Actions.setTitle(_translate("Interfejs", "Menu"))
            self.menuAdd.setTitle(_translate("Interfejs", "Zdefiniuj"))
            self.menu_bramki.setTitle(_translate("Interfejs", "Bramki"))
            self.menuDefault.setTitle(_translate("Interfejs", "Podstawowe"))
            self.menuAdvanced.setTitle(_translate("Interfejs", "Zaawansowane"))
            self.actionReset.setText(_translate("Interfejs", "Wyczyść"))
            self.actionRun.setText(_translate("Interfejs", "Run"))
            self.actionSWAP.setText(_translate("Interfejs", "SWAP"))
            #self.actionTEST.setText(_translate("Interfejs", "TEST"))
            self.actionGate.setText(_translate("Interfejs", "New Gate"))
            self.actionKubit.setText(_translate("Interfejs", "New Kubit"))
            self.actionCCNOT.setText(_translate("Interfejs", "CCNOT"))
            self.actionGate_2.setText(_translate("Interfejs", "Bramkę"))
            self.actionKibut.setText(_translate("Interfejs", "Kubit"))
            self.actionEntangled_Kubit.setText(_translate("Interfejs", "Splątany kubit"))
            self.actionCreate_Bool_Gate.setText(_translate("Interfejs", "Bool Gate"))
            self.actionHelp.setText(_translate("Interfejs", "Pomoc"))
            self.actionSWAP_2.setText(_translate("Interfejs", "SWAP"))
            self.actionQubit_Teleportation.setText(_translate("Interfejs", "Protokół‚ teleportacji"))
            self.actionDeutsch_Jozsa_circuit.setText(_translate("Interfejs", "Układ Deutsch\'a-Jozs\'y"))
            self.actionDark_Mode.setText(_translate("Interfejs", "Ciemny motyw"))
            self.actionExit.setText(_translate("Interfejs", "Wyjście"))
            self.actionGroover_algoritm.setText(_translate("Interfejs", "Algorytm Grovera"))
            self.actionControlled_U_Gate.setText(_translate("Interfejs", "Kontrolowaną bramkę"))
            self.actionRemove_Gate_2.setText(_translate("Interfejs", "Usuń bramkę/kubit"))
            self.actionFourier_Transform.setText(_translate("Interfejs", "Transformata Fouriera"))
            self.actionGate_from_circuit.setText(_translate("Interfejs", "Bramkę z obwodu"))
            self.actionCompare_circiut.setText(_translate("Interfejs", "Porównaj obwód"))

            self.ui.symb.setText(_translate("newKubitWindow", "Symbol:"))
            self.ui.OKButton.setText(_translate("newKubitWindow", "Potwierdź"))
            self.ui.CancelButton.setText(_translate("newKubitWindow", "Anuluj"))
            self.newKubitWindow.setWindowTitle(_translate("newKubitWindow", "Nowy kubit"))

            self.Dialog.setWindowTitle(_translate("Dialog", "Tworzenie bramki"))
            self.bramkaDialog.label.setText(_translate("Dialog", "Wybierz liczbę kubitów wejściowych bramki"))
            self.bramkaDialog.label_3.setText(_translate("Dialog", "Parametry"))
        else:
            self.englishMode = True
            Interfejs.setWindowTitle(_translate("Interfejs", "Qantum Simulator"))
            self.Actions.setTitle(_translate("Interfejs", "Actions"))
            self.menuAdd.setTitle(_translate("Interfejs", "Define New"))
            self.menu_bramki.setTitle(_translate("Interfejs", "Gates"))
            self.menuDefault.setTitle(_translate("Interfejs", "Default"))
            self.menuAdvanced.setTitle(_translate("Interfejs", "Advanced"))
            self.Push_Kubit_to_Gate.setText(_translate("Interfejs", "Push  Kubit"))
            self.Push_Gate.setText(_translate("Interfejs", "Next Gate"))
            self.actionPrev_Gate.setText(_translate("Interfejs", "Prev Gate"))
            self.actionRemove_Kubit.setText(_translate("Interfejs", "Remove Kubit"))
            self.actionReset.setText(_translate("Interfejs", "Clear"))
            self.actionRun.setText(_translate("Interfejs", "Run"))
            self.actionSWAP.setText(_translate("Interfejs", "SWAP"))
            #self.actionTEST.setText(_translate("Interfejs", "TEST"))
            self.actionGate.setText(_translate("Interfejs", "New Gate"))
            self.actionKubit.setText(_translate("Interfejs", "New Kubit"))
            self.actionCCNOT.setText(_translate("Interfejs", "CCNOT"))
            self.actionGate_2.setText(_translate("Interfejs", "Gate"))
            self.actionKibut.setText(_translate("Interfejs", "Qubit"))
            #self.actionRemove_Gate.setText(_translate("Interfejs", "Remove Gate or Qubit"))
            self.actionAdd_Gate.setText(_translate("Interfejs", "Push Gate"))
            self.actionEntangled_Kubit.setText(_translate("Interfejs", "Entangled qubit"))
            self.actionCreate_Bool_Gate.setText(_translate("Interfejs", "Bool gate"))
            self.actionHelp.setText(_translate("Interfejs", "Help"))
            self.actionSWAP_2.setText(_translate("Interfejs", "SWAP"))
            self.actionQubit_Teleportation.setText(_translate("Interfejs", "Qubit Teleportation"))
            self.actionDeutsch_Jozsa_circuit.setText(_translate("Interfejs", "Deutsch-Jozs'a circuit"))
            self.actionDark_Mode.setText(_translate("Interfejs", "Dark Mode"))
            self.actionExit.setText(_translate("Interfejs", "Exit"))
            self.actionGroover_algoritm.setText(_translate("Interfejs", "Grover algoritm"))
            self.actionControlled_U_Gate.setText(_translate("Interfejs", "Controlled-U gate"))
            self.actionRemove_Gate_2.setText(_translate("Interfejs", "Remove gate/qubit"))
            self.actionFourier_Transform.setText(_translate("Interfejs", "Fourier Transform"))
            self.actionGate_from_circuit.setText(_translate("Interfejs", "Gate from circuit"))
            self.actionCompare_circiut.setText(_translate("Interfejs", "Compare circiut"))
            self.label_4.setText(_translate("Interfejs", "    Qubits"))
            self.label.setText(_translate("Interfejs", "  Gates"))
            self.label_3.setText(_translate("Interfejs", "Matrtix"))
            self.pushButton_3.setText(_translate("Interfejs", "Add qubit"))
            self.pushButton_2.setText(_translate("Interfejs", "Run"))
            self.darkButton.setText(_translate("Interfejs", "Zmień język na polski"))
            self.Title.setText(_translate("Interfejs", "Qantum Simulator"))
            self.pushButton.setText(_translate("Interfejs", "Remove qubit"))

            self.newKubitWindow.setWindowTitle(_translate("newKubitWindow", "New qubit"))
            self.ui.symb.setText(_translate("newKubitWindow", "Symbol:"))
            self.ui.OKButton.setText(_translate("newKubitWindow", "Accept"))
            self.ui.CancelButton.setText(_translate("newKubitWindow", "Cancel"))

            self.Dialog.setWindowTitle(_translate("Dialog", "Creating a gate"))
            self.bramkaDialog.label.setText(_translate("Dialog", "Pick a number of input qubits gate"))
            self.bramkaDialog.label_3.setText(_translate("Dialog", "Parameters:"))
class Widget( QtWidgets.QLabel ):
    """ Odpowiada pojedyńczymu polu w tabeli interfejsu """
    def __init__(self, tabela, instancja = None, imagePath = None, scalX = 78, scalY = 58, kolejnyWidget = None ):
        if not instancja and not imagePath:
            tabela, instancja, imagePath, scalX, scalY, kolejnyWidget = tabela #tabela to lista atrybutów z retInit
        super( Widget, self ).__init__( tabela )
        self.tabela = tabela
        self.artybutyInstancji = [ tabela, instancja, imagePath, scalX, scalY, kolejnyWidget ]
        self.instancja = instancja
        self.wspolrzedne = None
        self.kolejnyWidget = kolejnyWidget
        pic = QtGui.QPixmap( imagePath ) 
        pic = pic.scaled( scalX, scalY )
        self.setPixmap( pic )

    def retInit( self ):
        """ Zwraca listę, którą można ponownie utworzyć instancję tego widżetu """
        self.artybutyInstancji[ 1 ] = self.instancja
        return self.artybutyInstancji
    def connect( self, kolejnyWidget = None ):
        """ Przyjmuje jako argument wskaźnik na widżet, który powinien być umieszczony w tabeli w polu poniżej, jeśli takowy jest """
        if kolejnyWidget is None:
            return self.kolejnyWidget
        self.kolejnyWidget = kolejnyWidget
        self.artybutyInstancji[ -1 ] = kolejnyWidget
    def wstaw( self, wspolrzedne, inPlace = False, usuwanie = True ):
        """ Wstawia ten widżet na podaną pozycję, jeśli sam już zajmuje jakieś miejsce to zamienia się pozycjami z widżetem na podanej pozycji"""
        item = QtWidgets.QTableWidgetItem()
        resourc = 'images'
        if self.artybutyInstancji[ 2 ] in [ resource_path( os.path.join(resourc, "emptyGate.png" ) ), resource_path( os.path.join(resourc, "controlEMPTYdown.png" ) ) ]:
            symb = self.instancja.symbol
            if len( symb ) == 1:
                spacja = 5
                sizeFont = 16
            elif len( symb ) == 2:
                spacja = 4
                sizeFont = 16
            elif len( symb ) == 3:
                spacja = 5
                sizeFont = 10
            elif len( symb ) == 4:
                spacja = 7
                sizeFont = 8
            elif len( symb ) == 5:
                spacja = 11
                sizeFont = 7
            else:
                spacja = 11
                sizeFont = 7
                symb = symb[ :7 ]
            font = QtGui.QFont()
            font.setPointSize( sizeFont )
            item.setFont( font )
            item.setText( ' ' * spacja + symb )
        
        if self.wspolrzedne is not None:
            ifswap = True
            if type( wspolrzedne ) != list:
                if ( type( wspolrzedne.instancja ) != Baza or type( self.instancja ) != Baza ) and usuwanie == False:
                    ifswap = False
                    wspolrzedne.wspolrzedne, self.wspolrzedne = self.wspolrzedne, wspolrzedne.wspolrzedne
                swapWidget1 = Widget( wspolrzedne.retInit() )
                wspolrzedne = wspolrzedne.wspolrzedne
            else:
                if type( self.tabela.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] ).instancja ) != Baza and usuwanie == False:
                    ifswap = False
                    wspolrzedne, self.wspolrzedne = self.wspolrzedne, wspolrzedne
                swapWidget1 = Widget( self.tabela.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] ).retInit() )
            if type( self.instancja ) != str and swapWidget1.instancja.symbol == self.instancja.symbol:
                swapWidget1.wstaw( self.wspolrzedne )
                return ifswap
            swapWidget2 = Widget( self.retInit() )
            swapWidget2.wstaw( wspolrzedne )
            swapWidget1.wstaw( self.wspolrzedne )
            return ifswap
        if type( wspolrzedne ) != list:
            wspolrzedne = wspolrzedne.wspolrzedne
        if self.tabela.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] ):
            if type( self.tabela.cellWidget( wspolrzedne[ 0 ], wspolrzedne[ 1 ] ).instancja ) != Baza and usuwanie == False:
                return
        if type( self.instancja ) != Baza and usuwanie == False:
            return
        self.wspolrzedne = wspolrzedne
        self.tabela.setCellWidget( self.wspolrzedne[ 0 ], self.wspolrzedne[ 1 ], self )
        self.tabela.setItem( self.wspolrzedne[ 0 ], self.wspolrzedne[ 1 ], item )
        if self.kolejnyWidget and self.tabela.rowCount() > self.wspolrzedne[ 0 ] + 1:
            widget = Widget( self.kolejnyWidget.retInit() )
            wsp = 1
            if inPlace:
                wsp = 0
            widget.wstaw( [ self.wspolrzedne[ 0 ] + wsp, self.wspolrzedne[ 1 ] ], inPlace )
    def cleanWhenMove( self, cleanWith, usuwanie = True ):
        """ Nadpisuje w tabeli ten widżet(i widżet z zmiennej self.kolejnyWidget) podanym widżetem """
        if self.wspolrzedne is not None:
            if type( self.instancja ) != Baza and usuwanie == False:
                return

            if type( self.instancja ) == str or self.instancja is None:
                size = 1
            else:
                size = self.instancja.rozmiar
            for i in range( size ):
                newWidget = Widget( cleanWith.retInit() )
                newWidget.wstaw( [ self.wspolrzedne[ 0 ] + i, self.wspolrzedne[ 1 ] ] )
if  __name__ == '__main__':
    ui = Ui_Interfejs()  #zdefiniowanie instancji klasy interfejsu
    ui.setupUi( QubitInterfaceWindow ) #wstawienie interfejsu do okna
    QubitInterfaceWindow.show() #wyświetlenie programu
    status = app.exec_() #event loop
    ui.save() #zapisanie aktualnych bramek i kubitów do zewnętrznego pliku
    print( 'Finished without problems' )
    sys.exit( status ) #zamknięcie 


#niedokończona nowa funkcjonalność
def reneratorBramek( wektoryBazowe = None ):
    wektoryBazowe = wektoryBazowe.replace( " ", "" )
    wektor = ''
    r = 2 #wylicz
    #macierz = np.eye( 2 ** r )
    macierz = np.zeros( [ 2 ** r, 2 ** r ], dtype = np.complex128 )
    pierwszy = True
    strzalka = False
    wiersz = 0
    wsp = ''
    for i in wektoryBazowe:
        #print(i)
        if i == '|':
            akumuluj = True
            wektor = ''
            continue
        elif strzalka:
            if i == '>':
                strzalka = False
        
        elif i == '>':
            if akumuluj:
                akumuluj = False
                if pierwszy:
                    rzad = eval( '0b' + wektor )
                    wektor = ''
                    strzalka = True
                    pierwszy = False
                else:
                    if wsp == '':
                        wsp = '1'
                    macierz[ rzad, eval( '0b' + wektor ) ] = eval( wsp )
                    wsp = ''
        elif i == '\n':
            wiersz += 1
            pierwszy = True
        elif akumuluj:
            if i in string.digits:
                wektor += i
        else:
            if i in string.digits + '-+.,e*j':
                wsp += i
    baza = Baza( macierz )
    if baza.macierz is None:
        print( macierz )
        return False
    return baza
wektoryBazowe = '''|00> -> |00>
    |01> -> 0.5|01>-0.5j|10>+0.70710678|11>
    |10> -> 1j|11>
    |11> -> |10>'''
redered = reneratorBramek( wektoryBazowe )
#print( redered.macierz ) 
