import socket

target_host = "www.google.com"
target_port = 80

# Crear un objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar con el servidor
client.connect((target_host, target_port))

# Enviar alguna data
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode('utf-8'))

# Recibir algunos datos
response = client.recv(4096)

print(response.decode('utf-8'))
