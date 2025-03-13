# Importa funções específicas do módulo generate_file para manipulação de nomes de arquivos e diretórios
from generate_file import generate_name_file, select_next_path, remover_utf8  

# Importa a biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importa a biblioteca NumPy para operações numéricas eficientes
import numpy as np  


# Função para gerar um gráfico de linhas comparando temperaturas numéricas, analíticas e o erro associado
def plot_lines(data, path, files, name, extension):
    # Remove caracteres especiais do nome do arquivo, substitui a extensão e converte para maiúsculas
    name = remover_utf8(name).replace(extension, '').upper()

    # Converte os dados para um array NumPy para facilitar a manipulação
    data = np.array(data)

    # Cria um eixo X com base no número de pontos nos dados
    x = np.arange(len(data))

    # Configura o tamanho da figura do gráfico
    plt.figure(figsize=(10, 5))

    # Plota os dados: 
    # data[:, 0] -> Temperatura Numérica
    # data[:, 1] -> Temperatura Analítica
    # data[:, 2] -> Erro
    plt.plot(x, data[:, 0], marker="o", linestyle="-", label="Temperatura Numérica")  # Linha contínua com marcadores "o"
    plt.plot(x, data[:, 1], marker="s", linestyle="--", label="Temperatura Analítica")  # Linha tracejada com quadrados
    plt.plot(x, data[:, 2], marker="d", linestyle=":", label="Erro")  # Linha pontilhada com losangos

    # Configurações do gráfico
    plt.xlabel("Pontos")  # Nome do eixo X
    plt.ylabel("Valores")  # Nome do eixo Y
    plt.title("Comparação de Temperaturas e Erro")  # Título do gráfico
    plt.legend()  # Adiciona a legenda para identificar as curvas
    plt.grid()  # Adiciona grade no fundo para facilitar a visualização

    # Salva o gráfico gerado no caminho correto com o nome de arquivo formatado
    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)

    # Fecha o gráfico para liberar memória
    plt.close()


# Função para gerar um mapa de calor da temperatura, podendo ser numérica ou analítica
def plot_temperature(data, path, files, name, extension, mode='NUMERIC'):
    # Remove caracteres especiais do nome do arquivo, substitui a extensão e converte para maiúsculas
    name = remover_utf8(name).replace(extension, '').upper()

    # Seleciona os dados de acordo com o modo escolhido: 
    # 'analytic' -> Usa a segunda coluna (temperatura analítica)
    # 'numeric'  -> Usa a primeira coluna (temperatura numérica)
    if mode.lower() == 'analytic':
        data_numeric = np.array(data)[:, 1]
    else:
        data_numeric = np.array(data)[:, 0]

    # Define o tamanho da figura
    plt.figure(figsize=(10, 5))

    # Gera o mapa de calor usando a função imshow() 
    # cmap="coolwarm" -> Define a coloração do mapa (azul para frio e vermelho para quente)
    # aspect="auto" -> Ajusta automaticamente a proporção do gráfico
    plt.imshow(data_numeric.reshape(1, -1), cmap="coolwarm", aspect="auto")

    # Adiciona uma barra de cores para indicar a escala de temperatura
    plt.colorbar(label="Temperatura (°C)")

    # Configura os eixos:
    if len(data_numeric) > 10:
        plt.xticks([])  # Remove os rótulos do eixo X, pois vai ficar com muitas informações de pontos
    else:
        plt.xticks(np.arange(len(data_numeric)), labels=np.arange(1, len(data_numeric) + 1))  # Define os rótulos no eixo X
    plt.yticks([])  # Remove os rótulos do eixo Y, pois não há necessidade de marcações verticais

    # Define o título com base no modo escolhido (numérico ou analítico)
    plt.title("Mapa de Calor da Temperatura Numérica" if mode.lower() == 'numeric' else "Mapa de Calor da Temperatura Analítica")

    # Define os rótulos dos eixos
    plt.xlabel("Pontos")
    plt.ylabel("")

    # Salva o gráfico gerado no caminho correto com o nome formatado
    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)

    # Fecha o gráfico para evitar consumo excessivo de memória
    plt.close()


# Função para gerar um gráfico de barras comparando temperaturas numéricas, analíticas e o erro
def plot_bar(data, path, files, name, extension):
    # Remove caracteres especiais do nome do arquivo, substitui a extensão e converte para maiúsculas
    name = remover_utf8(name).replace(extension, '').upper()

    # Converte os dados para um array NumPy
    data = np.array(data)

    # Cria um eixo X com base no número de pontos
    x = np.arange(len(data))

    # Define a largura das barras para melhor visualização
    largura = 0.3  

    # Configura o tamanho da figura
    plt.figure(figsize=(10, 5))

    # Plota três conjuntos de barras lado a lado:
    # - Temperatura Numérica (azul)
    # - Temperatura Analítica (vermelho)
    # - Erro (verde)
    plt.bar(x - largura, data[:, 0], width=largura, label="Temperatura Numérica", color="blue")  # Barras azuis
    plt.bar(x, data[:, 1], width=largura, label="Temperatura Analítica", color="red")  # Barras vermelhas
    plt.bar(x + largura, data[:, 2], width=largura, label="Erro", color="green")  # Barras verdes

    # Configura os rótulos do gráfico
    plt.xlabel("Pontos")  # Nome do eixo X
    plt.ylabel("Valores")  # Nome do eixo Y
    plt.title("Gráfico de Barras: Temperaturas e Erro")  # Título do gráfico
    plt.legend()  # Adiciona legenda para identificar os conjuntos de dados

    # Adiciona uma grade no fundo do gráfico apenas no eixo Y, com estilo tracejado e transparência
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Salva o gráfico gerado no caminho correto com o nome formatado
    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)

    # Fecha o gráfico para evitar consumo excessivo de memória
    plt.close()
