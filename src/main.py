from source_solution import (
    search_solution_problem_01,
)
from generate_file import (
    generate_name_file,
    get_local_default,
    select_next_path,
    len_file_path,
    create_excel,
    again_path,
)
from plot import (
    plot_temperature,
    plot_lines,
    plot_bar,
)


def run(DEBUG=False):
    local_path = get_local_default()
    local_save_database = select_next_path(again_path(local_path), 'data')
    local_save_plot = select_next_path(again_path(local_path), 'images')
    
    array = search_solution_problem_01()
    database = create_excel(array[1], local_save_database, generate_name_file(len_file_path(local_save_database, 0) , 'DATABASE', 'xlsx'), 'xlsx')
    
    plot_bar(array[1], local_save_plot, len_file_path(local_save_plot, 1), 'GRÁFICO-BARRA', 'png')
    plot_lines(array[1], local_save_plot, len_file_path(local_save_plot, 2), 'GRÁFICO-LINHA', 'png')
    plot_temperature(array[1], local_save_plot, len_file_path(local_save_plot, 3), 'GRÁFICO-TEMPERATURA-NUMÉRICA', 'png', 'NUMERIC')
    plot_temperature(array[1], local_save_plot, len_file_path(local_save_plot, 4), 'GRÁFICO-TEMPERATURA-ANALÍTICA', 'png', 'ANALYTIC')
    
    if DEBUG:
        print(array[0])
        print(database)

run(True)
