import socket

# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço do servidor
server_address = ('localhost', 10000)

# Associa o socket com o endereço do servidor
sock.bind(server_address)

# O servidor espera por conexões
sock.listen(2)
print('Aguardando conexões...')

# Lista para armazenar os jogadores conectados
jogadores = []

while len(jogadores) < 2:
    # Espera por uma conexão
    connection, client_address = sock.accept()
    print('Conexão estabelecida com', client_address)
    
    # Adiciona o jogador à lista de jogadores
    jogadores.append(connection)

# Envia a mensagem de início do jogo para os jogadores
for jogador in jogadores:
    jogador.sendall(b'Jogo iniciado! Escolha sua jogada (0 - Papel, 1 - Pedra, 2 - Tesoura):')

# Loop do jogo
while True:
    # Recebe a jogada do jogador 1
    data = jogadores[0].recv(1024)
    jogada1 = int(data.decode())
    print('Jogador 1 jogou', jogada1)

    # Recebe a jogada do jogador 2
    data = jogadores[1].recv(1024)
    jogada2 = int(data.decode())
    print('Jogador 2 jogou', jogada2)

    # Calcula o resultado do jogo
    resultado = (jogada1 - jogada2) % 3

    if resultado == 0:
        mensagem = 'Empate!'
    elif resultado == 1:
        mensagem = 'Jogador 1 venceu!'
    else:
        mensagem = 'Jogador 2 venceu!'

    # Envia o resultado para os jogadores
    jogadores[0].sendall(mensagem.encode())
    jogadores[1].sendall(mensagem.encode())

    # Envia a mensagem de continuação do jogo para os jogadores
    for jogador in jogadores:
        jogador.sendall(b'Escolha sua jogada (0 - Papel, 1 - Pedra, 2 - Tesoura):')
