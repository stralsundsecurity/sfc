# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Lib\site-packages\pyqt5_tools\Krypto_Systemsicherheit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableView
import binascii, re

import sys, math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(1100, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 111, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 10, 861, 499))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.tableView = myTabelView(self.verticalLayoutWidget_2)
        # self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableView.setAutoScrollMargin(16)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableView)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tableView_2 = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_2.sizePolicy().hasHeightForWidth())
        self.tableView_2.setSizePolicy(sizePolicy)
        self.tableView_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_2.horizontalHeader().setVisible(False)
        self.tableView_2.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableView_2)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(2, 330, 230, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(166678, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 430, 21, 16))
        self.label_9.setObjectName("label_9")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 430, 155, 35))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1114, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "encryption type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "DES"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AES"))
        self.label_2.setText(_translate("MainWindow", "encryption mode"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "CBC"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "CBF"))
        self.label_3.setText(_translate("MainWindow", "block size"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "64 bits"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "128 bits"))
        self.label_4.setText(_translate("MainWindow", "encoding"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Hex"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Base64"))
        self.label_5.setText(_translate("MainWindow", "ciphertext :"))
        self.label_6.setText(_translate("MainWindow", "cleartext :"))
        self.label_7.setText(_translate("MainWindow", "IV (Hex):"))
        self.label_8.setText(_translate("MainWindow", "Input: "))
        self.label_9.setText(_translate("MainWindow", "X0: "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

class myTabelView(QtWidgets.QTableView):
    keypressedSignal = QtCore.pyqtSignal(object)
    def __init__(self, parent):
        super(myTabelView, self).__init__(parent)


    def keyPressEvent(self, ev):
        self.keypressedSignal.emit(ev)


class mywindow(QtWidgets.QMainWindow):

    ModellIndex=None
    row = None
    column = None
    old_data_in_cell=None
    model2 = None
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.textChanged.connect(self.check_input_lenght)
        self.ui.textEdit_2.textChanged.connect(self.check_input_lenght)
        self.ui.comboBox.currentIndexChanged.connect(self.set_blocksize)
        self.ui.comboBox_3.currentIndexChanged.connect(self.check_encryption_mode)
        self.ui.tableView_2.doubleClicked.connect(self.check_table_input_size)
        self.ui.tableView.keypressedSignal.connect(self.keypressedTableView)
        self.ui.actionLoad.triggered.connect(self.read_file)
        self.ui.actionSave.triggered.connect(self.save_file)
    @staticmethod
    def bigint_to_bytes(x):
        if x == 0:
            return b""
        else:
            return mywindow.bigint_to_bytes(x // 256) + bytes([x % 256])


    def save_file(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name[0], 'w')
        if self.ui.tableView.model() != None and self.ui.tableView_2.model() != None:
            self.ui.tableView.selectAll()
            text = 'SFC Ciphertext\n'
            for item in self.ui.tableView.selectedIndexes():
                if item.data() != None:
                    text += item.data()
            self.ui.tableView_2.selectAll()
            text +='\nSFC Cleartext\n'
            for item in self.ui.tableView_2.selectedIndexes():
                if item.data() != None:
                    text += item.data()
            file.write(text)
            file.close()
        else:
            QtWidgets.QMessageBox.about(self, "Fehler","Tabelle ist leer.")

    def read_file(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        exported_File = False
        with open(name[0],'r') as file:
            line = file.readline()
            cleartext = False
            cipher_tag='SFC Ciphertext'
            clear_tag ='SFC Cleartext'
            if cipher_tag in line:
                exported_File=True
                data_cipher = ''
                data_clear=''
                while line:
                    line = file.readline()
                    line = line.strip()
                    if clear_tag in line:
                        cleartext = True
                    if not cleartext:
                        data_cipher += line
                    else:
                        if clear_tag not in line:
                            data_clear += line
            else:
                file.seek(0)
                data = file.read()
        if self.ui.tableView.model() != None or self.ui.tableView_2 != None:
            self.ui.tableView.setModel(None)
            self.ui.tableView_2.setModel(None)
        if not exported_File:
            self.insertTables(data)
        else:
            self.table1(data_cipher)
            self.table2(data_clear)



    def check_cell_input(self):
        new_data = self.ModellIndex.data(0)
        # /4 wegen Bits/4 => 16Hex-Ziffern => /2 wegen 1 Buchstabe = 2 Hex-Ziffern
        input_size = ((self.getBlocksize()/4)/2)
        if len(new_data) > input_size:
            index = self.model2.index(self.row,self.column)
            data = new_data[:int(input_size)]
            self.model2.setData(index,data)
            QtWidgets.QMessageBox.about(self,"Fehler","Ihre Eingabe war zu lang und wurde abgeschnitten.")
        if len(new_data) < input_size:
            QtWidgets.QMessageBox.about(self, "Fehler", "Ihre Eingabe war zu kurz und wurde durch den alten Wert ersetzt.")
            index = self.model2.index(self.row, self.column)
            self.model2.setData(index, self.old_data_in_cell)

    def keypressedTableView(self,event):
        if event.matches(QtGui.QKeySequence.Copy):
            self.copydatatoclipboard()
            return True
        if event.matches(QtGui.QKeySequence.Paste):
            clipboard = QApplication.clipboard()
            # Hex-Code Text
            text = clipboard.text()

            if self.ui.tableView.model() == None and self.ui.tableView.hasFocus():
               self.insertTables(text)
        QTableView.keyPressEvent(self.ui.tableView, event)


    def table1(self,data):
        number_of_tupels = (len(data) * 4) / self.getBlocksize()
        n_character = (self.getBlocksize() / 4)
        splittet_input = [(data[i:i + int(n_character)]) for i in range(0, len(data), int(n_character))]
        number, width, height = self.tablesize_and_number(number_of_tupels)
        self.create_table1(height,width,number_of_tupels,splittet_input,number)

    def table2(self,data):
        n_character = (self.getBlocksize() / 4)
        self.ui.tableView.selectAll()
        number_of_tupels=0
        for item in self.ui.tableView.selectedIndexes():
            if item.data() != None:
                number_of_tupels += 1
        number, width, height = self.tablesize_and_number(number_of_tupels)
        question_marks = [(data[i:i + int(n_character / 2)]) for i in range(0, len(data), int(n_character / 2))]
        self.create_table2(height,width,number_of_tupels,question_marks,number)

    def tablesize_and_number(self,number_of_tupels):
        if self.getBlocksize() == 64:
            number = 8
            width, height = self.calculate_tablesize(number, number_of_tupels)
        if self.getBlocksize() == 128:
            number = 4
            width, height = self.calculate_tablesize(number, number_of_tupels)
        return number, width, height

    def create_table1(self,height,width,number_of_tupels,splittet_input,number):
        model = QtGui.QStandardItemModel(height, width, self)
        self.ui.tableView.setModel(model)
        self.inserttableview(model, height, number_of_tupels, splittet_input, number)
        self.ui.tableView.resizeColumnsToContents()

    def create_table2(self,height,width,number_of_tupels,question_marks,number):
        self.model2 = QtGui.QStandardItemModel(height, width, self)
        self.ui.tableView_2.setModel(self.model2)
        self.inserttableview(self.model2, height, number_of_tupels, question_marks, number)
        self.resize_table(width)
        self.model2.itemChanged.connect(self.check_cell_input)

    def insertTables(self,data):
        blocksize = self.getBlocksize()
        number_of_tupels = (len(data) * 4) / blocksize
        n_character = (blocksize / 4)
        splittet_input = [(data[i:i + int(n_character)]) for i in range(0, len(data), int(n_character))]
        question_marks = [("?" * int(n_character / 2)) for i in range(0, len(data), int(n_character / 2))]

        number, width, height = self.tablesize_and_number(number_of_tupels)
        # Ciphertext
        self.create_table1(height,width,number_of_tupels,splittet_input,number)

        # cleartext
        self.create_table2(height,width,number_of_tupels,question_marks,number)



    def check_table_input_size(self, signal):
        self.ModellIndex = signal
        self.row = signal.row()
        self.column = signal.column()
        self.old_data_in_cell = signal.data(0)


    def resize_table(self,width):
        iterate = 0
        while iterate < width:
            self.ui.tableView_2.setColumnWidth(iterate, self.ui.tableView.columnWidth(iterate))
            iterate += 1
    def check_encryption_mode(self):
        if self.ui.comboBox.currentIndex() == 0 and self.ui.comboBox_3.currentIndex() == 1:
            self.ui.comboBox_3.setCurrentIndex(0)
        if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_3.currentIndex() == 0:
            self.ui.comboBox_3.setCurrentIndex(1)

    def set_blocksize(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.ui.comboBox_3.setCurrentIndex(0)
            if self.ui.tableView.model() != None and self.ui.tableView_2.model() != None:
                # AES zu DES wechseln
                self.change_cipher_mode()
                self.ui.textEdit_3.setMinimumHeight(21)
        if self.ui.comboBox.currentIndex() == 1:
            self.ui.comboBox_3.setCurrentIndex(1)
            if self.ui.tableView.model() != None and self.ui.tableView_2.model() != None:
                # DES zu AES wechseln
                self.change_cipher_mode()

    def change_cipher_mode(self):
        self.ui.tableView.selectAll()
        data = ''
        for item in self.ui.tableView.selectedIndexes():
            if item.data() != None:
                data += item.data()
        self.table1(data)
        self.ui.tableView_2.selectAll()
        data = ''
        for item in self.ui.tableView_2.selectedIndexes():
            if item.data() != None:
                data += item.data()
        self.table2(data)

    def check_input_lenght(self):
        blocksize = (self.getBlocksize() / 4)  # /4 wegen Hex
        if self.ui.textEdit.hasFocus():
            textedit = self.ui.textEdit
            Input_lenght = len(textedit.toPlainText().encode())
            input = textedit.toPlainText()
            hexpattern=re.compile('([G-Z])', re.IGNORECASE)
            match = re.search(hexpattern,input)
            if match:
                textedit.setText(input[:-1])
                textedit.moveCursor(QtGui.QTextCursor.End)
        if self.ui.textEdit_2.hasFocus():
            textedit = self.ui.textEdit_2
            Input_lenght = len(textedit.toPlainText().encode())*2
        if Input_lenght > blocksize:
            input = textedit.toPlainText()
            if self.ui.textEdit.hasFocus():
                input = input[:int(blocksize)]
            if self.ui.textEdit_2.hasFocus():
                input = input[:int((blocksize/2))]
            textedit.setText(input)
            textedit.moveCursor(QtGui.QTextCursor.End)


    def generate_gadget(self):
        IV = self.ui.textEdit.toPlainText()
        Input = self.ui.textEdit_2.toPlainText()
        IV_Byte_lenght = len(IV.encode())
        Input_Byte_length = len(Input.encode())*2
        blocksize_in_bytes = (self.getBlocksize()/4)
        tableview = None
        if self.ui.tableView.hasFocus():
            tableview = self.ui.tableView
        if self.ui.tableView_2.hasFocus():
            tableview = self.ui.tableView_2
        if tableview == None:
            return None
        tableViewIndexes = tableview.selectedIndexes()
        if len(tableViewIndexes) == 1:
            data = QtCore.QModelIndex.data(tableViewIndexes[0])
            if blocksize_in_bytes == IV_Byte_lenght and blocksize_in_bytes == Input_Byte_length:
                input_asHex = binascii.hexlify(Input.encode())
                data_asHex = binascii.hexlify(data.encode())
                if self.getBlocksize() == 64:
                    binary_format='064b'
                if self.getBlocksize() == 128:
                    binary_format='0128b'
                iv_data = format(int(bin(int(IV,16))[2:],2),binary_format)
                input_data = format(int(bin(int(input_asHex,16))[2:],2),binary_format)
                cell_data = format(int(bin(int(data_asHex,16))[2:],2),binary_format)
                gadget = int(iv_data,2) ^ int(input_data,2) ^ int(cell_data,2)
                self.ui.textEdit_3.setText(str(binascii.hexlify(self.bigint_to_bytes(gadget)))[2:-1])


            else:
                print("nicht die gleiche länge")
        else:
            print("Mehr als eine Celle ausgewählt")

    def getBlocksize(self):
        if self.ui.comboBox_3.currentIndex() == 0:
            number = 64
        elif self.ui.comboBox_3.currentIndex() == 1:
            number = 128
        return number



    def calculate_tablesize(self, number, number_of_tupels):
        if number_of_tupels < number:
            height = 1
            width = number_of_tupels
        else:
            width = number
            height = math.ceil((number_of_tupels / number))
        return width,height

    def inserttableview(self,model,height,width,input,number):
        counter_was_eight = False
        i = 0
        j=0
        counter=0

        while i < height:

            if counter_was_eight:
                width = width-number
                counter = 0
                counter_was_eight = False
            while counter < width:

                index = model.index(i, counter)
                model.setData(index, input[j])
                j += 1
                counter +=1
                if (counter%number) == 0:
                    counter_was_eight = True
                    break
            i += 1

    def add_item(self):
        if self.ui.textEdit_3.toPlainText().strip() == "":
            QtWidgets.QMessageBox.about(self, "Fehler", "Gadget noch nicht generiert.")
        else:
            data_cipher =''
            data_clear =''
            index = self.ui.tableView.selectedIndexes()
            row = index[0].row()
            column = index[0].column()
            self.ui.tableView.selectAll()
            for item in self.ui.tableView.selectedIndexes():
                if item.data() != None:
                    data_cipher +=item.data()
                if item == index[0]:
                    data_cipher += self.ui.textEdit_3.toPlainText()
            self.ui.tableView_2.selectAll()
            for item in self.ui.tableView_2.selectedIndexes():
                if item.data() != None:
                    data_clear += item.data()
                if item.row() == row and item.column() == column:
                    data_clear += self.ui.textEdit_2.toPlainText()
            self.table1(data_cipher)
            self.table2(data_clear)

    # right-click tabview
    def contextMenuEvent(self, event):
        if event.MouseButtonPress == QtCore.Qt.RightButton and self.ui.tableView.hasFocus() or self.ui.tableView_2.hasFocus():
            menu = QtWidgets.QMenu(self)
            pasteAction = menu.addAction("Paste")
            copyAction = menu.addAction("Copy")
            clearallAction = menu.addAction("Clear all")
            generateGadget = menu.addAction("Generate Gadget")
            add_item = menu.addAction("Add Item with Gadget")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == copyAction:
                self.copydatatoclipboard()
            if action == pasteAction:
                self.pastedata()
            if action == clearallAction:
                self.ui.tableView.setModel(None)
                self.ui.tableView_2.setModel(None)
            if action == generateGadget:
                self.generate_gadget()
            if action == add_item:
                self.add_item()

    def pastedata(self):
        tableview = None
        if self.ui.tableView.hasFocus():
            tableview = self.ui.tableView
        if self.ui.tableView_2.hasFocus():
            tableview = self.ui.tableView_2
        tableViewIndexes = tableview.selectedIndexes()
        if len(tableViewIndexes) == 1:
            self.ModellIndex = tableViewIndexes[0]
            self.row = tableViewIndexes[0].row()
            self.column = tableViewIndexes[0].column()
            self.old_data_in_cell = QtCore.QModelIndex.data(tableViewIndexes[0])
            tableview.model().setData(tableViewIndexes[0],QApplication.clipboard().text())



    def copydatatoclipboard(self):
        tableview= None
        data = ''
        if self.ui.tableView.hasFocus():
            tableview = self.ui.tableView
        if self.ui.tableView_2.hasFocus():
            tableview = self.ui.tableView_2

        tableViewIndexes = tableview.selectedIndexes()
        if len(tableViewIndexes) == 1:
            data = QtCore.QModelIndex.data(tableViewIndexes[0])
        if len(tableViewIndexes) > 1:
            for i in tableViewIndexes:
                data += QtCore.QModelIndex.data(i)
        QApplication.clipboard().clear()
        QApplication.clipboard().setText(data)



app = QApplication(sys.argv)
application = mywindow()
application.show()
sys.exit(app.exec_())