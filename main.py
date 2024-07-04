import streamlit as st
import matplotlib.pyplot as plt
from compactar_descompactar import compactar_arquivo, descompactar_arquivo, write_bits_to_file
import os

def main():
    st.title('Compactador e Descompactador Huffman')

    opcao = st.radio("Escolha uma opção:", ('Compactar', 'Descompactar'))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    if opcao == 'Compactar':
        if st.button('Compactar arquivo entrada.txt'):
            compactar_arquivo()
            write_bits_to_file()
            st.success("Arquivo compactado e bits salvos com sucesso!")
            
            # Calculando tamanhos
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
            
            # Calculando tamanhos
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
