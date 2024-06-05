# EcoDrones - Tecnologia de Limpeza de Lixo Marinho

EcoDrones é um programa que simula a operação de drones para a limpeza de lixo marinho. O programa gera um "mapa do mar" com lixo distribuído aleatoriamente e permite que o usuário controle o processo de limpeza, registre logs de temperatura e salve os dados em arquivos.

<img src="https://github.com/LucasLCabral/EcoDrone-Python-GlobalSolution/assets/162235385/7a1e6776-8523-49d9-8b99-5791fdeeb75b" alt="drone-simulacao" width="500" align-itens="center"/>

## Autores:
    Lucas Ludovico Cabral - RM554589
    Weslley Oliveira Cardoso - RM557927

## Funcionalidades

- **Limpeza do Mar**: Simulação de limpeza de lixo marinho por drones.
- **Log de Limpeza**: Registro detalhado de cada operação de limpeza com data, hora e temperatura.
- **Visualização de Temperaturas**: Exibição das temperaturas registradas em um DataFrame.
- **Salvar Log em Arquivo**: Possibilidade de salvar o log das operações de limpeza em um arquivo de texto.

## Instalação

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/seu-usuario/ecodrones.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd ecodrones
    ```

3. Instale as dependências:
    ```sh
    pip install pandas
    ```

## Uso

1. Execute o programa:
    ```sh
    python ecodrones.py
    ```

2. Escolha uma das opções do menu principal:
    - **[1] Limpar o mar**: Inicia uma nova rodada de limpeza.
    - **[2] Log limpeza**: Exibe o log de todas as operações de limpeza realizadas.
    - **[3] Mostrar DataFrame com temperaturas**: Mostra um DataFrame com as temperaturas registradas em cada rodada.
    - **[4] Salvar log em arquivo**: Salva o log atual em um arquivo de texto.
    - **[5] Finalizar programa**: Encerra o programa.

## Exemplo de Uso

```plaintext
██████╗░██╗░░░░░██╗░░░██╗███████╗  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗
██╔══██╗██║░░░░░██║░░░██║██╔════╝  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║
██████╦╝██║░░░░░██║░░░██║█████╗░░  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║
██╔══██╗██║░░░░░██║░░░██║██╔══╝░░  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║
██████╦╝███████╗╚██████╔╝███████╗  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║
╚═════╝░╚══════╝░╚═════╝░╚══════╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝

[1] - Limpar o mar
[2] - Log limpeza
[3] - Mostrar DataFrame com temperaturas
[4] - Salvar log em arquivo
[5] - Finalizar programa
Escolha uma opção: 1
````
Estrutura do Código
eco_drones.py: Contém a lógica principal do programa.
log.txt: Arquivo de log gerado ao salvar o log das operações de limpeza.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Os direitos estão reservados pelo grupo Blue Clean - 1ESPI. Global Solution 2024, first semester.

Contato
Se você tiver alguma dúvida ou sugestão, entre em contato:

Email: lucasludovicocabraal@gmail.com
GitHub:  LucasLCabral
