import socket
import os

def send_file_to_client(filename):
    HOST = "127.0.0.1"  # Endereço padrão de loopback (localhost)
    PORT = 65433        # Porta para escutar (portas não privilegiadas são > 1023)
    
    # Obtém o tamanho do arquivo e calcula o número de pacotes
    file_size = os.path.getsize(filename)  
    num_packets = (file_size // 1024) + 1  

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
            
            sent_packets = 0  # Contador de pacotes enviados
            
            # Lê o arquivo em pedaços de 1024 bytes
            with open(filename, 'rb') as file:
                while chunk := file.read(1024):  
                    
                    # Envia cada pedaço do arquivo para o cliente
                    conn.sendall(chunk)
                    sent_packets += 1
                
            print(f"Arquivo {filename} enviado com sucesso.")
           
        # Fecha a conexão com o cliente    
        conn.close()  
        
        # Fecha o socket do servidor
        s.close()     
        print("Encerrando servidor...")
        
        # Chama a função para imprimir o resumo
        imprimir_resumo(file_size, sent_packets)

def imprimir_resumo(tamanho_total, pacotes_enviados):
    print(f"\nTamanho total transferido: {tamanho_total} bytes")
    print(f"Total de pacotes enviados: {pacotes_enviados}")

if __name__ == '__main__':
    
    # Caminho do arquivo a ser enviado
    filename = 'TCP/arquivos_origem/FLS.rar'  
    
    send_file_to_client(filename)
