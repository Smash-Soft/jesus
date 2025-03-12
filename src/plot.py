from generate_file import generate_name_file, select_next_path, remover_utf8
import matplotlib.pyplot as plt
import numpy as np


def plot_lines(data, path, files, name, extension):
    name = remover_utf8(name).replace(extension, '').upper()
    data = np.array(data)
    x = np.arange(len(data))
    
    # deferred_numeric = np.abs(data[:, 0] - data[:, 1])
    # deferred_analytic = np.floor(data[:, 1])
    # deferred_analytic = np.where(deferred_analytic <= data[:, 1], deferred_analytic, deferred_analytic - deferred_numeric - 0.1)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, data[:, 0], marker="o", linestyle="-", label="Temperatura Numérica")
    plt.plot(x, data[:, 1], marker="s", linestyle="--", label="Temperatura Analítica")
    plt.plot(x, data[:, 2], marker="d", linestyle=":", label="Erro")

    plt.xlabel("Pontos")
    plt.ylabel("Valores")
    plt.title("Comparação de Temperaturas e Erro")
    plt.legend()
    plt.grid()
    
    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)
    plt.close()

def plot_temperature(data, path, files, name, extension, mode='NUMERIC'):
    name = remover_utf8(name).replace(extension, '').upper()
    if mode.lower() == 'analytic':
        data_numeric = np.array(data)[:, 1]
    else:
        data_numeric = np.array(data)[:, 0]

    plt.figure(figsize=(10, 5))
    
    plt.imshow(data_numeric.reshape(1, -1), cmap="coolwarm", aspect="auto")

    plt.colorbar(label="Temperatura (°C)")
    plt.xticks(np.arange(len(data_numeric)), labels=np.arange(1, len(data_numeric) + 1))
    plt.yticks([])
    
    plt.title("Mapa de Calor da Temperatura Numérica" if mode.lower() == 'numeric' else "Mapa de Calor da Temperatura Analítica")
    plt.xlabel("Pontos")
    plt.ylabel("")

    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)
    plt.close()

def plot_bar(data, path, files, name, extension):
    name = remover_utf8(name).replace(extension, '').upper()
    data = np.array(data)
    x = np.arange(len(data))
    largura = 0.3 

    plt.figure(figsize=(10, 5))
    plt.bar(x - largura, data[:, 0], width=largura, label="Temperatura Numérica", color="blue")
    plt.bar(x, data[:, 1], width=largura, label="Temperatura Analítica", color="red")
    plt.bar(x + largura, data[:, 2], width=largura, label="Erro", color="green")

    plt.xlabel("Pontos")
    plt.ylabel("Valores")
    plt.title("Gráfico de Barras: Temperaturas e Erro")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(select_next_path(path, generate_name_file(files, name, extension)), dpi=300)
    plt.close()
