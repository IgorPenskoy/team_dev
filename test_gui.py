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
		pass

if __name__ == '__main__':
    unittest.main()