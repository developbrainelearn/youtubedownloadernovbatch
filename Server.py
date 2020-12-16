# Socket  --> It is an entry point or exit point
import socket   #DevelopBrain

server = socket.socket()  # door
server.bind(('localhost',8888)) #127.0.0.1  # 65536 0 to 1024 # Ports

server.listen(10)  # no of users     1 kb = 1000bytes  1Kib = 1024 Bytes
print('Waiting for client...')  #   1 kilo bytes = 1000

while True:
    client,address = server.accept()
    client.send(bytes('Welcome to developBrain server.. What is your name','utf-8'))  #encoding...
    name = client.recv(1024)
    print('Connection is established with',name.decode('utf-8'),address)
    while True:
        write = input('>>')
        client.send(bytes(write,'utf-8'))
        readmsg = client.recv(1024)
        print(readmsg.decode('utf-8'))

        if write == 'Thank you':
            client.close()
            exit(0)