from socket import *

servidorNombre = "127.0.0.1" 
servidorPuerto = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)


service=input('Escriba el servicio a solicitar:\n(saldo,debitar o acreditar)\n\n')
clienteSocket.connect((servidorNombre,servidorPuerto))
clienteSocket.send(bytes(service, "utf-8"))
     

     
if service.lower()=='debitar':
    X=input('Ingresa la cantidad a reducir:\n')
    clienteSocket.send(bytes(X, "utf-8"))
elif service.lower()=='acreditar':
    Y=input('Ingresa la cantidad a incrementar:\n')
    clienteSocket.send(bytes(Y, "utf-8"))

    
    
response = str(clienteSocket.recv(1024),'utf-8')
print(response)
    
clienteSocket.close()



