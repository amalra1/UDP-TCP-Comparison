import socket

def receive_file_from_server(filename):
    HOST = "127.0.0.1"  
    PORT = 65433        

    # Cria socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # Conecta no servidor
        s.connect((HOST, PORT))  
        with open(filename, 'wb') as file:
            print("Iniciando recebimento do arquivo...")
            while True:
                
                # Recebe dados do servidor em pedaços de 1024 bytes
                data = s.recv(1024)  
                
                if not data:
                    # Sai do loop se não houver mais dados
                    break  
                
                # Escreve os dados recebidos no arquivo
                file.write(data)  
                
            print(f"Arquivo {filename} recebido com sucesso.")

if __name__ == '__main__':
    
    # Caminho onde o arquivo será salvo
    filename = 'TCP/arquivos_destino/video_arvore.mp4'
    receive_file_from_server(filename)
