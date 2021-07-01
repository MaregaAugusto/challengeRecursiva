from LectorCsv import *
from Vista import *


class Controlador():
	"""
	Clase que se encarga de procesar los datos recibidos por la vista y solicitar
	los datos a la clase LectorCsv para mostrar
	"""

	def __init__(self):
		"""
		esta clase inicia las clases con las que interactúa
		también se define el nombre del archivo a leer
		y por último llama al método Home
		"""
		archivo = "socios.csv"
		self.__vista = Vista()
		self.__lectorCsv = LectorCsv(archivo)
		self.Home()

	def Home(self):
		"""
		Este método ejecuta la vista y procesa la entrada de datos 
		"""
		opcion = self.__vista.main()

		if opcion == '1':
			self.punto1()
		elif opcion == '2':
			self.punto2()
		elif opcion == '3':
			self.punto3()
		elif opcion == '4':
			self.punto4()
		elif opcion == '5':
			self.punto5()
		elif opcion == '6':
			self.exit()
		else:
			self.Home()

	"""
	Todos los métodos siguientes llaman a una función de LectorCsv
	nos devuelve la respuesta que es pasada a la vista para que la muestre
	"""

	def punto1(self):
		repuesta = self.__lectorCsv.cantidadPersonas()
		self.__vista.resultados(repuesta, 0)
		self.Home()

	def punto2(self):
		repuesta = self.__lectorCsv.promedioEdad()
		self.__vista.resultados(repuesta, 1)
		self.Home()

	def punto3(self):
		repuesta = self.__lectorCsv.sociosCasadosUniversitarios()
		self.__vista.resultados(repuesta, 2)
		self.Home()

	def punto4(self):
		repuesta = self.__lectorCsv.nombresComunes()
		self.__vista.resultados(repuesta, 3)
		self.Home()

	def punto5(self):
		repuesta = self.__lectorCsv.datosEquipos()
		self.__vista.resultados(repuesta, 4)
		self.Home()

	# llama a un método que limpia la consola 
	def exit(self):
		self.__vista.closse()

#----Ejecición-----#
Controlador()