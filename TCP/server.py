import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Servidor esperando por conexões...")
    conn, addr = server_socket.accept()
    print(f"Conexão de {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Recebido: {data.decode()}")
        conn.sendall(data)

    conn.close()

if __name__ == '__main__':
    start_server()
