# Compactador e Descompactador Huffman

Este projeto implementa um compactador e descompactador de arquivos utilizando o algoritmo de compressão de Huffman. O código inclui uma interface interativa construída com Streamlit para facilitar o uso das funcionalidades de compactação e descompactação.

## Descrição

O algoritmo de Huffman é uma técnica de compressão de dados sem perdas. Ele utiliza uma árvore binária para codificar os caracteres com base em suas frequências, atribuindo códigos mais curtos aos caracteres mais frequentes.

## Componentes do Projeto

### Classes e Funções do Algoritmo de Huffman:

- **NoHuffman**: Classe que representa um nó na árvore de Huffman.
- **construir_arvore_huffman**: Constrói a árvore de Huffman a partir de um texto.
- **gerar_codigos_huffman**: Gera os códigos de Huffman a partir da árvore.
- **serializar_arvore** e **desserializar_arvore**: Serializam e desserializam a árvore de Huffman.
- **compactar_arquivo**: Compacta um arquivo de texto utilizando Huffman.
- **descompactar_arquivo**: Descompacta um arquivo comprimido utilizando Huffman.
- **descompactar_sequencia**: Descompacta a sequência de bits utilizando a árvore de Huffman.

### Classes e Funções de Manipulação de Bits:

- **BitWriter**: Classe que escreve bits em um arquivo binário.
- **write_bits_to_file**: Função que escreve uma string de bits em um arquivo binário.
- **read_bits_from_file**: Função que lê um arquivo binário e retorna uma string de bits.

### Interface com Streamlit:

A interface permite que o usuário escolha entre compactar ou descompactar um arquivo e exibe gráficos comparativos dos tamanhos dos arquivos.

## Como Rodar o Código

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias: streamlit, matplotlib

Você pode instalar as bibliotecas necessárias usando pip:

## - pip install streamlit matplotlib

### Arquivos Necessários
- entrada.txt: Arquivo de texto a ser compactado.
- compactar_descompactar.py: Arquivo contendo a implementação das funções de compactação e descompactação.
- Executando o Projeto
- Criar o Arquivo de Entrada:
- Certifique-se de ter um arquivo chamado entrada.txt no mesmo diretório que o código, contendo o texto que você deseja compactar.

#### Rodar o Script com Streamlit:
Execute o seguinte comando no terminal para iniciar a aplicação Streamlit:
## streamlit run main.py
## Utilizar a Interface:

### Compactar Arquivo:

- Selecione a opção "Compactar".
- Clique no botão "Compactar arquivo entrada.txt".
- O arquivo compactado será salvo como `saida.huf`, e a árvore de Huffman será salva como `arvore.json`.
- Um gráfico comparativo dos tamanhos dos arquivos original e compactado será exibido.

### Descompactar Arquivo:

- Selecione a opção "Descompactar".
- Clique no botão "Descompactar arquivo".
- O arquivo descompactado será salvo como `descompactado.txt`.
- Um gráfico comparativo dos tamanhos dos arquivos compactado e descompactado será exibido.

## Observações

- Certifique-se de que os arquivos `entrada.txt`, `saida.huf`, `arvore.json`, e `descompactado.txt` estejam no mesmo diretório do script.
- Para melhor visualização dos gráficos no Streamlit, instale o matplotlib.

## Exemplo de Uso

### Para compactar um arquivo de texto:

1. Coloque o texto que deseja compactar no arquivo `entrada.txt`.
2. Execute o script com o Streamlit.
3. Selecione a opção "Compactar" e clique no botão para compactar o arquivo.
4. Verifique o tamanho do arquivo original e compactado no gráfico exibido.

### Para descompactar o arquivo:

1. Execute o script com o Streamlit.
2. Selecione a opção "Descompactar" e clique no botão para descompactar o arquivo.
3. Verifique o tamanho do arquivo compactado e descompactado no gráfico exibido.

Com essas instruções, você poderá utilizar e entender melhor o funcionamento do compactador e descompactador de Huffman implementado.
