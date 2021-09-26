import socket
from threading import Thread
from terminal import name_terminal_cliente

global tcp_conexao

def receber():
    global tcp_conexao
    while True:
        msg = tcp_conexao.recv(1024)
        print ("Server:",msg)

def enviar():
    global tcp_conexao
    print ('Para sair use CTRL+X\n')
    msg = input()
    while msg != '\x18':
        tcp_conexao.send(msg.encode())
        msg = input()
    tcp_conexao.close()

SERVER = '127.0.0.1'
PORT = 5002

name_terminal_cliente()

tcp_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_conexao.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()