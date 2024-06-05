import random
import time
import os
from datetime import datetime
import pandas as pd

# ANSI colors
red = "\033[31m"
white = "\033[37m"
reset = "\033[0m"
bg_blue = "\033[44m"

# Blue Clean estilizado
blue_clean = """
██████╗░██╗░░░░░██╗░░░██╗███████╗  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗
██╔══██╗██║░░░░░██║░░░██║██╔════╝  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║
██████╦╝██║░░░░░██║░░░██║█████╗░░  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║
██╔══██╗██║░░░░░██║░░░██║██╔══╝░░  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║
██████╦╝███████╗╚██████╔╝███████╗  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║
╚═════╝░╚══════╝░╚═════╝░╚══════╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝
"""

def print_matriz(matriz):
    # Imprime a matriz do mar com cores indicando as células de lixo
    for linha in matriz:
        for celula in linha:
            if celula == 1:
                print(f'{bg_blue}{red}{celula}{reset}{bg_blue}', end=' ')
            else:
                print(f'{bg_blue}{white}{celula}{reset}{bg_blue}', end=' ')
        print(reset)
    print()

def find_trash(matriz):
    # Encontra a posição do lixo na matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                return i, j  # Retorna a posição do lixo
    return None  # Retorna nada caso nao encontre lixo

def simular_temp(matriz):
    # Simula as temperaturas para cada célula da matriz
    temperaturas = []
    for linha in matriz:
        temp_linha = []
        for celula in linha:
            base_temp = 25
            if celula == 1:
                aumenta_temp = random.uniform(0, 10)
            else:
                aumenta_temp = random.uniform(0, 2)
            temp_linha.append(base_temp + aumenta_temp)
        temperaturas.append(temp_linha)  # Adiciona temp_linha à lista de temperaturas
    return temperaturas  # Retorna a lista completa de temperaturas

def limpar_matriz(matriz, temperaturas, log, num_rodada, coordenadas, dataframes):
    # Limpa a matriz de lixo, atualiza as temperaturas e registra no log
    todas_as_temperaturas = []
    while True:
        posicao_do_lixo = find_trash(matriz)
        if posicao_do_lixo:
            linha, coluna = posicao_do_lixo
            horario_coleta = datetime.now().strftime("%d/%m/%Y - %H:%M")
            temp = temperaturas[linha][coluna]
            todas_as_temperaturas.append(temp)
            entrada_log = f"Lixo na posição Coluna {coluna}, Linha {linha} (Temp: {temp:.2f}°C) limpo às {horario_coleta}"
            log.append((num_rodada, coordenadas, entrada_log))
            print(f"Lixo encontrado na posição: Coluna {coluna}, Linha {linha} (Temp: {temp:.2f}°C)")
            print("Limpando...")
            matriz[linha][coluna] = 0  # Limpa o lixo da matriz
            time.sleep(1)
            clear_terminal()
            print_matriz(matriz)
        else:
            break
    
    if todas_as_temperaturas:
        df_temperaturas = pd.DataFrame(todas_as_temperaturas, columns=['Temperatura'])
        media_temp = df_temperaturas['Temperatura'].mean()
        df_temperaturas['Média'] = media_temp  # Adiciona a coluna de média ao DataFrame
        entrada_log = f"Média de temperatura na {num_rodada}ª rodada: {media_temp:.2f}°C"
        log.append((num_rodada, coordenadas, entrada_log))
        dataframes[num_rodada] = df_temperaturas  # Salva o DataFrame para a rodada

def clear_terminal():
    # Limpa o terminal
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, MacOs
        os.system('clear')

def show_log(log):
    # Mostra o log das operações de limpeza.
    if not log:
        print('Sem registros por enquanto')
    else:
        rodada_atual = 0
        for entrada in log:
            num_rodada, coordenadas, entrada_log = entrada
            if num_rodada != rodada_atual:
                rodada_atual = num_rodada
                print(f"\n{rodada_atual}ª Rodada de limpeza - Coordenada: Latitude {coordenadas[0]}, Longitude {coordenadas[1]}")
            print(entrada_log)
    print()
    input("Pressione Enter para voltar ao menu principal...")

def show_temperatures(dataframes):
    # Mostra os DataFrames de temperaturas registrados para cada rodada
    if not dataframes:
        print('Nenhuma rodada foi registrada ainda.')
    else:
        for num_rodada, df in dataframes.items():
            print(f"\n{num_rodada}ª Rodada de limpeza - Temperaturas registradas:")
            print(df)
    print()
    input("Pressione Enter para voltar ao menu principal...")

def salvar_arquivo_log(log):
    # Salva o log em um arquivo de texto
    if not log:
        print('Sem registros para salvar.')
    else:
        filename = input("Digite o nome do arquivo para salvar o log (exemplo: log.txt): ").strip()
        with open(filename, 'w') as file:
            rodada_atual = 0
            for entrada in log:
                num_rodada, coordenadas, entrada_log = entrada
                if num_rodada != rodada_atual:
                    rodada_atual = num_rodada
                    file.write(f"\n{rodada_atual}ª Rodada de limpeza - Coordenada: Latitude {coordenadas[0]}, Longitude {coordenadas[1]}\n")
                file.write(entrada_log + '\n')
        print(f"Log salvo no arquivo {filename} com sucesso!")
    input("Pressione Enter para voltar ao menu principal...")

def gerar_coordenadas_aleatorias():
    # Gera coordenadas aleatórias para o drone
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    return latitude, longitude

def main():
    # Função principal que gerencia o menu e as operações do programa
    log = []
    dataframes = {}
    num_rodada = 0

    while True:
        clear_terminal()
        print(blue_clean)
        print("[1] - Limpar o mar")
        print("[2] - Log limpeza")
        print("[3] - Mostrar DataFrame com temperaturas")
        print("[4] - Salvar log em arquivo")
        print("[5] - Finalizar programa")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            num_rodada += 1
            print("Bem-vindo à Tecnologia de Limpeza de Lixo Marinho - EcoDrones")
            print("Vamos mostrar o 'mapa do mar'.\n")

            # Escolha do tamanho da matriz
            while True:
                try:
                    linhas = int(input("Digite o número de linhas da matriz: ").strip())
                    colunas = int(input("Digite o número de colunas da matriz: ").strip())
                    if linhas > 0 and colunas > 0:
                        break
                    else:
                        print('Por favor, insira valores maiores que 0.')
                except ValueError:
                    print('Por favor, insira números inteiros válidos!')
            coordenadas = gerar_coordenadas_aleatorias()
            print(f'O drone está a caminho para as coordenadas: Latitude {coordenadas[0]}, Longitude {coordenadas[1]}\n')
            time.sleep(2)

            while True:
                # Gera a matriz de lixo com valores aleatórios
                matriz = [[random.choice([0, 1]) for _ in range(colunas)] for _ in range(linhas)]

                temperaturas = simular_temp(matriz)

                print('Mapa do mar inicial:')
                print_matriz(matriz)

                limpar_matriz(matriz, temperaturas, log, num_rodada, coordenadas, dataframes)
                print('Todo o lixo foi limpo!')
                print('Mapa do mar final:')
                print_matriz(matriz)

                cont = input("Deseja continuar buscando lixo? (S/N): ").strip().upper()
                if cont != 'S':
                    break
        elif escolha == '2':
            clear_terminal()
            print(blue_clean)
            show_log(log)

        elif escolha == '3':
            clear_terminal()
            print(blue_clean)
            show_temperatures(dataframes)

        elif escolha == '4':
            clear_terminal()
            print(blue_clean)
            salvar_arquivo_log(log)

        elif escolha == '5':
            print('Finalizando o programa...')
            break

        else:
            print('Opção inválida! Tente novamente.')

if __name__ == "__main__":
    main()
