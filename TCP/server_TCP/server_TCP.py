import socket

def send_file_to_client(filename):
    HOST = "127.0.0.1"  
    PORT = 65433       

    # Cria socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # Associa o socket ao HOST e PORT especificados
        s.bind((HOST, PORT))
        
        # Habilita o servidor para aceitar conexões
        s.listen()  
        
        # Espera e aceita conexão
        print("Servidor esperando por conexões...")
        conn, addr = s.accept()
        
        with conn:  
            print(f"Conectado por {addr}")
            with open(filename, 'rb') as file:
                
                # Lê o arquivo em pedaços de 1024 bytes
                while chunk := file.read(1024):  
                    
                    # Envia cada pedaço do arquivo para o cliente
                    conn.sendall(chunk)  
                    
            print(f"Arquivo {filename} enviado com sucesso.")
           
        # Fecha a conexão com o cliente    
        conn.close()  
        
        # Fecha o socket do servidor
        s.close()     
        print("Encerrando servidor...")

if __name__ == '__main__':
    
    # Caminho do arquivo a ser enviado
    filename = 'TCP/arquivos_origem/video_arvore.mp4'  
    
    send_file_to_client(filename)  
