import heapq
from collections import Counter, defaultdict
import json

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
def compactar_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r') as f:
        texto = f.read()

    raiz = construir_arvore_huffman(texto)
    codigos = gerar_codigos_huffman(raiz)
    texto_codificado = ''.join(codigos[caractere] for caractere in texto)

    # Salvar a árvore de Huffman e o texto codificado em saida.huf
    with open(nome_arquivo_saida, 'w') as f:
        json.dump({'arvore': serializar_arvore(raiz), 'dados': texto_codificado}, f)

    print(f"Arquivo '{nome_arquivo_entrada}' foi compactado para '{nome_arquivo_saida}'.")

# Função para descompactar um arquivo comprimido usando Huffman
def descompactar_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r') as f:
        conteudo = json.load(f)

    arvore_serializada = conteudo['arvore']
    texto_codificado = conteudo['dados']

    raiz = desserializar_arvore(arvore_serializada)
    texto_decodificado = descompactar_sequencia(texto_codificado, raiz)

    with open(nome_arquivo_saida, 'w') as f:
        f.write(texto_decodificado)

    print(f"Arquivo '{nome_arquivo_entrada}' foi descompactado para '{nome_arquivo_saida}'.")

# Função para descomprimir a sequência de bits usando a árvore de Huffman
def descompactar_sequencia(bits, raiz):
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

# Menu para selecionar a operação
def main():
    while True:
        print("Escolha uma opção:")
        print("1. Compactar")
        print("2. Descompactar")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
            nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
            compactar_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
        elif opcao == '2':
            nome_arquivo_entrada = input("Digite o nome do arquivo comprimido (entrada): ")
            nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
            descompactar_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
