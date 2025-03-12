import pandas as pd


def problem_01():
    N = int(input('Numero de pontos: '))
    K = float(input('Condutividade: '))
    TE = float(input('Temperatura da esquerda "<------": '))
    TD = float(input('Temperatura da direita  "------>": '))
    comp = float(input('Comprimento da barra: '))
    ger = float(input('Geração de calor: ')) or 0.0
    
    # N = 10
    # K = 1000
    # TE = 100
    # TD = 500
    # comp = 0.5
    # ger = 0
    
    dx = comp / N
    
    A = [0.0] * (N + 1)
    B = [0.0] * (N + 1)
    C = [0.0] * (N + 1)
    D = [0.0] * (N + 1)
    P = [0.0] * (N + 1)
    Q = [0.0] * (N + 1)
    T = [0.0] * (N + 1)
    
    A[0] = 3
    B[0] = 1
    C[0] = 0
    D[0] = 2 * TE + ger * dx**2 / K

    A[N-1] = 3
    B[N-1] = 0
    C[N-1] = 1
    D[N-1] = 2 * TD + ger * dx**2 / K

    for j in range(1, N-1):
        A[j] = 2
        B[j] = 1
        C[j] = 1
        D[j] = ger * dx**2 / K

    for j in range(N):
        if j == 0:
            P[j] = B[j] / (A[j] - C[j] * 0)
            Q[j] = (D[j] + C[j] * 0) / (A[j] - C[j] * 0)
        else:
            P[j] = B[j] / (A[j] - C[j] * P[j-1])
            Q[j] = (D[j] + C[j] * Q[j-1]) / (A[j] - C[j] * P[j-1])

    for j in range(N-1, -1, -1):
        if j == N-1:
            T[j] = P[j] * 0 + Q[j]
        else:
            T[j] = P[j] * T[j+1] + Q[j]

    data = {
        "Temperatura Numérica (°C)": [T[j] for j in range(N)],
        "Temperatura Exata (°C)": [
            -ger * (dx / 2 + (j) * dx) * 2 / (2 * K) + (ger * comp * 2 / (2 * K) + (TD - TE) * (dx / 2 + (j) * dx) / comp + TE)
            for j in range(N)
        ],
        'Erro': [
            dx / 2 + (j) * dx
            for j in range(N)
        ],
    }

    df = pd.DataFrame(data)
    return [df, df.to_numpy()]

def search_solution_problem_01():
    while True:
        try:
            data = problem_01()
            return data
        except Exception:
            print('Digite uma entrada válida...\n\n')

