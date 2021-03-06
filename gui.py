from PyQt5 import QtCore, QtGui,QtWidgets
from problem import *
import random
import matplotlib.pyplot as plt
import networkx as nx

##@brief A class for form window
#
class Ui_MainWindow(object):
	## Place elements on form, connect events and holders
	#
	#@param self class pointer
	#@param MainWindow a window instance
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(1200, 500)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.rates_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
		self.rates_tablewidget.setGeometry(QtCore.QRect(10, 40, 201, 192))
		self.rates_tablewidget.setRowCount(3)
		self.rates_tablewidget.setColumnCount(3)
		self.rates_tablewidget.setObjectName("rates_tablewidget")
		self.rates_tablewidget.horizontalHeader().setDefaultSectionSize(40)
		self.rates_tablewidget.horizontalHeader().setMinimumSectionSize(40)
		self.rates_tablewidget.verticalHeader().setDefaultSectionSize(40)
		self.rates_tablewidget.verticalHeader().setMinimumSectionSize(40)
		self.providers_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
		self.providers_tablewidget.setGeometry(QtCore.QRect(230, 40, 81, 192))
		self.providers_tablewidget.setRowCount(3)
		self.providers_tablewidget.setColumnCount(1)
		self.providers_tablewidget.setObjectName("providers_tablewidget")
		self.providers_tablewidget.horizontalHeader().setVisible(True)
		self.providers_tablewidget.horizontalHeader().setDefaultSectionSize(40)
		self.providers_tablewidget.horizontalHeader().setMinimumSectionSize(40)
		self.providers_tablewidget.verticalHeader().setVisible(True)
		self.providers_tablewidget.verticalHeader().setDefaultSectionSize(40)
		self.providers_tablewidget.verticalHeader().setMinimumSectionSize(40)
		self.customers_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
		self.customers_tablewidget.setGeometry(QtCore.QRect(10, 268, 201, 91))
		self.customers_tablewidget.setRowCount(1)
		self.customers_tablewidget.setColumnCount(3)
		self.customers_tablewidget.setObjectName("customers_tablewidget")
		self.customers_tablewidget.horizontalHeader().setVisible(True)
		self.customers_tablewidget.horizontalHeader().setDefaultSectionSize(40)
		self.customers_tablewidget.horizontalHeader().setMinimumSectionSize(40)
		self.customers_tablewidget.verticalHeader().setVisible(True)
		self.customers_tablewidget.verticalHeader().setDefaultSectionSize(40)
		self.customers_tablewidget.verticalHeader().setMinimumSectionSize(40)
		self.traffic_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
		self.traffic_tablewidget.setGeometry(QtCore.QRect(327, 40, 191, 192))
		self.traffic_tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.traffic_tablewidget.setRowCount(3)
		self.traffic_tablewidget.setColumnCount(3)
		self.traffic_tablewidget.setObjectName("traffic_tablewidget")
		self.traffic_tablewidget.horizontalHeader().setDefaultSectionSize(40)
		self.traffic_tablewidget.horizontalHeader().setMinimumSectionSize(40)
		self.traffic_tablewidget.verticalHeader().setDefaultSectionSize(40)
		self.traffic_tablewidget.verticalHeader().setMinimumSectionSize(40)
		self.rates_lable = QtWidgets.QLabel(self.centralwidget)
		self.rates_lable.setGeometry(QtCore.QRect(85, 19, 56, 17))
		self.rates_lable.setObjectName("rates_lable")
		self.calculation_pushbutton = QtWidgets.QPushButton(self.centralwidget)
		self.calculation_pushbutton.setGeometry(QtCore.QRect(220, 300, 181, 27))
		self.calculation_pushbutton.setObjectName("calculation_pushbutton")
		self.random_pushbutton = QtWidgets.QPushButton(self.centralwidget)
		self.random_pushbutton.setGeometry(QtCore.QRect(220, 270, 181, 27))
		self.random_pushbutton.setObjectName("random_pushbutton")
		self.commoncosts_label = QtWidgets.QLabel(self.centralwidget)
		self.commoncosts_label.setGeometry(QtCore.QRect(220, 330, 300, 17))
		self.commoncosts_label.setObjectName("commoncosts_label")
		self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.layoutWidget.setGeometry(QtCore.QRect(42, 235, 150, 29))
		self.layoutWidget.setObjectName("layoutWidget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.customers_label = QtWidgets.QLabel(self.layoutWidget)
		self.customers_label.setObjectName("customers_label")
		self.horizontalLayout_2.addWidget(self.customers_label)
		self.customers_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
		self.customers_spinbox.setMinimum(1)
		self.customers_spinbox.setMaximum(10)
		self.customers_spinbox.setProperty("value", 3)
		self.customers_spinbox.setObjectName("customers_spinbox")
		self.horizontalLayout_2.addWidget(self.customers_spinbox)
		self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
		self.layoutWidget1.setGeometry(QtCore.QRect(220, 10, 108, 29))
		self.layoutWidget1.setObjectName("layoutWidget1")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.providers_label = QtWidgets.QLabel(self.layoutWidget1)
		self.providers_label.setObjectName("providers_label")
		self.horizontalLayout.addWidget(self.providers_label)
		self.providers_spinbox = QtWidgets.QSpinBox(self.layoutWidget1)
		self.providers_spinbox.setMinimum(1)
		self.providers_spinbox.setMaximum(10)
		self.providers_spinbox.setProperty("value", 3)
		self.providers_spinbox.setObjectName("providers_spinbox")
		self.horizontalLayout.addWidget(self.providers_spinbox)
		self.traffic_label = QtWidgets.QLabel(self.centralwidget)
		self.traffic_label.setGeometry(QtCore.QRect(390, 16, 71, 20))
		self.traffic_label.setObjectName("traffic_label")
		self.alert_label = QtWidgets.QLabel(self.centralwidget)
		self.alert_label.setGeometry(QtCore.QRect(220, 350, 200, 20))
		self.alert_label.setText("")
		self.pic = QtWidgets.QLabel(self.centralwidget)
		self.pic.setGeometry(QtCore.QRect(550, 10, 1100, 500))
		self.rates_lable.setObjectName("pic")
		self.alert_label.setObjectName("alert_label")
		self.layoutWidget.raise_()
		self.layoutWidget.raise_()
		self.rates_tablewidget.raise_()
		self.providers_tablewidget.raise_()
		self.customers_tablewidget.raise_()
		self.traffic_tablewidget.raise_()
		self.rates_lable.raise_()
		self.traffic_label.raise_()
		self.calculation_pushbutton.raise_()
		self.random_pushbutton.raise_()
		self.commoncosts_label.raise_()
		self.alert_label.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.providers_spinbox.valueChanged.connect(self.providers_count_change)
		self.customers_spinbox.valueChanged.connect(self.customers_count_change)
		self.random_pushbutton.clicked.connect(self.random_fill)
		self.calculation_pushbutton.clicked.connect(self.calculation)

	## Change a digit in providers edit holder
	#
	#@param self class pointer
	def providers_count_change(self):
		self.providers_tablewidget.setRowCount(self.providers_spinbox.value())
		self.rates_tablewidget.setRowCount(self.providers_spinbox.value())
		self.traffic_tablewidget.setRowCount(self.providers_spinbox.value())

	## Change a digit in customers edit holder
	#
	#@param self class pointer
	def customers_count_change(self):
		self.customers_tablewidget.setColumnCount(self.customers_spinbox.value())
		self.rates_tablewidget.setColumnCount(self.customers_spinbox.value())
		self.traffic_tablewidget.setColumnCount(self.customers_spinbox.value())
		
	## Click on random fill button holder
	#
	#@param self class pointer
	def random_fill(self):
		self.providers_tablewidget.setRowCount(self.providers_spinbox.value())
		self.rates_tablewidget.setRowCount(self.providers_spinbox.value())
		self.traffic_tablewidget.setRowCount(self.providers_spinbox.value())
		self.customers_tablewidget.setColumnCount(self.customers_spinbox.value())
		self.rates_tablewidget.setColumnCount(self.customers_spinbox.value())
		self.traffic_tablewidget.setColumnCount(self.customers_spinbox.value())
		self.rates_tablewidget.setRowCount(self.providers_tablewidget.rowCount())
		self.rates_tablewidget.setColumnCount(self.customers_tablewidget.columnCount())
		for i in range(self.traffic_tablewidget.rowCount()):
			for j in range(self.traffic_tablewidget.columnCount()):
				self.traffic_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem('-'))
		for i in range(self.providers_tablewidget.rowCount()):
			self.providers_tablewidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(random.randint(1, 100))))
		for i in range(self.customers_tablewidget.columnCount()):
			self.customers_tablewidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(random.randint(1, 100))))
		for i in range(self.rates_tablewidget.rowCount()):
			for j in range(self.rates_tablewidget.columnCount()):
				self.rates_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(random.randint(1, 10))))
	
	## Check input data
	#
	#@param self class pointer
	def data_check(self):
		flag = True
		for i in range(self.providers_tablewidget.rowCount()):
			try:
				numb = float(self.providers_tablewidget.item(i, 0).text())
				if numb < 0:
					flag = False
			except ValueError:
				flag = False
			except TypeError:
				flag = False
			except AttributeError:
				flag = False
		for i in range(self.customers_tablewidget.columnCount()):
			try:
				numb = float(self.customers_tablewidget.item(0, i).text())
				if numb < 0:
					flag = False
			except ValueError:
				flag = False
			except TypeError:
				flag = False
			except AttributeError:
				flag = False
		for i in range(self.rates_tablewidget.rowCount()):
			for j in range(self.rates_tablewidget.columnCount()):
				try:
					numb = float(self.rates_tablewidget.item(i, j).text())
					if numb < 0:
						flag = False
				except ValueError:
					flag = False
				except TypeError:
					flag = False
				except AttributeError:
					flag = False
		return flag
		
	## Draw transportation graph
	#
	#@param self class pointer
	def graph(self, problem):
		G = nx.Graph()
		for i in range(problem.height + problem.width):
			G.add_node(i)
		pos = nx.spring_layout(G)
		node_list_providers = list()
		labels = dict()
		for i in range(problem.height):
			labels[i] = str(i + 1)
			node_list_providers.append(i)

		node_list_customers = list()
		for i in range(problem.height, problem.height + problem.width):
			labels[i] = str(i - problem.height + 1)
			node_list_customers.append(i)

		edge_list = list()
		edge_labels_list = dict()
		for i in range(problem.height):
			for j in range(problem.width):
				if problem.table[i][j].supply is not None:
					edge_list.append((i, j + problem.height))
					edge_labels_list[(i, j + problem.height)] = str(problem.table[i][j].supply)

		# nodes
		nx.draw_networkx_nodes(G,pos, nodelist=node_list_providers, node_color='r', node_size=100, alpha=0.8)
		nx.draw_networkx_nodes(G,pos, nodelist=node_list_customers, node_color='b', node_size=100, alpha=0.8)

		# labels
		nx.draw_networkx_labels(G,pos,labels,font_size=12, font_color='k', font_weight='bold')

		#edges
		nx.draw_networkx_edges(G,pos,edgelist=edge_list,arrows=True, style = 'dashed')

		#edge labels
		nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels_list)
		plt.axis("off")
		plt.savefig("traffic.png")
		plt.clf()
		pixmap = QtGui.QPixmap("traffic.png")
		self.pic.setPixmap(pixmap)

	## Click on calculation buuton holder
	#
	#@param self class pointer
	def calculation(self):
		self.alert_label.setText("")
		rates = list()
		providers = list()
		customers = list()
		if self.data_check():
			for i in range(self.providers_tablewidget.rowCount()):
				providers.append(float(self.providers_tablewidget.item(i, 0).text()))
			for i in range(self.customers_tablewidget.columnCount()):
				customers.append(float(self.customers_tablewidget.item(0, i).text()))
			for i in range(self.rates_tablewidget.rowCount()):
				tmp = list()
				for j in range(self.rates_tablewidget.columnCount()):
					tmp.append(float(self.rates_tablewidget.item(i, j).text()))
				rates.append(tmp)
			problem = Problem(customers, providers, rates)
			problem.solve()
			self.traffic_tablewidget.setRowCount(problem.height)
			self.traffic_tablewidget.setColumnCount(problem.width)
			for i in range(self.traffic_tablewidget.rowCount()):
				for j in range(self.traffic_tablewidget.columnCount()):
					if problem.table[i][j].supply is None:
						self.traffic_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem('-'))
					else:
						self.traffic_tablewidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(problem.table[i][j].supply)))
			if problem.width > self.rates_tablewidget.columnCount():
				self.rates_tablewidget.setColumnCount(problem.width)
				for i in range(self.rates_tablewidget.rowCount()):
					self.rates_tablewidget.setItem(i, problem.width - 1, QtWidgets.QTableWidgetItem('0'))
				self.customers_tablewidget.setColumnCount(problem.width)
				self.customers_tablewidget.setItem(0, problem.width - 1, QtWidgets.QTableWidgetItem(str(problem.customers[problem.width - 1])))
			if problem.height > self.rates_tablewidget.rowCount():
				self.rates_tablewidget.setRowCount(problem.height)
				for i in range(self.rates_tablewidget.columnCount()):
					self.rates_tablewidget.setItem(problem.height - 1, i, QtWidgets.QTableWidgetItem('0'))
				self.providers_tablewidget.setRowCount(problem.height)
				self.providers_tablewidget.setItem(0, problem.height - 1, QtWidgets.QTableWidgetItem(str(problem.providers[problem.height - 1])))
			self.commoncosts_label.setText('Общие затраты: ' + str(problem.common_costs))
			self.graph(problem)
		else:
			self.alert_label.setText("НЕКОРРЕКТНЫЕ ДАННЫЕ")

	## Set labels for objects ob form
	#
	#@param self class pointer
	#@param MainWindow a window instance
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Транспортная задача"))
		self.rates_lable.setText(_translate("MainWindow", "Тарифы"))
		self.calculation_pushbutton.setText(_translate("MainWindow", "Вычислить"))
		self.random_pushbutton.setText(_translate("MainWindow", "Случайное заполнение"))
		self.commoncosts_label.setText(_translate("MainWindow", "Общие затраты: "))
		self.customers_label.setText(_translate("MainWindow", "Потребности"))
		self.providers_label.setText(_translate("MainWindow", "Запасы"))
		self.traffic_label.setText(_translate("MainWindow", "Перевозки"))
