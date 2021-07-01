#import pandas as pd

from LectorCsv import *
from Vista import *


class Controlador():
	

	def __init__(self):
		archivo = "socios.csv"
		self.__vista = Vista()
		self.__lectorCsv = LectorCsv(archivo)
		self.Home()

	def Home(self):

		opcion = self.__vista.main()

		if opcion == 1:
			self.punto1()
		elif opcion == 2:
			self.punto2()
		elif opcion == 3:
			self.punto3()
		elif opcion == 4:
			self.punto4()
		elif opcion == 5:
			self.punto5()
		elif opcion == 6:
			self.exit()

	def punto1(self):
		repuesta = self.__lectorCsv.cantidadPersonas()
		self.__vista.resultados(repuesta)
		self.Home()

	def punto2(self):
		repuesta = self.__lectorCsv.promedioEdad()
		self.__vista.resultados(repuesta)
		self.Home()

	def punto3(self):
		repuesta = self.__lectorCsv.sociosCasadosUniversitarios()
		self.__vista.resultados(repuesta)
		self.Home()

	def punto4(self):
		repuesta = self.__lectorCsv.nombresComunes()
		self.__vista.resultados(repuesta)
		self.Home()

	def punto5(self):
		repuesta = self.__lectorCsv.datosEquipos()
		self.__vista.resultados(repuesta)
		self.Home()

	def exit(self):
		self.__vista.closse()

#----Ejecicion-----#
Controlador()