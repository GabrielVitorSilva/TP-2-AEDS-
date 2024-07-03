# Compressor de Arquivos usando Huffman

Este projeto implementa um compressor e descompressor de arquivos de texto usando a codificação de Huffman. O programa compacta o conteúdo de um arquivo `entrada.txt` e gera dois arquivos de saída: `saida.huf`, que contém o texto codificado em binário, e `arvore.json`, que armazena a árvore de Huffman utilizada na codificação. Para descompactar, o programa lê esses arquivos de saída e gera um arquivo `descompactado.txt` com o conteúdo original.

## Funcionamento

### Compactação
1. O programa lê o arquivo `entrada.txt`.
2. Calcula a frequência de cada caractere no texto e constrói a árvore de Huffman.
3. Gera códigos binários para cada caractere com base na árvore de Huffman.
4. Codifica o texto original usando esses códigos binários.
5. Salva a árvore de Huffman em `arvore.json` e o texto codificado em `saida.huf`.

### Descompactação
1. O programa lê a árvore de Huffman de `arvore.json` e o texto codificado de `saida.huf`.
2. Reconstrói a árvore de Huffman.
3. Decodifica o texto binário usando a árvore reconstruída.
4. Salva o texto original em `descompactado.txt`.

## Estrutura do Projeto

- `huffman.py`: Arquivo principal contendo o código do compressor e descompressor.
- `entrada.txt`: Arquivo de texto a ser compactado.
- `saida.huf`: Arquivo gerado contendo o texto codificado em binário.
- `arvore.json`: Arquivo gerado contendo a árvore de Huffman.
- `descompactado.txt`: Arquivo gerado após a descompactação, contendo o texto original.

## Como Executar

### Pré-requisitos

- Python 3.x

### Passos

1. **Clone o repositório ou faça o download dos arquivos**:

   ```sh
   git clone https://github.com/GabrielVitorSilva/TP-2-AEDS-
   cd repository
2. **Crie ou coloque o arquivo entrada.txt na mesma pasta que o script huffman.py. Este arquivo deve conter o texto que você deseja compactar.**
3. **Executar o script**
  python huffman.py
4. **Siga as instruções no menu:**
  .Digite 1 para compactar o arquivo entrada.txt. Isso gerará os arquivos saida.huf e arvore.json.
  .Digite 2 para descompactar os arquivos saida.huf e arvore.json. Isso gerará o arquivo descompactado.txt.
  .Digite 3 para sair do programa.
### Exemplo de Execução

Suponha que você tenha um arquivo `entrada.txt` com o seguinte conteúdo: 

Este é um exemplo de texto para testar o algoritmo de compressão de Huffman.
Este texto será compactado e descompactado para verificar a eficiência do algoritmo.

Ao executar o script e escolher a opção `1`, serão gerados dois arquivos:

- `saida.huf`: Contém o texto codificado em binário.
- `arvore.json`: Contém a árvore de Huffman utilizada para a codificação.

Para descompactar, execute o script novamente e escolha a opção `2`. O arquivo `descompactado.txt` será gerado com o conteúdo original:
Este é um exemplo de texto para testar o algoritmo de compressão de Huffman.
Este texto será compactado e descompactado para verificar a eficiência do algoritmo.

## Explicação do Código

### Estruturas de Dados

- **NoHuffman**: Classe que representa um nó na árvore de Huffman. Cada nó armazena um caractere, sua frequência e referências para os filhos esquerdo e direito.
- **Counter**: Utilizado para contar a frequência de cada caractere no texto.

### Funções Principais

- **construir_arvore_huffman**: Constrói a árvore de Huffman a partir de um texto.
- **gerar_codigos_huffman**: Gera os códigos binários para cada caractere usando a árvore de Huffman.
- **serializar_arvore**: Serializa a árvore de Huffman para um formato que pode ser salvo em um arquivo JSON.
- **desserializar_arvore**: Reconstrói a árvore de Huffman a partir de um arquivo JSON.
- **compactar_arquivo**: Lê o arquivo `entrada.txt`, compacta seu conteúdo e salva os arquivos `saida.huf` e `arvore.json`.
- **descompactar_arquivo**: Lê os arquivos `saida.huf` e `arvore.json`, descompacta o conteúdo e salva o arquivo `descompactado.txt`.
- **descompactar_sequencia**: Descompacta uma sequência de bits usando a árvore de Huffman.

### Menu de Navegação

O menu permite ao usuário escolher entre compactar, descompactar ou sair do programa. As funções são chamadas com base na escolha do usuário.

## Conclusão

Este projeto demonstra a implementação da codificação de Huffman para compressão e descompressão de arquivos de texto. O uso de arquivos separados para o texto codificado e a árvore de Huffman garante que apenas o código binário seja armazenado no arquivo compactado principal, otimizando a eficiência do armazenamento.
