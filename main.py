import os
import heapq
from collections import Counter
import json
import streamlit as st
import matplotlib.pyplot as plt

class BitWriter:
    def __init__(self, filename):
        self.file = open(filename, 'wb')
        self.bit_atual = 0
        self.bits_preenchidos = 0

    def escrever_bit(self, bit):
        self.bit_atual = (self.bit_atual << 1) | bit
        self.bits_preenchidos += 1
        if self.bits_preenchidos == 8:
            self.file.write(bytes([self.bit_atual]))
            self.bit_atual = 0
            self.bits_preenchidos = 0

    def fechar(self):
        if self.bits_preenchidos > 0:
            self.bit_atual = self.bit_atual << (8 - self.bits_preenchidos)
            self.file.write(bytes([self.bit_atual]))
        self.file.close()

def write_bits_to_file(bit_string, filename):
    bit_writer = BitWriter(filename)
    for bit in bit_string:
        bit_writer.escrever_bit(int(bit))
    bit_writer.fechar()

def read_bits_from_file(filename):
    bit_string = ''
    with open(filename, 'rb') as file:
        byte = file.read(1)
        while byte:
            byte_value = ord(byte)
            bits = bin(byte_value)[2:].zfill(8)
            bit_string += bits
            byte = file.read(1)
    return bit_string

class NoHuffman:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

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

def serializar_arvore(no):
    if no is None:
        return None
    return {
        'caractere': no.caractere,
        'frequencia': no.frequencia,
        'esquerda': serializar_arvore(no.esquerda),
        'direita': serializar_arvore(no.direita)
    }

def desserializar_arvore(dados):
    if dados is None:
        return None
    no = NoHuffman(dados['caractere'], dados['frequencia'])
    no.esquerda = desserializar_arvore(dados['esquerda'])
    no.direita = desserializar_arvore(dados['direita'])
    return no

def compactar_arquivo():
    nome_arquivo_entrada = "entrada.txt"
    nome_arquivo_codificado = "saida.huf"
    nome_arquivo_arvore = "arvore.json"

    with open(nome_arquivo_entrada, 'r') as f:
        texto = f.read()

    raiz = construir_arvore_huffman(texto)
    codigos = gerar_codigos_huffman(raiz)
    texto_codificado = ''.join(codigos[caractere] for caractere in texto)

    with open(nome_arquivo_arvore, 'w') as f:
        json.dump(serializar_arvore(raiz), f)

    write_bits_to_file(texto_codificado, nome_arquivo_codificado)
    print(f"Arquivo '{nome_arquivo_entrada}' foi compactado para '{nome_arquivo_codificado}'.")

def descompactar_arquivo(nome_arquivo_codificado, nome_arquivo_arvore, nome_arquivo_saida):
    with open(nome_arquivo_arvore, 'r') as f:
        arvore_serializada = json.load(f)

    bit_string = read_bits_from_file(nome_arquivo_codificado)
    raiz = desserializar_arvore(arvore_serializada)
    texto_decodificado = descompactar_sequencia(bit_string, raiz)

    with open(nome_arquivo_saida, 'w') as f:
        f.write(texto_decodificado)

    print(f"Arquivo '{nome_arquivo_codificado}' foi descompactado para '{nome_arquivo_saida}'.")

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

def main():
    st.title('Compactador e Descompactador Huffman')
    opcao = st.radio("Escolha uma opção:", ('Compactar', 'Descompactar'))
    st.set_option('deprecation.showPyplotGlobalUse', False)

    if opcao == 'Compactar':
        if st.button('Compactar arquivo entrada.txt'):
            compactar_arquivo()
            st.success("Arquivo compactado e bits salvos com sucesso!")

            tamanho_original = os.path.getsize('entrada.txt')
            tamanho_compactado = os.path.getsize('saida.huf')

            st.subheader('Gráfico de comparação de tamanhos')
            labels = ['Original', 'Compactado']
            sizes = [tamanho_original, tamanho_compactado]
            explode = (0, 0.1)
            fig, ax = plt.subplots()
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
            st.pyplot(fig)

    elif opcao == 'Descompactar':
        if st.button('Descompactar arquivo'):
            descompactar_arquivo('saida.huf', 'arvore.json', 'descompactado.txt')
            st.success("Arquivo descompactado com sucesso!")

            tamanho_compactado = os.path.getsize('saida.huf')
            tamanho_descompactado = os.path.getsize('descompactado.txt')

            st.subheader('Gráfico de comparação de tamanhos')
            labels = ['Compactado', 'Descompactado']
            sizes = [tamanho_compactado, tamanho_descompactado]
            explode = (0, 0.1)
            fig, ax = plt.subplots()
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
