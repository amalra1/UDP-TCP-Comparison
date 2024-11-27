import socket
import os
import time

def receive_file_from_server(filename):
    HOST = "127.0.0.1"
    PORT = 65433
    BUFFER_SIZE = 1024  # Tamanho do buffer

    # Cria socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        
        # Envia uma mensagem inicial para o servidor para iniciar a transferência
        s.sendto(b'START', (HOST, PORT))
        
        # Inicia a contagem do tempo
        start_time = time.time()
        
        with open(filename, 'wb') as file:
            print("Iniciando recebimento do arquivo...")
            received_packets = 0  # Contador de pacotes recebidos
            while True:
                
                # Recebe dados do servidor em pedaços de 1024 bytes
                data, addr = s.recvfrom(BUFFER_SIZE)  
                
                # Sai do loop se receber a mensagem de fim
                if data == b'END':
                    break  
                
                # Escreve os dados recebidos no arquivo
                file.write(data)
                received_packets += 1
                
            print(f"Arquivo {filename} recebido com sucesso.")
        
        # Calcula o tempo total de transferência
        end_time = time.time()
        total_time = end_time - start_time

    # Chama a função para comparar os arquivos
    comparar_arquivos('UDP/arquivos_origem/FLS.rar', filename)
    print(f"Tempo total de transferência: {total_time:.5f} segundos")
    print(f"Total de pacotes recebidos: {received_packets}")

def comparar_arquivos(origem, destino):
    with open('UDP/arquivos_origem/FLS.rar', 'rb') as file1, open('UDP/arquivos_destino/download.rar', 'rb') as file2:
        if file1.read() == file2.read():
            print("Todos os pacotes enviados foram recebidos corretamente.")
        else:
            print("Diferença detectada entre os arquivos de origem e destino.")

if __name__ == '__main__':
    
    # Caminho onde o arquivo será salvo
    filename = 'UDP/arquivos_destino/download.rar'
    receive_file_from_server(filename)
