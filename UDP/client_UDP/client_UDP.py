import socket
import os

def start_udp_client(file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    # Expande o caminho caso contenha ~
    file_path = os.path.expanduser(file_path)

    try:
        # Obter nome e tamanho do arquivo
        file_name = os.path.basename(file_path)  # Nome do arquivo
        file_size = os.path.getsize(file_path)   # Tamanho do arquivo em bytes

        # Enviar nome do arquivo
        print(f"Enviando nome do arquivo: {file_name}")
        client_socket.sendto(file_name.encode('utf-8'), server_address)
        ack, _ = client_socket.recvfrom(1024)
        print(f"ACK recebido: {ack.decode('utf-8')}")
        if ack.decode('utf-8') != 'ACK_NAME':
            print("Erro: ACK_NAME não recebido.")
            return

        # Enviar tamanho do arquivo
        print(f"Enviando tamanho do arquivo: {file_size}")
        client_socket.sendto(str(file_size).encode('utf-8'), server_address)
        ack, _ = client_socket.recvfrom(1024)
        print(f"ACK recebido: {ack.decode('utf-8')}")
        if ack.decode('utf-8') != 'ACK_SIZE':
            print("Erro: ACK_SIZE não recebido.")
            return

        # Enviar o conteúdo do arquivo
        print("Enviando conteúdo do arquivo...")
        with open(file_path, 'rb') as file:
            sent_size = 0
            while chunk := file.read(1024):  # Envia o arquivo em pedaços
                client_socket.sendto(chunk, server_address)
                sent_size += len(chunk)
                print(f"Progresso: {sent_size}/{file_size} bytes enviados")

        print(f"Arquivo {file_name} enviado com sucesso.")

    except Exception as e:
        print(f"Erro no cliente: {e}")
    finally:
        client_socket.close()

if _name_ == '_main_':
    file_path = input("Digite o caminho do arquivo para enviar: ")
    start_udp_client(file_path)
