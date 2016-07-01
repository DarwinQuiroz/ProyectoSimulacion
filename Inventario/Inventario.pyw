import sys
from PyQt5.QtWidgets import QApplication, QAction, QMessageBox, QDialog,QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import ctypes

__author__ = 'Darwin Fabián Quiroz Baque'
"""
	Materia: Modelo y Simulación
	Profesor: Ing. Jorge Moya
	Curso: Quinto "A" anual
"""
class Inventario(QDialog):
	"""docstring for Inventario"""
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("Interfaces/Inventario.ui", self)
		self.btnCalcular.setEnabled(False)
		self.CentrarVentana()
		self.CabeceraTabla()
		self.btnIngresar.clicked.connect(self.Ingresar)
		self.btnDemanda.clicked.connect(self.CalcularDemandaSemanal)
		self.btnRetraso.clicked.connect(self.CalcularRetrasoDespacho)
		self.btnCalcular.clicked.connect(self.Calcular)
		self.btnNuevo.clicked.connect(self.LimpiarCampos)


	def CentrarVentana(self):
		resolucion = ctypes.windll.user32
		ancho = resolucion.GetSystemMetrics(0)
		alto = resolucion.GetSystemMetrics(1)
		left = (ancho/2)-(self.frameSize().width()/2)
		top = (alto/2)-(self.frameSize().height()/2)
		self.move(left, top)


	def CabeceraTabla(self):
		fuente = QFont("MS Shell Dlg2", 9, QFont.Bold)
		self.tablaInventario.setFont(fuente)
		self.tablaInventario.setColumnCount(14)
		self.tablaInventario.setHorizontalHeaderLabels(['Semana', 'Aleatorio', 'Ventas', 'Aleatorio', 'Retraso de\n'+'Venta', 'Recibo \n'+'Bodega', 'Cantidad de \n'+'Pedido', 'Iniventario\n'+'Inicial', 'Inventario\n'+'Final', 'Costo por\n'+'Mantener', 'Faltante de \n'+'Venta', 'Costo por\n'+'Faltante', 'Cantidad de \n'+'Pedido', 'Despacho del\n'+'Pedido'])


	def Ingresar(self):
		semanas = self.txtSemanas.value()
		fila = 0
		if semanas > 0:
			self.btnCalcular.setEnabled(True)
			while semanas >= fila:
				self.tablaInventario.insertRow(fila)
				valorSemana = QTableWidgetItem(str(fila))
				valorAleatorio1 = QTableWidgetItem("0")
				valorVentas = QTableWidgetItem("0")
				valorAleatorio2 = QTableWidgetItem("0")
				valorRetraso = QTableWidgetItem("0")
				valorBodega = QTableWidgetItem("0")
				valorCantPedido = QTableWidgetItem("0")
				valorInvInicial = QTableWidgetItem("0")
				valorInvFinal = QTableWidgetItem("0")
				valorCostoMantener = QTableWidgetItem("0")
				valorFaltante = QTableWidgetItem("0")
				valorCostoFaltante = QTableWidgetItem("0")
				valorCant_Pedido = QTableWidgetItem("0")
				valorDespacho = QTableWidgetItem("0")
				self.tablaInventario.setItem(fila, 0, valorSemana)
				self.tablaInventario.setItem(0, 1, valorAleatorio1)
				self.tablaInventario.setItem(0, 2, valorVentas)
				self.tablaInventario.setItem(0, 3, valorAleatorio2)
				self.tablaInventario.setItem(0, 4, valorRetraso)
				self.tablaInventario.setItem(0, 5, valorBodega)
				self.tablaInventario.setItem(0, 6, valorCantPedido)
				self.tablaInventario.setItem(0, 7, valorInvInicial)
				self.tablaInventario.setItem(0, 8, valorInvFinal)
				self.tablaInventario.setItem(0, 9, valorCostoMantener)
				self.tablaInventario.setItem(0, 10, valorFaltante)
				self.tablaInventario.setItem(0, 11, valorCostoFaltante)
				self.tablaInventario.setItem(0, 12, valorCant_Pedido)
				self.tablaInventario.setItem(0, 13, valorDespacho)
				fila += 1
		else:
			QMessageBox.warning(self, "Advertencia", "Debe ingresar un número mayor a cero", QMessageBox.Ok)


	def CalcularDemandaSemanal(self):
		fila = 0
		while fila < 5:
			probabilidad = float(self.tablaDemanda.item(fila, 1).text())
			if fila == 0:
				inicio = QTableWidgetItem("0")
				fin = probabilidad
				valorFin = QTableWidgetItem(str(fin))
				self.tablaDemanda.setItem(fila, 2, inicio)
				self.tablaDemanda.setItem(fila, 3, valorFin)
			else:
				inicio = float(self.tablaDemanda.item(fila-1, 3).text())
				valorInicio = QTableWidgetItem(str(inicio))
				acumulada = round(probabilidad + inicio, 2)
				valorFin = QTableWidgetItem(str(acumulada))
				self.tablaDemanda.setItem(fila, 2, valorInicio)
				self.tablaDemanda.setItem(fila, 3, valorFin)
			fila += 1


	def CalcularRetrasoDespacho(self):
		fila = 0
		while fila < 4:
			probabilidad = float(self.tablaRetraso.item(fila, 1).text())
			if fila == 0:
				inicio = QTableWidgetItem("0")
				fin = probabilidad
				valorFin = QTableWidgetItem(str(fin))
				self.tablaRetraso.setItem(fila, 2, inicio)
				self.tablaRetraso.setItem(fila, 3, valorFin)
			else:
				inicio = float(self.tablaRetraso.item(fila-1, 3).text())
				valorInicio = QTableWidgetItem(str(inicio))
				acumulada = round(probabilidad + inicio, 2)
				valorFin = QTableWidgetItem(str(acumulada))
				self.tablaRetraso.setItem(fila, 2, valorInicio)
				self.tablaRetraso.setItem(fila, 3, valorFin)
			fila += 1


	def Buscar(self, tabla, filas, aleatorio):
		posicion = 0
		for i in range(filas):
			demanda = float(tabla.item(i, 0).text())
			inicio = float(tabla.item(i, 2).text())
			fin = float(tabla.item(i, 3).text())
			if aleatorio >= inicio and aleatorio <= fin:
				posicion = demanda
		return posicion


	def Calcular(self):
		semanas = self.txtSemanas.value()
		tamPedido = self.txtTamPedido.value()
		nivelPedido = self.txtNivelPedido.value()
		invInicial = self.txtInvInicial.value()
		costoFaltante = self.txtFaltante.value()
		costoMantener = self.txtCH.value()
		fila = 1
		banderaDespacho = 0
		banderaPedido = 0
		if semanas > 0:
			while fila <= semanas:
				aleatorio1 = float(self.tablaInventario.item(fila, 1).text())
				aleatorio2 = float(self.tablaInventario.item(fila, 3).text())
				ventas = self.Buscar(self.tablaDemanda, 5, aleatorio1)
				retraso = self.Buscar(self.tablaRetraso, 4, aleatorio2)
				valorVentas = QTableWidgetItem(str(ventas))
				valorRetraso = QTableWidgetItem(str(retraso))
				self.tablaInventario.setItem(fila, 2, valorVentas)
				self.tablaInventario.setItem(fila, 4, valorRetraso)
				if (banderaPedido == tamPedido) and (banderaDespacho == fila):
					#float(self.tablaInventario.item(fila, 0).text()))
					bodega = tamPedido
					banderaDespacho = 0
					banderaPedido = 0
				else:
					bodega = 0
				cantPedido = float(self.tablaInventario.item(fila-1, 6).text()) - bodega + float(self.tablaInventario.item(fila-1, 12).text())
				inv_Inicial = float(self.tablaInventario.item(fila-1, 8).text()) + bodega
				fin = inv_Inicial - float(self.tablaInventario.item(fila, 2).text())
				if fin < 0:
					inv_Final = 0
					faltante = -1 * fin
				else:
					inv_Final = fin
					faltante = 0
				costo_Mantener = inv_Final * costoMantener
				costo_Faltante = faltante * costoFaltante
				if (inv_Final + cantPedido) <= nivelPedido:
					cant_Pedido = tamPedido
					despacho = float(self.tablaInventario.item(fila, 4).text()) + float(self.tablaInventario.item(fila, 0).text())
					banderaDespacho = despacho
					banderaPedido = cant_Pedido
				else:
					cant_Pedido = 0
					despacho = 0
				valorBodega = QTableWidgetItem(str(bodega))
				valorCantPedido = QTableWidgetItem(str(cantPedido))
				valorInvInicial = QTableWidgetItem(str(inv_Inicial))
				valorInvFinal = QTableWidgetItem(str(inv_Final))
				valorCostoMantener = QTableWidgetItem(str(costo_Mantener))
				valorFaltante = QTableWidgetItem(str(faltante))
				valorCostoFaltante = QTableWidgetItem(str(costo_Faltante))
				valorCant_Pedido = QTableWidgetItem(str(cant_Pedido))
				valorDespacho = QTableWidgetItem(str(despacho))
				self.tablaInventario.setItem(fila, 5, valorBodega)
				self.tablaInventario.setItem(fila, 6, valorCantPedido)
				self.tablaInventario.setItem(fila, 7, valorInvInicial)
				self.tablaInventario.setItem(fila, 8, valorInvFinal)
				self.tablaInventario.setItem(fila, 9, valorCostoMantener)
				self.tablaInventario.setItem(fila, 10, valorFaltante)
				self.tablaInventario.setItem(fila, 11, valorCostoFaltante)
				self.tablaInventario.setItem(fila, 12, valorCant_Pedido)
				self.tablaInventario.setItem(fila, 13, valorDespacho)
				fila += 1

	def LimpiarCampos(self):
		self.tablaDemanda.clearContents()
		self.tablaRetraso.clearContents()
		self.txtSemanas.setValue(0)
		self.txtTamPedido.setValue(0)
		self.txtNivelPedido.setValue(0)
		self.txtInvInicial.setValue(0)
		self.txtFaltante.setValue(0.00)
		self.txtCH.setValue(0.00)
		fila = self.tablaInventario.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.tablaInventario.removeRow(i)