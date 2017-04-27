from pytestqt import qtbot
from gui import *

def test_blank_data(qtbot):
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	qtbot.addWidget(ui)
	qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
	assert ui.alert_label.text() == 'НЕКОРРЕКТНЫЕ ДАННЫЕ'

def test_not_digit_data(qtbot):
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	qtbot.addWidget(ui)
	qtbot.mouseClick(ui.random_pushbutton, QtCore.Qt.LeftButton)
	ui.rates_tablewidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str('asasdasd')))
	qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
	assert ui.alert_label.text() == 'НЕКОРРЕКТНЫЕ ДАННЫЕ'

def test_negative_data(qtbot):
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	qtbot.addWidget(ui)
	qtbot.mouseClick(ui.random_pushbutton, QtCore.Qt.LeftButton)
	ui.rates_tablewidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(-1)))
	qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
	assert ui.alert_label.text() == 'НЕКОРРЕКТНЫЕ ДАННЫЕ'
