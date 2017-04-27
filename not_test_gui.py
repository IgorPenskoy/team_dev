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


def test_normal(qtbot):
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	qtbot.addWidget(ui)
	ui.rates_tablewidget.setRowCount(3)
	ui.rates_tablewidget.setColumnCount(3)
	ui.customers_tablewidget.setColumnCount(3)
	ui.providers_tablewidget.setRowCount(3)
	providers = [30, 40, 20]
	customers = [25, 20, 55]
	rates = [[2, 4, 1], [1, 3, 2], [5, 2, 4]]
	label_result = 'Общие затраты: 125.001'
	item_results = [['-', '-', '30.0'], ['25.0', '-', '15.0'], ['-', '20.0', '-'], ['-', '0.0', '10.0']]
	for i in range(ui.providers_tablewidget.rowCount()):
		ui.providers_tablewidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(providers[i])))
	for i in range(ui.customers_tablewidget.columnCount()):
		ui.customers_tablewidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(customers[i])))
	for i in range(ui.rates_tablewidget.rowCount()):
		for j in range(ui.rates_tablewidget.columnCount()):
			ui.rates_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rates[i][j])))
	qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
	for i in range(ui.rates_tablewidget.rowCount()):
		for j in range(ui.rates_tablewidget.columnCount()):
			assert ui.traffic_tablewidget.item(i, j).text() == item_results[i][j]
	assert ui.commoncosts_label.text() == label_result

def test_one_item(qtbot):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qtbot.addWidget(ui)
    ui.rates_tablewidget.setRowCount(1)
    ui.rates_tablewidget.setColumnCount(1)
    ui.customers_tablewidget.setColumnCount(1)
    ui.providers_tablewidget.setRowCount(1)
    qtbot.mouseClick(ui.random_pushbutton, QtCore.Qt.LeftButton)
    try:
        qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
    except Exception:
        assert 0


def test_ten_items(qtbot):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qtbot.addWidget(ui)
    ui.rates_tablewidget.setRowCount(10)
    ui.rates_tablewidget.setColumnCount(10)
    ui.customers_tablewidget.setColumnCount(10)
    ui.providers_tablewidget.setRowCount(10)
    qtbot.mouseClick(ui.random_pushbutton, QtCore.Qt.LeftButton)
    try:
        qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
    except Exception:
        assert 0


def test_all_zero_items(qtbot):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qtbot.addWidget(ui)
    ui.rates_tablewidget.setRowCount(10)
    ui.rates_tablewidget.setColumnCount(10)
    ui.customers_tablewidget.setColumnCount(10)
    ui.providers_tablewidget.setRowCount(10)
    for i in range(ui.providers_tablewidget.rowCount()):
        ui.providers_tablewidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(0)))
    for i in range(ui.customers_tablewidget.columnCount()):
        ui.customers_tablewidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(0)))
    for i in range(ui.rates_tablewidget.rowCount()):
        for j in range(ui.rates_tablewidget.columnCount()):
            ui.rates_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(0)))
    try:
        qtbot.mouseClick(ui.calculation_pushbutton, QtCore.Qt.LeftButton)
    except Exception:
        assert 0
