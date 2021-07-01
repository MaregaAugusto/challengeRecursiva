import os
#import pandas as pd

class Vista():
	
	def main(self):
		os.system('cls')
		print('Challenge Recursiva')
		print('1) Total de personas registradas')
		print('2) Edad promedio socios Racing')
		print('3) Listado de personas casadas y estudio universitario')
		print('4) 5 nombre mas comunes entre los hinchas de River')
		print('5) Listado: Equipo-Numero de socios- Edad promedio - Edad minima - Edad Maxima')
		print('6) Exit')
		return int(input("Ingrese el número de de la opción: "))
	
	def resultados(self, resultado):
		os.system('cls')
		print("----------Resultado-----------------")
		print(resultado)
		input()

	def closse(self):
		os.system('cls')
