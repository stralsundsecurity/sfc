import csv
import sys

import clipboard as clipboard
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *


class App(QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title = 'Systemsicherheit'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.hotkey = {}

        self.tableWidget = QTableWidget()
        self.tableWidgetPlainText = QTableWidget()

        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")

        self.comboBoxGadget = QComboBox()
        self.comboBoxCipher = QComboBox()
        self.comboBoxBlockSize = QComboBox()
        self.comboBoxEncoding = QComboBox()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)  # set QMainWindow.centralWidget

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createMenu()

        self.shortcut('Copy', 'Ctrl+C', self.copyData)
        self.shortcut('Copy', 'Ctrl+X', self.extractData)
        self.shortcut('Copy', 'Ctrl+V', self.insertData)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.doubleClicked.connect(self.onTableClick)

        self.vboxTableWidgets = QVBoxLayout()
        self.vboxTableWidgets.addWidget(self.tableWidget)
        self.vboxTableWidgets.addWidget(self.tableWidgetPlainText)

        self.comboBoxGadget.addItem("CBC")
        self.comboBoxGadget.addItem("CFB")
        self.comboBoxGadget.activated.connect(self.onSelectGadget)

        self.comboBoxCipher.addItem("AES")
        self.comboBoxCipher.addItem("DES")
        self.comboBoxCipher.activated.connect(self.onSelectChiffre)

        self.comboBoxBlockSize.addItem("64 Bit")
        self.comboBoxBlockSize.addItem("128 Bit")
        self.comboBoxBlockSize.addItem("256 Bit")
        self.comboBoxBlockSize.addItem("512 Bit")
        self.comboBoxGadget.activated.connect(self.onSelectBlockSize)

        self.comboBoxEncoding.addItem("BASE 64")
        self.comboBoxEncoding.addItem("BASE 32")
        self.comboBoxEncoding.addItem("Hex")
        self.comboBoxEncoding.addItem("UTF-8")
        self.comboBoxGadget.activated.connect(self.onSelectEncoding)

        self.vboxComboBox = QVBoxLayout()
        self.vboxComboBox.addWidget(self.comboBoxGadget)
        self.vboxComboBox.addWidget(self.comboBoxCipher)
        self.vboxComboBox.addWidget(self.comboBoxBlockSize)
        self.vboxComboBox.addWidget(self.comboBoxEncoding)
        self.vboxComboBox.addStretch(1)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vboxComboBox)
        self.hbox.addLayout(self.vboxTableWidgets)

        # Add box layout to central widget
        self.central_widget.setLayout(self.hbox)

        self.statusBar().showMessage('')

        # Show widget
        self.show()

    def onSelectGadget(self):
        # Todo
        return None

    def onSelectChiffre(self):
        # Todo
        return None

    def onSelectBlockSize(self):
        # Todo
        return None

    def onSelectEncoding(self):
        # Todo
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
        menuItemAddRow.triggered.connect(self.addRow)
        editMenu.addAction(menuItemAddRow)

        menuItemAddColumn = QAction('Add column', self)
        menuItemAddColumn.setStatusTip('Adds a new column to the right of the selected one.')
        menuItemAddColumn.triggered.connect(self.addColumn)
        editMenu.addAction(menuItemAddColumn)

        menuItemRemoveRow = QAction('Remove row', self)
        menuItemRemoveRow.setStatusTip('Removes the selected row.')
        menuItemRemoveRow.triggered.connect(self.removeRow)
        editMenu.addAction(menuItemRemoveRow)

        menuItemRemoveColumn = QAction('Remove column', self)
        menuItemRemoveColumn.setStatusTip('Removes the selected column.')
        menuItemRemoveColumn.triggered.connect(self.removeColumn)
        editMenu.addAction(menuItemRemoveColumn)

        menuItemConvertToASCII = QAction('Convert to ASCII', self)
        menuItemConvertToASCII.setStatusTip('Converts the table data to ASCII')
        menuItemConvertToASCII.triggered.connect(self.on_menuItemConvertToASCII_clicked)
        viewMenu.addAction(menuItemConvertToASCII)

        menuItemConvertToHEX = QAction('Convert to HEX', self)
        menuItemConvertToHEX.setStatusTip('Converts the table data to HEX')
        menuItemConvertToHEX.triggered.connect(self.on_menuItemConvertToHEX_clicked)
        viewMenu.addAction(menuItemConvertToHEX)

        menuItemAbout = QAction('About', self)
        menuItemAbout.setStatusTip('About the program (Not implemented)')

    def on_menuItemLoad_clicked(self):
        filename = self.openFile()
        self.loadCSV(filename)

    def on_menuItemSave_clicked(self):
        filename = self.saveFile()
        if filename is not None:
            self.writeCsv(filename)

    def on_menuItemConvertToASCII_clicked(self):
        self.convertToASCII()

    def on_menuItemConvertToHEX_clicked(self):
        self.convertToHEX()

    def onTableClick(self):
        """
        Prints cell content on the console

        :return:
        """
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def addRow(self):
        """
        Adds a new row below the selected one.

        :return: None
        """
        self.tableWidget.insertRow(self.tableWidget.currentRow() + 1)

    def addColumn(self):
        """
        Adds a new column to the right of the selected one.
        :return: None
        """
        self.tableWidget.insertColumn(self.tableWidget.currentColumn() + 1)

    def removeRow(self):
        """
        Removes the selected row
        :return: None
        """
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def removeColumn(self):
        """
        Removes the selected column
        :return: None
        """
        self.tableWidget.removeColumn(self.tableWidget.currentColumn())

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

    def copyData(self):
        """
        Copies the data from the selected cells to the system clipboard
        :return: None
        """
        copiedData = ""
        for i in range(self.tableWidget.selectedRanges().pop(0).topRow(),
                       self.tableWidget.selectedRanges().pop(0).bottomRow() + 1):
            for j in range(self.tableWidget.selectedRanges().pop(0).leftColumn(),
                           self.tableWidget.selectedRanges().pop(0).rightColumn() + 1):
                copiedData += self.tableWidget.item(i, j).text() + "\t"
            copiedData += '\n'
        clipboard.copy(copiedData)

    def extractData(self):
        """
        Extracts the data from the selected cells to the system clipboard and fills the cells with empty strings
        :return: None
        """
        copiedData = ""
        for i in range(self.tableWidget.selectedRanges().pop(0).topRow(),
                       self.tableWidget.selectedRanges().pop(0).bottomRow() + 1):
            for j in range(self.tableWidget.selectedRanges().pop(0).leftColumn(),
                           self.tableWidget.selectedRanges().pop(0).rightColumn() + 1):
                copiedData += self.tableWidget.item(i, j).text() + "\t"
                self.tableWidget.setItem(i, j, QTableWidgetItem(""))
            copiedData += '\n'
        clipboard.copy(copiedData)

    def insertData(self):
        """
        Inserts the data from the system clipboard to the selected cell.
        TODO: Fix: When inserting into the last column, the following data is inserted into the initial columns
        :return: None
        """
        data = clipboard.paste().split("\n")

        for i in range(self.tableWidget.selectedRanges().pop(0).topRow(),
                       self.tableWidget.selectedRanges().pop(0).bottomRow() + len(data) - 1):
            tokens = data[i - self.tableWidget.selectedRanges().pop(0).topRow()].strip().split("\t")
            for j in range(self.tableWidget.selectedRanges().pop(0).leftColumn(),
                           self.tableWidget.selectedRanges().pop(0).rightColumn() + len(tokens)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(
                    tokens[j - self.tableWidget.selectedRanges().pop(0).leftColumn()]))

    def loadCSV(self, filename):
        """
        Loads data from a csv file to the table widget
        :param filename: name of the file
        :return: None
        """

        if filename != "":
            infile = open(filename, "r")
            lines = infile.readlines()
            infile.close()
            self.tableWidget.setRowCount(len(lines))
            self.tableWidget.setColumnCount(len(lines[0].strip().split(",")))
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                for j in range(0, len(tokens)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(tokens[j]))
            self.tableWidget.resizeColumnsToContents()

    def writeCsv(self, filename):
        """
        Writes the data from the table widget to a csv file
        :param filename: name of the file
        :return: None
        """
        data = []
        with open(filename, "w", newline='') as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.tableWidget.rowCount()):
                for columnNumber in range(self.tableWidget.columnCount()):
                    data.append(self.tableWidget.item(rowNumber, columnNumber).text())
                writer.writerow(data)
                data = []

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
        action = contextMenu.exec_(self.mapToParent(event.pos()))

        if action == colorAct:
            self.openColorDialog()
        elif action == asciiAct:
            self.convertToASCII()
        elif action == hexAct:
            self.convertToHEX()

    def openColorDialog(self):
        """
        Opens a color dialog to select and set a background color for the selected cells.
        :return:
        """

        color = QColorDialog.getColor()

        if color.isValid():
            for item in self.tableWidget.selectedItems():
                item.setBackground(color)

    def convertToASCII(self):
        """
        Converts the table data to ascii
        :return: None
        """

        for rowNumber in range(self.tableWidget.rowCount()):
            for columnNumber in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(rowNumber, columnNumber, QTableWidgetItem(
                    binascii.unhexlify(self.tableWidget.item(rowNumber, columnNumber).text()).decode('utf8')))

    #
    def convertToHEX(self):
        """
        Converts the table data to hex
        :return: None
        """

        for rowNumber in range(self.tableWidget.rowCount()):
            for columnNumber in range(self.tableWidget.columnCount()):
                binaryData = bytes(self.tableWidget.item(rowNumber, columnNumber).text(), 'utf-8')
                hexData = binaryData.hex()
                self.tableWidget.setItem(rowNumber, columnNumber, QTableWidgetItem(hexData))

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
