import socket
import os
import time

def receive_file_from_server(filename):
    HOST = "127.0.0.1"  
    PORT = 65433        

    # Cria socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # Conecta no servidor
        s.connect((HOST, PORT))
        
        # Inicia a contagem do tempo
        start_time = time.time()
        
        with open(filename, 'wb') as file:
            print("Iniciando recebimento do arquivo...")
            received_packets = 0  # Contador de pacotes recebidos
            while True:
                
                # Recebe dados do servidor em pedaços de 1024 bytes
                data = s.recv(1024)  
                
                if not data:
                    # Sai do loop se não houver mais dados
                    break  
                
                # Escreve os dados recebidos no arquivo
                file.write(data)
                received_packets += 1
                
            print(f"Arquivo {filename} recebido com sucesso.")
        
        # Calcula o tempo total de transferência
        end_time = time.time()
        total_time = end_time - start_time

    # Chama a função para comparar os arquivos
    comparar_arquivos('TCP/arquivos_origem/FLS.rar', filename)
    print(f"Tempo total de transferência: {total_time:.5f} segundos")
    print(f"Total de pacotes recebidos: {received_packets}")

def comparar_arquivos(origem, destino):
    with open('TCP/arquivos_origem/FLS.rar', 'rb') as file1, open('TCP/arquivos_destino/download.rar', 'rb') as file2:
        if file1.read() == file2.read():
            print("Todos os pacotes enviados foram recebidos corretamente.")
        else:
            print("Diferença detectada entre os arquivos de origem e destino.")

if __name__ == '__main__':
    
    # Caminho onde o arquivo será salvo
    filename = 'TCP/arquivos_destino/download.rar'
    receive_file_from_server(filename)
