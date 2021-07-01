import pandas as pd


class LectorCsv():
	"""
	Esta clase se encarga de tratar los datos optenidos
	de un archivo csv
	"""
	def __init__(self, archivo):
		self.__datos = pd.read_csv(archivo, delimiter=";", header=0)

	def cantidadPersonas(self):
		#Retorna cantidad total de personas registradas
		return len(self.__datos)

	def promedioEdad(self, equipo="Racing" ):
		# Retorna el promedio de edad de los socios de un equipo por defecto Racing
		sociosEquipo = self.__datos.query('equipo == "'+equipo+'"')
		promedio = sociosEquipo["edad"].mean()
		return promedio

	def sociosCasadosUniversitarios(self, tamanio=100):
		"""
		Retorna Un listado con cantidad de personas solicitadas por  el parametro
		tamanio donde cumplen la condicion de personas casadas, con estudios
		Universitarios, ordenadas de menor a mayor según su edad. Por
		cada persona, muestra: nombre, edad y equipo.
		"""
		casadosUniversitarios = self.__datos.query(
			'estadoCivil == "Casado" and nivelEstudio == "Universitario" ')
		sociosOrdenados = casadosUniversitarios.sort_values(by=["edad"], ascending=[True])
		respuesta = sociosOrdenados[["nombre","edad","equipo"]]
		return (respuesta[0:tamanio])

	def nombresComunes(self, equipo="River", tamanio=5):
		"""Retorna la cantidad de nombres mas comunes de un equipo
		segun el tamannio pasado por parametro, ordenados de el mas comun
		al menos comun
		"""
		listaNombres = self.__datos.query('equipo == "'+equipo+'"')
		nombres = listaNombres["nombre"].value_counts()
		return (nombres[0:tamanio])

	def datosEquipos(self):
		"""
		Retorna un listado, ordenado de mayor a menor según la cantidad de
		socios, que enumere, junto con cada equipo, el promedio de edad
		de sus socios, la menor edad registrada y la mayor edad registrada
		"""
		datosEquipoEdades = self.__datos[["equipo","edad"]]
		equipoSocios = datosEquipoEdades["equipo"].value_counts()
		datosEquipo = equipoSocios.to_frame(name='numSocios')
		datosEquipo[["edadPromedio","edadMinima","edadMaxima"]]=0
		
		for x in (datosEquipo.index):
			aux = datosEquipoEdades.query('equipo == "'+x+'"')
			datosEquipo.loc[x,"edadPromedio"] = aux["edad"].mean()
			datosEquipo.loc[x,"edadMinima"] = aux["edad"].min()
			datosEquipo.loc[x,"edadMaxima"] = aux["edad"].max()
		
		return(datosEquipo)