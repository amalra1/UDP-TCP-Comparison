import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("Servidor UDP esperando por mensagens...")

    try:
        # Receber nome do arquivo
        file_name_data, client_address = server_socket.recvfrom(1024)
        file_name = file_name_data.decode('utf-8')
        print(f"Recebendo arquivo: {file_name}")
        server_socket.sendto(b'ACK_NAME', client_address)

        # Receber tamanho do arquivo
        file_size_data, client_address = server_socket.recvfrom(1024)
        file_size = int(file_size_data.decode('utf-8'))
        print(f"Tamanho do arquivo: {file_size} bytes")
        server_socket.sendto(b'ACK_SIZE', client_address)

        # Receber o arquivo
        print("Iniciando recebimento do arquivo...")
        received_size = 0
        with open(file_name, 'wb') as file:
            while received_size < file_size:
                data, client_address = server_socket.recvfrom(1024)
                file.write(data)
                received_size += len(data)
                print(f"Progresso: {received_size}/{file_size} bytes recebidos")

        if received_size == file_size:
            print(f"Arquivo {file_name} recebido com sucesso.")
        else:
            print("Erro: Arquivo incompleto.")

    except Exception as e:
        print(f"Erro no servidor: {e}")
    finally:
        server_socket.close()

if _name_ == '_main_':
    start_udp_server()
