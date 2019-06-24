import base64
import binascii
import sys
import os

import clipboard as clipboard
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *


class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(CustomTableWidget, self).__init__(parent)
        self.encoding = 'UTF-8'

    def contextMenuEvent(self, event):
        """
        Defines a context menu on the table widget.
        :param event:
        :return: None
        """
        contextMenu = QMenu(self)
        colorAct = contextMenu.addAction("Color")
        asciiAct = contextMenu.addAction("Convert to ASCII")
        hexAct = contextMenu.addAction("Convert to HEX")
        deleteRow = contextMenu.addAction("Delete row")
        deleteColumn = contextMenu.addAction("Delete column")
        action = contextMenu.exec_(event.globalPos())

        if action == colorAct:
            self.openColorDialog()
        elif action == asciiAct:
            self.convertToASCII()
        elif action == hexAct:
            self.convertToHex()
        elif action == deleteRow:
            self.removeRow(self.currentRow())
        elif action == deleteColumn:
            self.removeColumn(self.currentColumn())

    def addTableRow(self):
        """
        Adds a new row below the selected one.

        :return: None
        """
        self.insertRow(self.currentRow() + 1)

    def addTableColumn(self):
        """
        Adds a new column to the right of the selected one.
        :return: None
        """
        self.insertColumn(self.currentColumn() + 1)

    def convertToASCII(self, blockSize):
        """
        Converts the table data to ascii
        :return: None
        """
        data = ""
        if self.encoding != "UTF-8":
            for rowNumber in range(self.rowCount()):
                for columnNumber in range(self.columnCount()):
                    if self.item(rowNumber, columnNumber) is not None:
                        data += self.item(rowNumber, columnNumber).text()
            binaryData = self.decode(data)
            encoded = binaryData.decode('utf8')
            clipboard.copy(encoded)
            self.clearTable()
            self.insertData(blockSize)

    def convertToHex(self, blockSize):

        """
        Converts the table data to hex
        :return: None
        """
        data = ""
        if self.encoding != "Hex":
            for rowNumber in range(self.rowCount()):
                for columnNumber in range(self.columnCount()):
                    if self.item(rowNumber, columnNumber) is not None:
                        data += self.item(rowNumber, columnNumber).text()
            binaryData = self.decode(data)
            encoded = binaryData.hex()
            clipboard.copy(encoded)
            self.clearTable()
            self.insertData(blockSize)

    def convertToBase32(self, blockSize):

        """
        Converts the table data to Base32
        :return: None
        """
        data = ""
        if self.encoding != "Base32":
            for rowNumber in range(self.rowCount()):
                for columnNumber in range(self.columnCount()):
                    if self.item(rowNumber, columnNumber) is not None:
                        data += self.item(rowNumber, columnNumber).text()
            binaryData = self.decode(data)
            encoded = base64.b32encode(binaryData).decode('utf-8')
            clipboard.copy(encoded)
            self.clearTable()
            self.insertData(blockSize)

    def convertToBase64(self, blockSize):

        """
        Converts the table data to Base64
        :return: None
        """
        data = ""
        if self.encoding != "Base64":
            for rowNumber in range(self.rowCount()):
                for columnNumber in range(self.columnCount()):
                    if self.item(rowNumber, columnNumber) is not None:
                        data += self.item(rowNumber, columnNumber).text()
            binaryData = self.decode(data)
            encoded = base64.b64encode(binaryData).decode('utf-8')
            clipboard.copy(encoded)
            self.clearTable()
            self.insertData(blockSize)

    def openColorDialog(self):

        """
        Opens a color dialog to select and set a background color for the selected cells.
        :return:
        """

        color = QColorDialog.getColor()

        if color.isValid():
            for item in self.selectedItems():
                item.setBackground(color)

    def copyData(self, blockSize):

        """
        Copies the data from the selected cells to the system clipboard
        :return: None
        """

        copiedData = ""
        for i in range(self.selectedRanges().pop(0).topRow(),
                       self.selectedRanges().pop(0).bottomRow() + 1):
            for j in range(self.selectedRanges().pop(0).leftColumn(),
                           self.selectedRanges().pop(0).rightColumn() + 1):
                if self.item(i, j) is not None:
                    copiedData += self.item(i, j).text()
                # else:
                #     copiedData += "?" * int(blockSize/8)
        clipboard.copy(copiedData)

    def extractData(self, blockSize):

        """
        Extracts the data from the selected cells to the system clipboard and fills the cells with empty strings
        :return: None
        """

        extractedData = ""
        for i in range(self.selectedRanges().pop(0).topRow(),
                       self.selectedRanges().pop(0).bottomRow() + 1):
            for j in range(self.selectedRanges().pop(0).leftColumn(),
                           self.selectedRanges().pop(0).rightColumn() + 1):
                if self.item(i, j) is not None:
                    extractedData += self.item(i, j).text()
                    self.setItem(i, j, QTableWidgetItem(""))
        clipboard.copy(extractedData)

    def insertData(self, blockSize):

        """
        Inserts the data from the system clipboard to the selected cell.
        //TODO fix paste into a different cell from 1 1 (0 0)
        :return: None
        """
        s = clipboard.paste()
        data = []
        while s:
            data.append(s[:int((blockSize / 8))])
            s = s[int((blockSize / 8)):]

        # topRow = self.selectedRanges().pop(0).topRow()
        # bottomRow = self.selectedRanges().pop(0).bottomRow()
        # leftColumn = self.selectedRanges().pop(0).leftColumn()
        # rightColumn = self.selectedRanges().pop(0).rightColumn()
        self.setColumnCount(4)
        self.setRowCount((len(data) / 4) + 1)
        # self.setRangeSelected(QTableWidgetSelectionRange(topRow, bottomRow
        #                                                  , leftColumn, rightColumn
        #                                                  ), True)
        # for i in range(self.selectedRanges().pop(0).topRow(),
        #                self.selectedRanges().pop(0).bottomRow() + int(len(data)/4) + 1):
        #     for j in range(self.selectedRanges().pop(0).leftColumn(),
        #                    self.columnCount()):
        #         if((j - self.selectedRanges().pop(0).leftColumn()) +
        #           (i - self.selectedRanges().pop(0).topRow()) * self.columnCount()) < len(data):
        #             index = (j - self.selectedRanges().pop(0).leftColumn()) + (i - self.selectedRanges().pop(0).topRow()) * self.columnCount()
        #             self.setItem(i, j, QTableWidgetItem(
        #                 data[index]))
        #     self.setRangeSelected(QTableWidgetSelectionRange(self.selectedRanges().pop(0).topRow(),
        #           self.selectedRanges().pop(0).bottomRow(), 0, self.selectedRanges().pop(0).rightColumn()), True)

        for i in range(self.selectedRanges().pop(0).topRow(),
                       self.selectedRanges().pop(0).bottomRow() + int(len(data) / 4) + 1):
            for j in range(self.selectedRanges().pop(0).leftColumn(),
                           self.columnCount()):
                if (j + i * self.columnCount()) < len(data):
                    index = j + i * self.columnCount()
                    self.setItem(i, j, QTableWidgetItem(
                        data[index]))

    def changeBlockSize(self, blockSize):
        self.setRangeSelected(QTableWidgetSelectionRange(0, 0, self.rowCount() - 1, self.columnCount() - 1), True)
        self.extractData(blockSize)
        self.insertData(blockSize)

    def clearTable(self):
        """
        Removes all data from the table.
        :return:
        """

        self.setRangeSelected(QTableWidgetSelectionRange(0, 0, self.rowCount() - 1, self.columnCount() - 1), True)
        for i in range(self.selectedRanges().pop(0).topRow(),
                       self.selectedRanges().pop(0).bottomRow() + 1):
            for j in range(self.selectedRanges().pop(0).leftColumn(),
                           self.selectedRanges().pop(0).rightColumn() + 1):
                self.setItem(i, j, QTableWidgetItem(""))

    def insertQuestionmarks(self, tableWidgetCipher, blockSize):

        s = clipboard.paste()
        s = "?" * len(s)
        data = []
        while s:
            data.append(s[:int((blockSize / 8))])
            s = s[int((blockSize / 8)):]

        self.setColumnCount(4)
        self.setRowCount((len(data) / 4) + 1)

        for i in range(tableWidgetCipher.selectedRanges().pop(0).topRow(),
                       tableWidgetCipher.selectedRanges().pop(0).bottomRow() + len(data) - 1):
            for j in range(tableWidgetCipher.selectedRanges().pop(0).leftColumn(),
                           self.columnCount()):
                if (j + i * self.columnCount()) < len(data):
                    index = j + i * self.columnCount()
                    self.setItem(i, j, QTableWidgetItem(
                        data[index]))

    def getKnownPlain(self):
        """
        :return:
        """

        data = ""
        for rowNumber in range(self.rowCount()):
            for columnNumber in range(self.columnCount()):
                if self.item(rowNumber, columnNumber) is not None and "?" not in self.item(rowNumber,
                                                                                           columnNumber).text():
                    data = self.item(rowNumber, columnNumber).text()
                    break
        binaryData = self.decode(data)
        return binaryData, rowNumber, columnNumber

    def getCipher(self, rowNumber, columnNumber):
        """
        :return:
        """
        if columnNumber == 0:
            rowNumber = rowNumber - 1
            columnNumber = columnNumber + 4
        data = self.item(rowNumber, columnNumber - 1).text()
        binaryData = self.decode(data)
        return binaryData

    def decode(self, data):
        if self.encoding == 'UTF-8':
            binaryData = bytes(data, 'UTF-8')
        elif self.encoding == 'Hex':
            binaryData = binascii.unhexlify(data.encode('utf-8'))
        elif self.encoding == 'Base32':
            binaryData = base64.b32decode(data)
        elif self.encoding == 'Base64':
            if "=" in data:
                data.replace("=", "")
            binaryData = base64.b64decode(data)
        return binaryData


class App(QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.hotkey = {}
        self.vboxTableWidgets = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vboxComboBox = QVBoxLayout()
        self.title = 'Systemsicherheit'
        self.left = 0
        self.top = 0
        self.width = 550
        self.height = 500

        self.tableWidgetCipher = CustomTableWidget(parent=self)
        self.tableWidgetCipher.setColumnCount(4)
        self.tableWidgetCipher.setRowCount(5)
        self.tableWidgetPlain = CustomTableWidget(parent=self)
        self.tableWidgetPlain.setColumnCount(4)
        self.tableWidgetPlain.setRowCount(5)

        self.gadget = 'CBC'
        self.x = b""
        self.cipher = 'AES'
        self.blockSize = 64

        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")

        self.comboBoxGadget = QComboBox()
        self.comboBoxCipher = QComboBox()
        self.comboBoxBlockSize = QComboBox()
        self.comboBoxEncoding = QComboBox()

        self.labelGadget = QLabel(self)
        self.labelCipher = QLabel(self)
        self.labelBlockSize = QLabel(self)
        self.labelEncoding = QLabel(self)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)  # set QMainWindow.centralWidget

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createMenu()

        self.tableWidgetCipher.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetPlain.horizontalHeader().setStretchLastSection(True)

        self.vboxTableWidgets.addWidget(self.tableWidgetCipher)
        self.vboxTableWidgets.addWidget(self.tableWidgetPlain)

        self.labelGadget.setText("Select Gadget:")
        self.comboBoxGadget.addItem("CBC")
        self.comboBoxGadget.addItem("CFB")
        self.comboBoxGadget.activated.connect(self.onSelectGadget)

        self.labelCipher.setText("Select Cipher:")
        self.comboBoxCipher.addItem("AES")
        self.comboBoxCipher.addItem("DES")
        self.comboBoxCipher.activated.connect(self.onSelectCipher)

        self.labelBlockSize.setText("Select Blocksize:")
        self.comboBoxBlockSize.addItem("64")
        self.comboBoxBlockSize.addItem("128")
        self.comboBoxBlockSize.addItem("256")
        self.comboBoxBlockSize.addItem("512")
        self.comboBoxBlockSize.activated.connect(self.onSelectBlockSize)

        self.labelEncoding.setText("Select Encoding:")
        self.comboBoxEncoding.addItem("UTF-8")
        self.comboBoxEncoding.addItem("Hex")
        self.comboBoxEncoding.addItem("Base32")
        self.comboBoxEncoding.addItem("Base64")
        self.comboBoxEncoding.activated.connect(self.onSelectEncoding)

        self.vboxComboBox.addWidget(self.labelGadget)
        self.vboxComboBox.addWidget(self.comboBoxGadget)
        self.vboxComboBox.addWidget(self.labelCipher)
        self.vboxComboBox.addWidget(self.comboBoxCipher)
        self.vboxComboBox.addWidget(self.labelBlockSize)
        self.vboxComboBox.addWidget(self.comboBoxBlockSize)
        self.vboxComboBox.addWidget(self.labelEncoding)
        self.vboxComboBox.addWidget(self.comboBoxEncoding)
        self.vboxComboBox.addStretch(1)

        self.hbox.addLayout(self.vboxComboBox)
        self.hbox.addLayout(self.vboxTableWidgets)

        # Add box layout to central widget
        self.central_widget.setLayout(self.hbox)

        self.statusBar().showMessage('')

        self.shortcut('Copy', 'Ctrl+C', self.copyData)
        self.shortcut('Extract', 'Ctrl+X', self.extractData)
        self.shortcut('Paste', 'Ctrl+V', self.insertData)

        # Show widget
        self.show()

    def shortcut(self, key_name, key_combo, func):
        """
        Adds a shortcut for a key combination and the function
        :param key_name: Name of the shortcut
        :param key_combo: Key combination
        :param func: function name you want to call with the shortcut
        :return:
        """
        self.hotkey[key_name] = QtWidgets.QShortcut(QtGui.QKeySequence(key_combo), self)
        self.hotkey[key_name].activated.connect(func)
        self.hotkey[key_name].setContext(1)

    def copyData(self):
        if self.tableWidgetCipher.hasFocus():
            self.tableWidgetCipher.copyData(self.blockSize)
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.copyData(self.blockSize)

    def extractData(self):
        if self.tableWidgetCipher.hasFocus():
            self.tableWidgetCipher.extractData(self.blockSize)
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.extractData(self.blockSize)

    def insertData(self):
        if self.tableWidgetCipher.hasFocus():
            self.tableWidgetCipher.insertData(self.blockSize)
            self.tableWidgetPlain.insertQuestionmarks(self.tableWidgetCipher, self.blockSize)
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.insertData(self.blockSize)

    def onSelectGadget(self):
        self.gadget = self.comboBoxGadget.currentText()
        self.searchGadget()
        return None

    def onSelectCipher(self):
        self.cipher = self.comboBoxCipher.currentText()
        return None

    def onSelectBlockSize(self):
        self.blockSize = int(self.comboBoxBlockSize.currentText())
        self.tableWidgetCipher.changeBlockSize(self.blockSize)
        self.tableWidgetPlain.changeBlockSize(self.blockSize)
        return None

    def onSelectEncoding(self):
        encoding = self.comboBoxEncoding.currentText()

        if encoding == "UTF-8":
            self.tableWidgetCipher.convertToASCII(self.blockSize)
            # self.tableWidgetCipher.convertToASCII(self.blockSize)
        elif encoding == "Hex":
            self.tableWidgetCipher.convertToHex(self.blockSize)
            # self.tableWidgetCipher.convertToHex(self.blockSize)
        elif encoding == "Base32":
            self.tableWidgetCipher.convertToBase32(self.blockSize)
            # self.tableWidgetCipher.convertToBase32(self.blockSize)
        elif encoding == "Base64":
            self.tableWidgetCipher.convertToBase64(self.blockSize)
            # self.tableWidgetCipher.convertToBase64(self.blockSize)

        self.tableWidgetCipher.encoding = encoding
        self.tableWidgetPlain.encoding = encoding
        return None

    def createMenu(self):

        """
        Creates a menu bar and the menu items.
        :return: None
        """
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        editMenu = mainMenu.addMenu('&Edit')
        viewMenu = mainMenu.addMenu('&View')
        helpMenu = mainMenu.addMenu('&Help')

        menuItemLoad = QAction('Load', self)
        menuItemLoad.setStatusTip('Load data from csv file')
        menuItemLoad.triggered.connect(self.on_menuItemLoad_clicked)
        fileMenu.addAction(menuItemLoad)

        menuItemSave = QAction('Save', self)
        menuItemSave.setStatusTip('Save data to csv file')
        menuItemSave.triggered.connect(self.on_menuItemSave_clicked)
        fileMenu.addAction(menuItemSave)

        menuItemExit = QAction('Exit', self)
        menuItemExit.setShortcut('Ctrl+Q')
        menuItemExit.setStatusTip('Exit application')
        menuItemExit.triggered.connect(self.close)
        fileMenu.addAction(menuItemExit)

        menuItemAddRow = QAction('Add row', self)
        menuItemAddRow.setStatusTip(' Adds a new row below the selected one.')
        menuItemAddRow.triggered.connect(self.tableWidgetCipher.addTableRow)
        menuItemAddRow.triggered.connect(self.tableWidgetPlain.addTableRow)
        editMenu.addAction(menuItemAddRow)

        menuItemAddColumn = QAction('Add column', self)
        menuItemAddColumn.setStatusTip('Adds a new column to the right of the selected one.')
        menuItemAddColumn.triggered.connect(self.tableWidgetCipher.addTableColumn)
        menuItemAddColumn.triggered.connect(self.tableWidgetPlain.addTableColumn)
        editMenu.addAction(menuItemAddColumn)

        menuItemConvertToASCII = QAction('Convert to ASCII', self)
        menuItemConvertToASCII.setStatusTip('Converts the table data to ASCII')
        menuItemConvertToASCII.triggered.connect(self.tableWidgetCipher.convertToASCII)
        menuItemConvertToASCII.triggered.connect(self.tableWidgetPlain.convertToASCII)
        viewMenu.addAction(menuItemConvertToASCII)

        menuItemConvertToHEX = QAction('Convert to HEX', self)
        menuItemConvertToHEX.setStatusTip('Converts the table data to HEX')
        menuItemConvertToHEX.triggered.connect(self.tableWidgetCipher.convertToHex)
        menuItemConvertToHEX.triggered.connect(self.tableWidgetPlain.convertToHex)
        viewMenu.addAction(menuItemConvertToHEX)

        menuItemAbout = QAction('About', self)
        menuItemAbout.setStatusTip('About the program (Not implemented)')

    def on_menuItemLoad_clicked(self):
        filename = self.openFile()
        self.loadFile(filename)

    def on_menuItemSave_clicked(self):
        filename = self.saveFile()
        if filename is not None:
            self.writeFile(filename)

    # def loadCSV(self, filename):
    #     """
    #     Loads data from a csv file to the table widget
    #     :param filename: name of the file
    #     :return: None
    #     """
    #
    #     if filename != "":
    #         infile = open(filename, "r")
    #         lines = infile.readlines()
    #         infile.close()
    #         self.tableWidgetCipher.setRowCount(len(lines))
    #         self.tableWidgetCipher.setColumnCount(len(lines[0].strip().split(",")))
    #         for i in range(0, len(lines)):
    #             tokens = lines[i].strip().split(",")
    #             for j in range(0, len(tokens)):
    #                 self.tableWidgetCipher.setItem(i, j, QTableWidgetItem(tokens[j]))
    #         self.tableWidgetCipher.resizeColumnsToContents()

    def loadFile(self, filename):
        if (filename is not None) and (filename != ""):
            with open(filename, 'rb') as f:
                fileSize = os.stat(filename).st_size
                self.tableWidgetCipher.setColumnCount((fileSize / (self.blockSize / 8) + 1) / 2)
                self.tableWidgetCipher.setRowCount(fileSize / (self.blockSize / 8) / 2)
                byte = f.read(self.blockSize)
                row = 0
                column = 0
                while byte != b"":
                    self.tableWidgetCipher.setItem(row, column, QTableWidgetItem(byte.decode('utf-8')))
                    if column >= self.tableWidgetCipher.columnCount():
                        row += 1
                        column = 0
                    else:
                        column += 1
                    byte = f.read(self.blockSize)

    def writeFile(self, filename):
        with open(filename, "wb") as fileOutput:
            for rowNumber in range(self.tableWidgetCipher.rowCount()):
                for columnNumber in range(self.tableWidgetCipher.columnCount()):
                    if self.tableWidgetCipher.item(rowNumber, columnNumber) is not None:
                        fileOutput.write(self.tableWidgetCipher.item(rowNumber, columnNumber).text().encode('utf-8'))

    # def writeCsv(self, filename):
    #    """
    #    Writes the data from the table widget to a csv file
    #    :param filename: name of the file
    #    :return: None
    #    """
    #    data = []
    #    with open(filename, "w", newline='') as fileOutput:
    #        writer = csv.writer(fileOutput)
    #        for rowNumber in range(self.tableWidgetCipher.rowCount()):
    #            for columnNumber in range(self.tableWidgetCipher.columnCount()):
    #                data.append(self.tableWidgetCipher.item(rowNumber, columnNumber).text())
    #            writer.writerow(data)
    #            data = []

    def openFile(self):
        """
        Opens fileDialog
        :return: filename
        """

        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            return filename

    def saveFile(self):
        """
        Opens fileDialog
        :return: filename
        """

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if filename:
            return filename

    def searchGadget(self):
        """
        //TODO
        :return:
        """
        plain, rowNumber, columnNumber = self.tableWidgetPlain.getKnownPlain()
        cipher = self.tableWidgetCipher.getCipher(rowNumber, columnNumber)
        print(plain)
        print(cipher)
        print(self.encrypt(plain, cipher))
        self.x = self.encrypt(plain, cipher)

    def encrypt(self, plain, cipher):
        int_var = int.from_bytes(plain, sys.byteorder)
        int_key = int.from_bytes(cipher, sys.byteorder)
        int_enc = int_var ^ int_key
        return int_enc.to_bytes(len(plain), sys.byteorder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
