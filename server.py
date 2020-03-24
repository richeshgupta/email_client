import socket
import sqlite3


s = socket.socket()
port = 12345
s.bind(('',port))
s.listen(10)
while True:
    c,addr = s.accept()
    print('Connection req. from : ',addr)
    c.close()
