import unittest
import sys
from gui import *

class TestGui(unittest.TestCase):
	def test_setupUi(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = Ui_MainWindow()
		ui.setupUi(MainWindow)

	def test_retranslateUi(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = Ui_MainWindow()
		ui.retranslateUi(MainWindow)

if __name__ == '__main__':
    unittest.main()