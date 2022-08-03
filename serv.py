import socket
import os
 
sock = socket.socket()
sock.bind(('0.0.0.0', 2222))
sock.listen(10)
pid=os.fork()
while True:
  conn, addr = sock.accept()
  print 'connected:', addr
  data = conn.recv(1024)
  if not data:
    break
  conn.send(data)
  conn.close()
  print 'disconnected:', addr
