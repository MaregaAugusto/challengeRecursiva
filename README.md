# Challenge 
Se solicitaba leer un archivo .csv y mostrar información por consola, para mas detalle leer el archivo Challenge - Superliga.pdf adjunto

## Ejecución del programa
Entrar en la carpeta **dist**, comprobar que el archivo **socios.csv** se encuentre a la misma altura que el ejecutable **Challenge.exe** se abrirá la consola y mostrara la siguiente información  

>Challenge Recursiva 
>1) Total de personas registradas 
>2) Edad promedio socios Racing 
>3) Listado de personas casadas y estudio universitario
>4) 5 nombre mas comunes entre los hinchas de River 
>5) Listado: Equipo-Numero de socios- Edad promedio - Edad mínima - Edad Máxima 
>6) Exit 
>Ingrese el número de de la opción:

Una vez ingresa el valor presione enter y se mostrara los resultados

## Correr el programa desde el código
Primero deberá clonar el código en su maquina, luego situarse con la consola a la altura del archivo **Controlador.py** y crear un entorno virtual (asegúrese de tener instalado python)
Ejecute el siguiente comando 

    pip install virtualenv
Esperamos que se instale

    python -m virtualenv *nombreDelEntorno*
Luego nos dirigimos a la carpeta **nombreDelEntorno/Scripts**

    cd nombreDelEntorno/Scripts
y ejecutamos el comando
	

    activate
Ahora necesitamos instala la librería ***pandas***

    pip install pandas

una ves instalada la librería, volvemos a la carpeta donde se encuentra el archivo **Controlador.py** y ejecutamos el archivo con el siguiente comando

    python Controlador.py
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0MjU0NTcyMywtMjE0NTI2MjA1MV19
-->