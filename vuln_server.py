import socket
import subprocess
import threading

BIND_ADDR = '0.0.0.0'
BIND_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BIND_ADDR, BIND_PORT))
server.listen(5)

print(f'Listening on {BIND_ADDR}:{BIND_PORT}')

# Handle client connection
def handle_client(client_socket):

  # Receive data
  request = client_socket.recv(1024)
  
  # COMMAND INJECTION 
  if request.startswith(b'COMMAND'):
    cmd = request[len(b'COMMAND'):].strip() 
    output = subprocess.getoutput(cmd) 
    client_socket.send(output.encode())

  # FORMAT STRING    
  elif request.startswith(b'PRINT'):
    msg = request[len(b'PRINT'):].strip()
    client_socket.send(msg % b'A'*100)

  # BUFFER OVERFLOW
  elif request.startswith(b'OVERFLOW'):
    func1(request[len(b'OVERFLOW'):])   

  # Plaintext communication
  else:
    client_socket.send(b'Welcome!')

  client_socket.close()

# Vulnerable function
def func1(input):
  buffer = "A" * 100
  buffer += input

while True:
  client,addr = server.accept()
  thread = threading.Thread(target=handle_client, args=(client,))
  thread.start()
