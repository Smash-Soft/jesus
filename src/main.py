from source_solution import (
    search_solution_problem_01,  # Importa a função que resolve o problema e retorna os resultados
)
from generate_file import (
    generate_name_file,  # Gera um nome de arquivo único
    get_local_default,  # Obtém o diretório padrão para salvar arquivos
    select_next_path,  # Escolhe o próximo caminho disponível para salvar arquivos
    len_file_path,  # Obtém o número de arquivos existentes em um diretório
    create_excel,  # Cria e salva uma planilha Excel com os dados
    again_path,  # Reajusta o caminho para garantir que ele esteja correto
)
from plot import (
    plot_temperature,  # Função para gerar gráficos de temperatura (mapa de calor)
    plot_lines,  # Função para gerar gráficos de linhas comparando valores
    plot_bar,  # Função para gerar gráficos de barras comparando valores
)

def run(DEBUG=bool(False)):
    """
    Executa o processo completo de resolução do problema, armazenamento dos dados e geração de gráficos.
    
    Parâmetros:
        DEBUG (bool): Se True, imprime informações adicionais para depuração.
    """
    
    # Obtém o diretório padrão onde os arquivos serão salvos
    local_path = get_local_default()
    
    # Define os diretórios para salvar os arquivos de dados e imagens
    local_save_database = select_next_path(again_path(local_path), 'data')  # Caminho para salvar os dados
    local_save_plot = select_next_path(again_path(local_path), 'images')  # Caminho para salvar os gráficos
    
    # Chama a função que resolve o problema e retorna os dados calculados
    array = search_solution_problem_01()
    
    # Cria e salva uma planilha Excel com os dados numéricos gerados
    database = create_excel(
        array[1],  # Dados que serão armazenados no arquivo Excel
        local_save_database,  # Diretório onde o arquivo será salvo
        generate_name_file(len_file_path(local_save_database, 0), 'DATABASE', 'xlsx'),  # Nome do arquivo gerado
        'xlsx'  # Extensão do arquivo
    )
    
    # Gera gráficos para visualizar os dados gerados
    plot_bar(  # Gráfico de barras
        array[1],  # Array com os dados
        local_save_plot,  # Local de salvamento
        len_file_path(  # Retorna o número de arquivos do modo passado
            local_save_plot,
            1
        ), 
        'GRÁFICO-BARRA',  # Nome do arquivo a ser salvo
        'png'  # Extensão do arquivo a ser salvo
    )

    plot_lines(  # Gráfico de linhas
        array[1],  # Array com os dados
        local_save_plot,  # Local de salvamento
        len_file_path(  # Retorna o número de arquivos do modo passado
            local_save_plot,
            2
        ),
        'GRÁFICO-LINHA',  # Nome do arquivo a ser salvo
        'png'  # Extensão do arquivo a ser salvo
    )

    plot_temperature(  # Mapa de calor da temperatura numérica
        array[1],  # Array com os dados
        local_save_plot,  # Local de salvamento
        len_file_path(  # Retorna o número de arquivos do modo passado
            local_save_plot,
            3
        ),
        'GRÁFICO-TEMPERATURA-NUMÉRICA',  # Nome do arquivo a ser salvo
        'png',  # Extensão do arquivo a ser salvo
        'NUMERIC'  # Modo do gráfico: numérico
    )

    plot_temperature(  # Mapa de calor da temperatura analítica
        array[1],  # Array com os dados
        local_save_plot,  # Local de salvamento
        len_file_path(  # Retorna o número de arquivos do modo passado
            local_save_plot,
            4
        ),
        'GRÁFICO-TEMPERATURA-ANALÍTICA',  # Nome do arquivo a ser salvo
        'png',  # Extensão do arquivo a ser salvo
        'ANALYTIC'  # Modo do gráfico: analítico
    )
    
    # Se o modo de depuração estiver ativado, imprime as informações na tela
    if DEBUG:
        print(array[0])  # Exibe no prompt uma tabela formatada com os dados
        print(database)  # Exibe se o database foi gerado com sucesso ou ocorreu algum erro

# Chama a função principal com o modo de depuração passada como padrão como falsa
run(True)
