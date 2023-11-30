# Busca CEP App

Este é um aplicativo simples de busca de CEP desenvolvido em Python usando a biblioteca Tkinter. Ele permite que o usuário insira um CEP e obtenha informações sobre o endereço correspondente.

## Como Executar o Aplicativo:

1. **Pré-requisitos:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale as dependências usando o seguinte comando:
     ```
     pip install customtkinter
     ```

2. **Execução:**
   - Execute o script Python `busca_cep.py`.

## Funcionalidades:

- **Busca de CEP:**
  - Insira o CEP desejado no campo de entrada.
  - Clique no botão "Search" para obter informações sobre o CEP.

- **Limpar Resultados:**
  - Clique no botão "Clear" para limpar as informações exibidas.

## Estrutura do Código:

- **Módulos:**
  - O código é dividido em módulos para facilitar a leitura e manutenção.
  - Módulos incluem `customtkinter` para elementos personalizados do Tkinter e `functions` para a função de busca de CEP.

- **Função de Busca de CEP:**
  - A função `searchCep` no módulo `functions` realiza a busca de CEP e retorna as informações.

- **Interface Gráfica:**
  - Utiliza a biblioteca Tkinter para criar uma interface simples.
  - Elementos como entrada (`Entry`), botões (`Button`), e rótulos (`Label`) são personalizados com a biblioteca `customtkinter`.

## Contribuições e Problemas Conhecidos:

- Contribuições são bem-vindas. Se encontrar problemas ou tiver sugestões de melhoria, abra uma *issue* neste repositório.

## Licença:

Este projeto está sob a licença [MIT](LICENSE).

Desenvolvido por Felipe.