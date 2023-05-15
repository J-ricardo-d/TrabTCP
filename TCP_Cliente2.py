import socket

# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço do servidor
server_address = ('localhost', 10000)

# Conecta ao servidor
sock.connect(server_address)
print('Conectado ao servidor!')

# Loop do jogo
while True:
    # Recebe a mensagem do servidor
    data = sock.recv(1024)
    print(data.decode())

    # Pede ao usuário para escolher sua jogada
    jogada = input('Sua jogada (0 - Papel, 1 - Pedra, 2 - Tesoura): ')
    sock.sendall(jogada.encode())

    # Recebe o resultado do jogo do servidor
    data = sock.recv(1024)
    print(data.decode())
