import heapq
from collections import Counter
import json

class BitWriter:
    def __init__(self, filename):
        self.file = open(filename, 'wb')
        self.bit_atual = 0
        self.bits_preenchidos = 0

    def escrever_bit(self, bit):
        # Pegando cada Byte (Os bytes ainda não foram convertidos, estão em formato de decimal)
        self.bit_atual = (self.bit_atual << 1) | bit
        self.bits_preenchidos += 1

        if self.bits_preenchidos == 8:
            # Depois de terminar de pegar o byte em forma de decimal, converte-lo para byte e escreve-lo no arquivo
            self.file.write(bytes([self.bit_atual]))
            self.bit_atual = 0
            self.bits_preenchidos = 0

    def fechar(self):
        if self.bits_preenchidos > 0:
            self.bit_atual = self.bit_atual << (8 - self.bits_preenchidos)
            print(8 - self.bits_preenchidos)
            self.file.write(bytes([self.bit_atual]))
        self.file.close()


class NoHuffman:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

# Função para construir a árvore de Huffman
def construir_arvore_huffman(texto):
    frequencias = Counter(texto)
    heap = [NoHuffman(caractere, freq) for caractere, freq in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)
        no_fusao = NoHuffman(None, no1.frequencia + no2.frequencia)
        no_fusao.esquerda = no1
        no_fusao.direita = no2
        heapq.heappush(heap, no_fusao)

    return heap[0]

# Função para gerar os códigos de Huffman a partir da árvore
def gerar_codigos_huffman(raiz):
    codigos = {}
    def _gerar_codigos(no, codigo_atual):
        if no is None:
            return
        if no.caractere is not None:
            codigos[no.caractere] = codigo_atual
        _gerar_codigos(no.esquerda, codigo_atual + "0")
        _gerar_codigos(no.direita, codigo_atual + "1")

    _gerar_codigos(raiz, "")
    return codigos

# Função para serializar a árvore de Huffman em um formato que pode ser salvo
def serializar_arvore(no):
    if no is None:
        return None
    return {
        'caractere': no.caractere,
        'frequencia': no.frequencia,
        'esquerda': serializar_arvore(no.esquerda),
        'direita': serializar_arvore(no.direita)
    }

# Função para desserializar a árvore de Huffman de volta ao formato de árvore
def desserializar_arvore(dados):
    if dados is None:
        return None
    no = NoHuffman(dados['caractere'], dados['frequencia'])
    no.esquerda = desserializar_arvore(dados['esquerda'])
    no.direita = desserializar_arvore(dados['direita'])
    return no

# Função para compactar um arquivo de texto usando Huffman
def compactar_arquivo():
    nome_arquivo_entrada = "entrada.txt"
    nome_arquivo_codificado = "saida.huf"
    nome_arquivo_arvore = "arvore.json"

    with open(nome_arquivo_entrada, 'r') as f:
        texto = f.read()

    raiz = construir_arvore_huffman(texto)
    codigos = gerar_codigos_huffman(raiz)
    texto_codificado = ''.join(codigos[caractere] for caractere in texto)

    # Salvar a árvore de Huffman em arvore.json
    with open(nome_arquivo_arvore, 'w') as f:
        json.dump(serializar_arvore(raiz), f)

    # Salvar apenas o texto codificado em saida.huf
    with open(nome_arquivo_codificado, 'w') as f:
        f.write(texto_codificado)

    print(f"Arquivo '{nome_arquivo_entrada}' foi compactado para '{nome_arquivo_codificado}'.")

# Função para descompactar um arquivo comprimido usando Huffman


# Função para descompactar um arquivo comprimido usando Huffman
def descompactar_arquivo(nome_arquivo_codificado, nome_arquivo_arvore, nome_arquivo_saida):
    with open(nome_arquivo_arvore, 'r') as f:
        arvore_serializada = json.load(f)

    with open(nome_arquivo_codificado, 'rb') as f:
        bit_string = f.read()

    raiz = desserializar_arvore(arvore_serializada)
    texto_decodificado = descompactar_sequencia(bit_string, raiz)

    with open(nome_arquivo_saida, 'w') as f:
        f.write(texto_decodificado)

    print(f"Arquivo '{nome_arquivo_codificado}' foi descompactado para '{nome_arquivo_saida}'.")

# Função para descomprimir a sequência de bits usando a árvore de Huffman
def descompactar_sequencia(bits, raiz):
    texto_decodificado = []
    no_atual = raiz

    for bit in bits:
        if bit == b'0':
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita

        if no_atual.esquerda is None and no_atual.direita is None:
            texto_decodificado.append(no_atual.caractere)
            no_atual = raiz

    return ''.join(texto_decodificado)

    texto_decodificado = []
    no_atual = raiz
    
    for bit in bits:
        if bit == '0':
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita

        if no_atual.esquerda is None and no_atual.direita is None:
            texto_decodificado.append(no_atual.caractere)
            no_atual = raiz

    return ''.join(texto_decodificado)

# Função para ler os bits a partir de um arquivo binário.
def read_bits_from_file():
    filename = "saida.huf"
    bit_string = ''

    # Abrir o arquivo no modo leitura
    with open(filename, 'rb') as file:
        byte = file.read(1)
        while byte:
            # Converter o byte para um inteiro
            byte_value = ord(byte)
            # Converter o inteiro para sua representação binária e preencher com zeros para garantir que ele fique com 8 bits
            bits = bin(byte_value)[2:].zfill(8)
            # Fazer o append dos bits para bit_string
            bit_string += bits
            # Ler o próximo byte
            byte = file.read(1)
    
    with open(filename, 'w') as file:
        file.write(bit_string)

# Função para escrever os bits a partir de um arquivo com 0s e 1s.
def write_bits_to_file():
    with open("saida.huf", "r") as f:
                zeros_uns = f.read()

    bits = list(zeros_uns)
    bits = list(map(int, bits))

    bit_writer = BitWriter('saida.huf')

    for bit in bits:
        bit_writer.escrever_bit(bit)

    bit_writer.fechar()

# Menu para selecionar a operação
def main():
    while True:
        print("Escolha uma opção:")
        print("1. Compactar")
        print("2. Descompactar")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == '1': 
            compactar_arquivo()
            write_bits_to_file()
        elif opcao == '2':
            read_bits_from_file()
            descompactar_arquivo()
            write_bits_to_file()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
