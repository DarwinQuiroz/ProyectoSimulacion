import sys
from PyQt5.QtWidgets import QApplication, QAction, QMessageBox, QDialog,QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import ctypes
import random, math

__author__ = 'Darwin Fabián Quiroz Baque'
"""
	Materia: Modelo y Simulación
	Profesor: Ing. Jorge Moya
	Curso: Quinto "A" anual
"""
class LineaDeEspera(QDialog):
	"""Contructor de la clase"""
	def __init__(self):
		#inicializar el objeto QMainWindows que ejecuta la aplicación
		QDialog.__init__(self)
		#cargar la interfaz
		uic.loadUi("Interfaces/LineaDeEspera.ui", self)
		self.btnCalcular.setEnabled(False)
		self.CentrarVentana()
		self.CabeceraTabla()
		self.btnIngresar.clicked.connect(self.Ingresar)
		self.btnCalcular.clicked.connect(self.Calcular)
		self.btnLimpiar.clicked.connect(self.LimpiarCampos)


	def CentrarVentana(self):
		resolucion = ctypes.windll.user32
		ancho = resolucion.GetSystemMetrics(0)
		alto = resolucion.GetSystemMetrics(1)
		left = (ancho/2)-(self.frameSize().width()/2)
		top = (alto/2)-(self.frameSize().height()/2)
		self.move(left, top)


	def CabeceraTabla(self):
		fuente = QFont("MS Shell Dlg2", 9, QFont.Bold)
		self.tablaLE.setFont(fuente)
		self.tablaLE.setColumnCount(10)
		self.tablaLE.setHorizontalHeaderLabels(['Evento', 'Llegada', 'Servicio', 'Tiempo Entre\n'+'Llegada', 'Tiempo de\n'+'Servicio', 'Hora de\n'+'Llegada Exacta', 'Hora de\n'+'Iniciación', 'Hora de\n'+'Finalización', 'Tiempos de\n'+'Espera', 'Tiempo en\n'+'Sistema'])


	def Ingresar(self):
		eventos = self.txtEventos.value()
		fila = 0
		if eventos > 0:
			self.btnCalcular.setEnabled(True)
			while fila <= eventos:
				self.tablaLE.insertRow(fila)
				valorEvento = QTableWidgetItem(str(fila))
				valorHLlegada = QTableWidgetItem("0")
				valorHInicio = QTableWidgetItem("0")
				valorHFin = QTableWidgetItem("0")
				valorTEspera = QTableWidgetItem("0")
				valorTSistema = QTableWidgetItem("0")
				self.tablaLE.setItem(fila, 0, valorEvento)
				self.tablaLE.setItem(0, 5, valorHLlegada)
				self.tablaLE.setItem(0, 6, valorHInicio)
				self.tablaLE.setItem(0, 7, valorHFin)
				self.tablaLE.setItem(0, 8, valorTEspera)
				self.tablaLE.setItem(0, 9, valorTSistema)
				fila += 1
		else:
			QMessageBox.warning(self, "Advertencia", "Debe ingresar un número mayor a cero", QMessageBox.Ok)


	def Calcular(self):
		eventos = self.txtEventos.value()
		llegada = self.txtLlegada.value()
		servicio = self.txtServicio.value()
		fila = 0
		if llegada > 0 and servicio > 0:
			while fila < eventos:
				aleatorioLlegada = float(self.tablaLE.item(fila+1, 1).text())
				aleatorioServicio = float(self.tablaLE.item(fila+1, 2).text())
				tiempoLlegada = round((-1/llegada)*math.log(aleatorioLlegada), 4)
				tiempoServicio = round((-1/servicio)*math.log(aleatorioServicio), 4)
				horaLlegada = round(float(self.tablaLE.item(fila, 5).text()) + tiempoLlegada, 4)
				horaInicioServicio = round(float(self.tablaLE.item(fila, 6).text()) + tiempoServicio, 4)
				horaFinServicio = horaInicioServicio + tiempoServicio
				tiempoEspera = round(horaInicioServicio - horaLlegada, 4)
				tiempoSistema = round(tiempoEspera + tiempoServicio, 4)
				valorTLlegada = QTableWidgetItem(str(tiempoLlegada))
				valorTservicio = QTableWidgetItem(str(tiempoServicio))
				valorHLlegada = QTableWidgetItem(str(horaLlegada))
				valorHInicio = QTableWidgetItem(str(horaInicioServicio))
				valorHFin = QTableWidgetItem(str(horaFinServicio))
				valorTEspera = QTableWidgetItem(str(tiempoEspera))
				valorTSistema = QTableWidgetItem(str(tiempoSistema))
				self.tablaLE.setItem(fila+1, 3, valorTLlegada)
				self.tablaLE.setItem(fila+1, 4, valorTservicio)
				self.tablaLE.setItem(fila+1, 5, valorHLlegada)
				self.tablaLE.setItem(fila+1, 6, valorHInicio)
				self.tablaLE.setItem(fila+1, 7, valorHFin)
				self.tablaLE.setItem(fila+1, 8, valorTEspera)
				self.tablaLE.setItem(fila+1, 9, valorTSistema)
				fila += 1
		else:
			QMessageBox.warning(self, "Advertencia", "Debe ingresar valores para la media de llegada y de servicio", QMessageBox.Ok)

	def LimpiarCampos(self):
		self.btnCalcular.setEnabled(False)
		self.txtEventos.setValue(0)
		self.txtLlegada.setValue(0.00)
		self.txtServicio.setValue(0.00)
		# self.tablaLE.clearContents()
		fila = self.tablaLE.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.tablaLE.removeRow(i)