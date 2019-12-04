import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)


def clicked1():
	print("Ясно")

def clicked2():
	print("Понятно")

class LayForHello(QWidget):
	"""docstring for LayForHello"""
	def __init__(self, arg):
		super (LayForHello, self).__init__()
		self.QH = QHBoxLayout
		self.QV = QVBoxLayout
		self.lable = QLabel('<h1>Внимание</h1>')

		self.QV.addStretch(1)
		self.QV.addWidget(self.lable)
		self.QV.addStretch(1)

		self.QH.addStretch(1)
		self.QH.addLayout(self.QV)
		self.QH.addStretch(1)

		self.setLayout(self.QH)

		self.show

		a=LayForHello()
		app.exec



def window1():

	app = QApplication(sys.argv)
	window = QWidget() 
	window.setWindowTitle('Внимание') 
	window.setGeometry(100, 100, 280, 100) 
	window.move(60, 15)

	helloMsg = QLabel(LayForHello)

	#helloMsgv = QVBoxLayout
	#helloMsgv

	okbutton = QPushButton("Ясно")	
	ok2button = QPushButton("Понятно")
	

	layoutH = QHBoxLayout()
	layoutH.addWidget(okbutton)
	layoutH.addWidget(ok2button)  

	layoutV = QVBoxLayout()
	layoutV.addStretch(1)
	layoutV.addLayout(layoutH)

	window.setLayout(layoutV)

	window.show()
	sys.exit(app.exec_())	
window1()