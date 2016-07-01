import sys
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import ctypes
from Inventario.Inventario import Inventario
from LineaDeEspera.LineaDeEspera import LineaDeEspera
"""
Clase Principal que ejecuta toda la aplicación
"""
class Main(QMainWindow):#Hereda de QMainnWindows(Costructor de ventanas)
	#Método constructor de la clase Main
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)#Se inicia el objeto QMainWindow
		# self.ui = Ui_MainWindow()#Objeto de la intefaz Principal
		# self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		uic.loadUi("Interfaces/Main.ui", self)
		self.btnAceptar.clicked.connect(self.Abrir)#boton de la interfaz que llama al método Abrir
		#Crear la barra de menú
		menu = self.menuBar()
		info = menu.addMenu("&Acerca de...")
		autor = QAction(QIcon(), "&Autor", self)
		autor.setShortcut("Ctrl+a")
		autor.setStatusTip("Autor")
		autor.triggered.connect(self.Mensaje)
		info.addAction(autor)


	def Mensaje(self):
		#Mensaje que muestra la barra de menú
		QMessageBox.information(self, "Información del Autor", "Autor: Darwin Quiroz "+
			"\n Curso: Quinto 'A'"+
			"\n Materia: Modelo y Simulación \n"
			+"Profesor: Ing. Jorge Moya \n"
			+"Año Lectivo: 2015 - 2016")


	"""Método para abrir el modelo seleccionado desde el combobox"""
	def Abrir(self):
		combo = self.cbbDistribuciones.currentText()
		if combo == "Linea de Espera":
			#Se abre la interfaz para calcular Linea de Espera
			lineaEspera = LineaDeEspera()
			lineaEspera.exec_()
		elif combo == "Inventario":
			#Se abre la interfaz para calcular Inventario
			inventario = Inventario()
			inventario.exec_()


if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)#instacia para iniciar la aplicación
	main = Main()#Objeto de la clase Main
	main.show()#Mostar la ventana
	app.exec_()#Ejecutarla aplicación