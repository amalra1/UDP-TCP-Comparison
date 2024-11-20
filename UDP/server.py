import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("Servidor UDP esperando por mensagens...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Recebido de {addr}: {data.decode()}")
        server_socket.sendto(data, addr)  # Echo de volta ao cliente

if __name__ == '__main__':
    start_udp_server()
