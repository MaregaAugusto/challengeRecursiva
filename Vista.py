import os

class Vista():
	"""
	Clase que interactúa con el usuario
	muestra y solicita información
	"""
	def __init__(self):
		# guardamos en una tupla los títulos para reutilizarlos 
		self.__opciones = ('Total de personas registradas',
			'Edad promedio socios Racing',
			'Listado de personas casadas y estudio universitario',
			'5 nombre mas comunes entre los hinchas de River',
			'Listado: Equipo-Cantidad de socios- Edad promedio - Edad mínima - Edad máxima',
			'exit')

	def main(self):
		"""
		Función menú principal muestra las opciones de consola
		y solicita la ejecución de una de ellas 
		retorna cualquier valor ingresado por consola
		"""
		os.system('cls')
		print('Challenge Recursiva')

		for i in range(6):
			print(f'{i+1}) {self.__opciones[i]}')
		return input("Ingrese el número de de la opción: ")
	
	def resultados(self, resultado, titulo):
		"""
		Función que muestra los resultados con el título 
		de lo solicitado
		"""
		os.system('cls')
		print(self.__opciones[titulo])
		print("----------Resultado-----------------")
		print(resultado)
		input()

	def closse(self):
		# Limpia la consola una vez terminada la ejecución
		os.system('cls')
