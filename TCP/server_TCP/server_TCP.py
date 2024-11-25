import socket
import socket

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Servidor esperando por conexões...")
    conn, addr = server_socket.accept()
    print(f"Conexão de {addr}")

    try:
        # Receber nome do arquivo
        file_name = conn.recv(1024).decode()
        print(f"Recebendo arquivo: {file_name}")
        conn.sendall(b'ACK_NAME')  # Confirmação de recebimento do nome do arquivo

        # Receber tamanho do arquivo
        file_size = int(conn.recv(1024).decode())
        print(f"Tamanho do arquivo: {file_size} bytes")
        conn.sendall(b'ACK_SIZE')  # Confirmação de recebimento do tamanho do arquivo

        # Receber o arquivo
        print("Iniciando recebimento do arquivo...")
        received_size = 0
        with open(file_name, 'wb') as file:
            while received_size < file_size:
                data = conn.recv(1024)
                if not data:
                    print("Conexão encerrada inesperadamente.")
                    break
                file.write(data)
                received_size += len(data)
                print(f"Progresso: {received_size}/{file_size} bytes recebidos")

        if received_size == file_size:
            print(f"Arquivo {file_name} recebido com sucesso.")
        else:
            print("Erro: Arquivo incompleto.")

    finally:
        conn.close()

if _name_ == '_main_':
    start_tcp_server()
