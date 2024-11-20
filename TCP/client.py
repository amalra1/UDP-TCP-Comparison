import socket

def start_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        while True:
            message = input("Digite a mensagem para enviar: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Recebido do servidor: {data.decode()}")
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_tcp_client()
