import binascii
import csv
import sys
import os

import clipboard as clipboard
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *


class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(CustomTableWidget, self).__init__(parent)

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
        action = contextMenu.exec_(event.globalPos())

        if action == colorAct:
            self.openColorDialog()
        elif action == asciiAct:
            self.convertToASCII()
        elif action == hexAct:
            self.convertToHex()

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

    def removeTableRow(self):
        """
        Removes the selected row
        :return: None
        """
        self.removeRow(self.currentRow())

    def removeTableColumn(self):
        """
        Removes the selected column
        :return: None
        """
        self.removeColumn(self.currentColumn())

    def convertToASCII(self):
        """
        Converts the table data to ascii
        :return: None
        """

        for rowNumber in range(self.rowCount()):
            for columnNumber in range(self.columnCount()):
                if self.item(rowNumber, columnNumber) is not None:
                    self.setItem(rowNumber, columnNumber, QTableWidgetItem(
                        binascii.unhexlify(self.item(rowNumber, columnNumber).text()).decode('utf8')))

    def convertToHex(self):
        """
        Converts the table data to hex
        :return: None
        """

        for rowNumber in range(self.rowCount()):
            for columnNumber in range(self.columnCount()):
                if self.item(rowNumber, columnNumber) is not None:
                    binaryData = bytes(self.item(rowNumber, columnNumber).text(), 'utf-8')
                    hexData = binaryData.hex()
                    self.setItem(rowNumber, columnNumber, QTableWidgetItem(hexData))

    def openColorDialog(self):
        """
        Opens a color dialog to select and set a background color for the selected cells.
        :return:
        """

        color = QColorDialog.getColor()

        if color.isValid():
            for item in self.selectedItems():
                item.setBackground(color)

    def copyData(self):
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
                    copiedData += self.item(i, j).text() + "\t"
            copiedData += '\n'
        clipboard.copy(copiedData)
        self.resizeColumnsToContents()

    def extractData(self):
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
                    extractedData += self.item(i, j).text() + "\t"
                    self.setItem(i, j, QTableWidgetItem(""))
            extractedData += '\n'
        clipboard.copy(extractedData)
        self.resizeColumnsToContents()

    def insertData(self):
        """
        Inserts the data from the system clipboard to the selected cell.
        TODO: Fix: When inserting into the last column, the following data is inserted into the initial columns
        :return: None
        """
        data = clipboard.paste().split("\n")

        for i in range(self.selectedRanges().pop(0).topRow(),
                       self.selectedRanges().pop(0).bottomRow() + len(data) - 1):
            tokens = data[i - self.selectedRanges().pop(0).topRow()].strip().split("\t")
            for j in range(self.selectedRanges().pop(0).leftColumn(),
                           self.selectedRanges().pop(0).rightColumn() + len(tokens)):
                self.setItem(i, j, QTableWidgetItem(
                    tokens[j - self.selectedRanges().pop(0).leftColumn() - 1]))
        self.resizeColumnsToContents()


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
        self.width = 500
        self.height = 500

        self.tableWidgetCipher = CustomTableWidget(parent=self)
        self.tableWidgetPlain = CustomTableWidget(parent=self)

        self.gadget = 'CBC'
        self.cipher = 'AES'
        self.blockSize = 64
        self.encoding = 'utf-8'

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

        self.comboBoxGadget.addItem("CBC")
        self.comboBoxGadget.addItem("CFB")
        self.comboBoxGadget.activated.connect(self.onSelectGadget)

        self.comboBoxCipher.addItem("AES")
        self.comboBoxCipher.addItem("DES")
        self.comboBoxCipher.activated.connect(self.onSelectCipher)

        self.comboBoxBlockSize.addItem("64")
        self.comboBoxBlockSize.addItem("128")
        self.comboBoxBlockSize.addItem("256")
        self.comboBoxBlockSize.addItem("512")
        self.comboBoxBlockSize.activated.connect(self.onSelectBlockSize)

        self.comboBoxEncoding.addItem("BASE 64")
        self.comboBoxEncoding.addItem("BASE 32")
        self.comboBoxEncoding.addItem("Hex")
        self.comboBoxEncoding.addItem("UTF-8")
        self.comboBoxEncoding.activated.connect(self.onSelectEncoding)

        self.labelGadget.setText("Select Gadget:")
        self.labelCipher.setText("Select Cipher:")
        self.labelBlockSize.setText("Select Blocksize:")
        self.labelEncoding.setText("Select Encoding:")

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
            self.tableWidgetCipher.copyData()
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.copyData()

    def extractData(self):
        if self.tableWidgetCipher.hasFocus():
            self.tableWidgetCipher.extractData()
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.extractData()

    def insertData(self):
        if self.tableWidgetCipher.hasFocus():
            self.tableWidgetCipher.insertData()
        elif self.tableWidgetPlain.hasFocus():
            self.tableWidgetPlain.insertData()

    def onSelectGadget(self):
        self.gadget = int(self.comboBoxGadget.currentText())
        return None

    def onSelectCipher(self):
        self.cipher = int(self.comboBoxCipher.currentText())
        return None

    def onSelectBlockSize(self):
        self.blockSize = int(self.comboBoxBlockSize.currentText())
        return None

    def onSelectEncoding(self):
        self.encoding = int(self.comboBoxEncoding.currentText())
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

        menuItemRemoveRow = QAction('Remove row', self)
        menuItemRemoveRow.setStatusTip('Removes the selected row.')
        menuItemRemoveRow.triggered.connect(self.tableWidgetCipher.removeTableRow)
        menuItemRemoveRow.triggered.connect(self.tableWidgetPlain.removeTableRow)
        editMenu.addAction(menuItemRemoveRow)

        menuItemRemoveColumn = QAction('Remove column', self)
        menuItemRemoveColumn.setStatusTip('Removes the selected column.')
        menuItemRemoveColumn.triggered.connect(self.tableWidgetCipher.removeTableColumn)
        menuItemRemoveColumn.triggered.connect(self.tableWidgetPlain.removeTableColumn)
        editMenu.addAction(menuItemRemoveColumn)

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
        with open(filename, 'rb') as f:
            fileSize = os.stat(filename).st_size
            self.tableWidgetCipher.setColumnCount((fileSize / self.blockSize) / 2)
            self.tableWidgetCipher.setRowCount((fileSize / self.blockSize) / 2)
            byte = f.read(self.blockSize)
            while byte != b"":
                for i in range(0, self.tableWidgetCipher.rowCount()):
                    for j in range(0, self.tableWidgetCipher.columnCount()):
                        self.tableWidgetCipher.setItem(i, j, QTableWidgetItem(str(byte)))
                self.tableWidgetCipher.resizeColumnsToContents()
                byte = f.read(self.blockSize)

    def writeFile(self, filename):
        data = []
        with open(filename, "br+", newline='') as fileOutput:
            for rowNumber in range(self.tableWidgetCipher.rowCount()):
                for columnNumber in range(self.tableWidgetCipher.columnCount()):
                    data.append(self.tableWidgetCipher.item(rowNumber, columnNumber).text())
            fileOutput.write(bytes(data))

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
