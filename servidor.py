import socket
from threading import Thread
from terminal import name_terminal_servidor

global tcp_conexao

def enviar():
    global tcp_conexao
    mensagem = input()
    while True:
        tcp_conexao.send(mensagem.encode())
        mensagem = input()

HOST = ''
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    name_terminal_servidor()
    tcp_conexao, cliente = tcp.accept()
    print ('Concetado por', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        mensagem = tcp_conexao.recv(1024)
        if not mensagem: break
        print("Cliente:",mensagem)
    print ('Finalizando conexao do cliente', cliente)
    tcp_conexao.close()