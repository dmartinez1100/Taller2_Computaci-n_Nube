from socket import *
import ast
import shlex
import re

servidorNombre = "192.168.1.5"
servidorPuerto = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))

while True:
	#Ingresa solicitud HTTP
	mensaje = input("Ingrese un mensaje:\n")

	#String must recognize scape characters
	#Detects Scape characters
	scape_char = re.search("\\\.",mensaje)

	#Si hay un Scape caracter, lo acepta
	if scape_char:
		mensaje = ast.literal_eval(shlex.quote(mensaje))

	#se recibe el mensaje y se cierra la conexion
	clienteSocket.send(bytes(mensaje, "utf-8"))
	mensajeRespuesta = clienteSocket.recv(1024)
	clienteSocket.close()

	print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))

	#se contacta el servidor de nuevo
	clienteSocket = socket(AF_INET, SOCK_STREAM)
	clienteSocket.connect((servidorNombre,servidorPuerto))

	#si no se envia nada mas, se cierra la conexion
	mensaje = input(u"¿Enviar otro mensaje[Y\\N]?:\n")
	if (mensaje != "Y"):
		clienteSocket.close()
		break



#Solicitudes - Algunas Mal hechas

#GET Web\Index.html HTTP/1.1\r\nHost: 192.168.1.5:12000\r\n\r\n

#GET Archivo.html HTTP/1.1\r\nHost: 192.168.1.5:12000\r\n\r\n
#obtener Archivo.html HTTP/1.1\r\nHost: 192.168.1.5:12000\r\n\r\n
#get Archivo.html HTTP/1.1\r\nHost: 194.158.1.12:12000\r\n\r\n
