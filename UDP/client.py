import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    try:
        while True:
            message = input("Digite a mensagem para enviar: ")
            client_socket.sendto(message.encode(), server_address)
            data, _ = client_socket.recvfrom(1024)
            print(f"Recebido do servidor: {data.decode()}")
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_udp_client()
