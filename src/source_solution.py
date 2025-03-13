import pandas as pd  # Importa a biblioteca pandas para manipulação de dados e criação de tabelas


def problem_01():
    # Solicita ao usuário os dados de entrada necessários para a solução do problema
    N = int(input('Numero de pontos: '))  # Número de pontos discretos na barra
    K = float(input('Condutividade: '))  # Condutividade térmica do material da barra
    TE = float(input('Temperatura da esquerda "<------": '))  # Temperatura na extremidade esquerda da barra
    TD = float(input('Temperatura da direita  "------>": '))  # Temperatura na extremidade direita da barra
    comp = float(input('Comprimento da barra: '))  # Comprimento total da barra
    ger = float(input('Geração de calor: ')) or 0.0  # Quantidade de calor gerado por unidade de volume (se não fornecido, assume-se 0)

    dx = comp / N  # Passo de discretização, que define a distância entre os pontos

    # Inicializa os vetores necessários para a resolução do sistema
    A = [0.0] * (N + 1)  # Coeficiente da diagonal principal
    B = [0.0] * (N + 1)  # Coeficiente da diagonal superior
    C = [0.0] * (N + 1)  # Coeficiente da diagonal inferior
    D = [0.0] * (N + 1)  # Vetor de termos independentes
    P = [0.0] * (N + 1)  # Vetor auxiliar para o método de Thomas (eliminação progressiva)
    Q = [0.0] * (N + 1)  # Outro vetor auxiliar para o método de Thomas
    T = [0.0] * (N + 1)  # Solução final contendo as temperaturas nos pontos discretizados

    # Condições de contorno: extremidades esquerda e direita da barra
    A[0] = 3  # Coeficiente da equação na extremidade esquerda
    B[0] = 1  # Coeficiente da equação na extremidade esquerda
    C[0] = 0  # Não há coeficiente inferior na extremidade esquerda
    D[0] = 2 * TE + ger * dx**2 / K  # Termo independente da equação na extremidade esquerda

    A[N-1] = 3  # Coeficiente da equação na extremidade direita
    B[N-1] = 0  # Não há coeficiente superior na extremidade direita
    C[N-1] = 1  # Coeficiente da equação na extremidade direita
    D[N-1] = 2 * TD + ger * dx**2 / K  # Termo independente da equação na extremidade direita

    # Preenchendo os coeficientes das equações para os pontos internos
    for j in range(1, N-1):
        A[j] = 2  # Coeficiente principal (diagonal principal)
        B[j] = 1  # Coeficiente superior
        C[j] = 1  # Coeficiente inferior
        D[j] = ger * dx**2 / K  # Termo independente devido à geração de calor

    # Aplicando o método de Thomas (eliminação progressiva para resolver sistemas tridiagonais)
    for j in range(N):
        if j == 0:
            # Primeira iteração - Normalização da primeira equação
            P[j] = B[j] / (A[j] - C[j] * 0)
            Q[j] = (D[j] + C[j] * 0) / (A[j] - C[j] * 0)
        else:
            # Demais iterações - Aplicação do método de Thomas
            P[j] = B[j] / (A[j] - C[j] * P[j-1])
            Q[j] = (D[j] + C[j] * Q[j-1]) / (A[j] - C[j] * P[j-1])

    # Substituição regressiva para obter as temperaturas nos pontos discretizados
    for j in range(N-1, -1, -1):
        if j == N-1:
            T[j] = P[j] * 0 + Q[j]  # Última temperatura calculada diretamente
        else:
            T[j] = P[j] * T[j+1] + Q[j]  # Propagação das temperaturas para trás

    # Criando um DataFrame do pandas para armazenar e exibir os resultados
    data = {
        "Temperatura Numérica (°C)": [T[j] for j in range(N)],  # Valores calculados
        "Temperatura Exata (°C)": [
            # Cálculo da solução analítica (exata) para comparação
            -ger * (dx / 2 + (j) * dx) * 2 / (2 * K) + (ger * comp * 2 / (2 * K) + (TD - TE) * (dx / 2 + (j) * dx) / comp + TE)
            for j in range(N)
        ],
        'Erro': [
            dx / 2 + (j) * dx  # Diferença entre os pontos, usada para análise do erro
            for j in range(N)
        ],
    }

    df = pd.DataFrame(data)  # Criando um DataFrame com os resultados
    return [df, df.to_numpy()]  # Retornando o DataFrame e um array NumPy com os resultados


# Função para rodar o problema repetidamente até receber entradas válidas
def search_solution_problem_01():
    while True:
        try:
            data = problem_01()  # Chama a função principal para resolver o problema
            return data  # Retorna os resultados quando bem-sucedido
        except Exception:
            print('Digite uma entrada válida...\n\n')  # Mensagem de erro para entrada inválida
