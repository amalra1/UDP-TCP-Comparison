import socket
import os

def send_file_to_client(filename):
    HOST = "127.0.0.1"  # Endereço padrão de loopback (localhost)
    PORT = 65433        # Porta para escutar (portas não privilegiadas são > 1023)
    
    # Obtém o tamanho do arquivo e calcula o número de pacotes
    file_size = os.path.getsize(filename)  
    num_packets = (file_size // 1024) + 1  

    # Cria socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        
        # Espera por uma mensagem inicial do cliente para saber o endereço e porta
        print("Servidor esperando por conexões...")
        data, addr = s.recvfrom(1024)
        print(f"Conectado por {addr}")
        
        # Contador de pacotes enviados
        sent_packets = 0  
        
        # Lê o arquivo em pedaços de 1024 bytes
        with open(filename, 'rb') as file:
            while chunk := file.read(1024):  
                
                # Envia cada pedaço do arquivo para o cliente
                s.sendto(chunk, addr)
                sent_packets += 1
                
        # Envia uma mensagem final para indicar o fim da transferência
        s.sendto(b'END', addr)
        
        print(f"Arquivo {filename} enviado com sucesso.")
        imprimir_resumo(file_size, sent_packets)

def imprimir_resumo(tamanho_total, pacotes_enviados):
    print(f"\nTamanho total transferido: {tamanho_total} bytes")
    print(f"Total de pacotes enviados: {pacotes_enviados}")

if __name__ == '__main__':
    
    # Caminho do arquivo a ser enviado
    filename = 'UDP/arquivos_origem/FLS.rar'  
    
    send_file_to_client(filename)
