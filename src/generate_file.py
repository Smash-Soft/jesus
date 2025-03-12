from openpyxl.styles import Font, PatternFill
from openpyxl.styles import Border, Side
from openpyxl.styles import Alignment
from openpyxl import load_workbook
from datetime import datetime
from openpyxl import Workbook
from pathlib import Path
import unicodedata
import tempfile
import os


def len_file_path(path, mode=0):
    counter = 0
    if mode == 0:
        for file in os.listdir(path):
            if 'DATABASE_' in file:
                counter += 1
    elif mode == 1:
        for file in os.listdir(path):
            if remover_utf8('GRÁFICO-BARRA_') in file:
                counter += 1
    elif mode == 2:
        for file in os.listdir(path):
            if remover_utf8('GRÁFICO-LINHA_') in file:
                counter += 1
    elif mode == 3:
        for file in os.listdir(path):
            if remover_utf8('GRÁFICO-TEMPERATURA-NUMÉRICA_') in file:
                counter += 1
    elif mode == 4:
        for file in os.listdir(path):
            if remover_utf8('GRÁFICO-TEMPERATURA-ANALÍTICA_') in file:
                counter += 1
                
    return counter

def generate_name_file(files=int, name=str, extension=str):
    extension = extension.replace('.', '')
    if files + 1 < 10:
        files = f'00000{files + 1}'
    elif files + 1 < 100:
        files = f'0000{files + 1}'
    elif files + 1 < 1000:
        files = f'000{files + 1}'
    elif files + 1 < 10000:
        files = f'00{files + 1}'
    elif files + 1 < 100000:
        files = f'0{files + 1}'
    else:
        files = f'{files + 1}'
    return f'{name}_{files}.{extension}'

def get_local_default():
    local_default = Path(__file__).parent.resolve()
    return local_default

def again_path(path):
    return os.path.dirname(path)

def select_next_path(path, next):
    return os.path.join(path, next)

def remover_utf8(texto):
    normalized = unicodedata.normalize('NFD', texto)
    new_text = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    return new_text

def settings_font():
    font_title = Font(color="ffffff", size=14, bold=True)
    fill_title = PatternFill(start_color="cc0000", end_color="cc0000", fill_type="solid")
    font_display = Font(color="000000", size=12, bold=True)
    fill_display = PatternFill(start_color="ffea00", end_color="ffea00", fill_type="solid")
    
    border_all_min = Border(
        left=Side(border_style="thin"),
        right=Side(border_style="thin"),
        top=Side(border_style="thin"),
        bottom=Side(border_style="thin"),
    )
    border_left_bottom = Border(
        left=Side(border_style="thick"),
        right=Side(border_style="thin"),
        top=Side(border_style="thin"),
        bottom=Side(border_style="thick"),
    )
    border_right_bottom = Border(
        left=Side(border_style="thin"),
        right=Side(border_style="thick"),
        top=Side(border_style="thin"),
        bottom=Side(border_style="thick"),
    )
    border_bottom = Border(
        left=Side(border_style="thin"),
        right=Side(border_style="thin"),
        top=Side(border_style="thin"),
        bottom=Side(border_style="thick"),
    )

    return [
        font_title,                # 00
        fill_title,                # 01
        font_display,              # 02
        fill_display,              # 03
       
        border_all_min,            # 04
        border_left_bottom,        # 05
        border_right_bottom,       # 06
        border_bottom,             # 07
        
    ]

def settings_border():
    border_1 = Border(
        top=Side(border_style='thin', color='000000'),
        left=Side(border_style='thin', color='000000'),
        right=Side(border_style='thin', color='000000')
    )
    border_2 = Border(
        bottom=Side(border_style='thin', color='000000'),
        left=Side(border_style='thin', color='000000'),
        right=Side(border_style='thin', color='000000')
    )
    border_3 = Border(left=Side(border_style='thin', color='000000'))
    border_4 = Border(right=Side(border_style='thin', color='000000'))
    return [
        border_1,
        border_2,
        border_3,
        border_4,
    ]

def settings_align():
    align_1 = Alignment(horizontal="center", vertical="center")
    align_2 = Alignment(horizontal="left", vertical="center")
    return [
        align_1,
        align_2,
    ]

def settings_header(header_1, header_2, date):
    header = [
            f"{header_1} - {date}".upper(),
            f"{header_2}".upper(),
    ]
    return header

def create_excel(array=list, path=str, name=str, extension=str):
    try:
        wb = Workbook()
        ws = wb.active

        ws.merge_cells("A1:D1")
        ws.merge_cells("A2:D2")
        
        date = datetime.now()
        date = f"{date.day}/{date.month}"
        
        header = settings_header('TRANSFERÊNCIA DE CALOR', 'JESUS', date)
        border_settings = settings_border()
        align_settings = settings_align()
        font_settings = settings_font()
        
        ws["A1"] = header[0]
        ws["A1"].alignment = align_settings[0]
        ws["A1"].font = font_settings[0]
        ws["A1"].fill = font_settings[1]
        ws["A1"].border = border_settings[0]

        ws["A2"] = header[1]
        ws["A2"].alignment = align_settings[0]
        ws["A2"].font = font_settings[0]
        ws["A2"].fill = font_settings[1]
        ws["A2"].border = border_settings[1]

        ws["A3"] = "PONTO Nº"
        ws["A3"].alignment = align_settings[0]
        ws["A3"].border = border_settings[2]

        ws["B3"] = "SOLUÇÃO NUMÉRICA"
        ws["B3"].alignment = align_settings[0]
        ws["B3"].border = font_settings[4]

        ws["C3"] = "SOLUÇÃO ANALÍTICA"
        ws["C3"].alignment = align_settings[0]
        ws["C3"].border = font_settings[4]

        ws["D3"] = "ERRO"
        ws["D3"].alignment = align_settings[0]
        ws["D3"].border = font_settings[4]

        for col in range(1, 5):
            ws.cell(row=3, column=col).font = font_settings[2]
            ws.cell(row=3, column=col).fill = font_settings[3]
            
        ws.column_dimensions['A'].width = 20
        ws.column_dimensions['B'].width = 30
        ws.column_dimensions['C'].width = 30
        ws.column_dimensions['D'].width = 30
        
        counter = 0
        for c, data in enumerate(array):
            counter += 1
            calc_numeric = '{:0.20f}'.format(data[0])
            calc_analytic = '{:0.20f}'.format(data[1])
            error = '{:0.20f}'.format(data[2])
            
            ws.cell(row=counter + 3, column=1).value = counter
            ws.cell(row=counter + 3, column=1).alignment = align_settings[0]
            ws.cell(row=counter + 3, column=1).border = font_settings[4]

            ws.cell(row=counter + 3, column=2).value = calc_numeric
            ws.cell(row=counter + 3, column=2).alignment = align_settings[0]
            ws.cell(row=counter + 3, column=2).border = font_settings[4]

            ws.cell(row=counter + 3, column=3).value = calc_analytic
            ws.cell(row=counter + 3, column=3).alignment = align_settings[1]
            ws.cell(row=counter + 3, column=3).border = font_settings[4]

            ws.cell(row=counter + 3, column=4).value = error
            ws.cell(row=counter + 3, column=4).alignment = align_settings[0]
            ws.cell(row=counter + 3, column=4).border = font_settings[4]

        last_column = 5
        for col in range(1, last_column):
            ws.cell(row=len(array) + 3, column=col).border = font_settings[7]
            
        
        extension = extension.replace('.', '')
        extension = f'.{extension}'
        
        name_file = name.replace(extension, '')
        name_file = remover_utf8(name_file).upper()
        name_file = f'{name_file}{extension}'
        
        local_file = select_next_path(path, name_file)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
            wb.save(temp_file.name)  

        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as final_temp_file:
            workbook = load_workbook(temp_file.name)
            sheet = workbook.active

            sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
            sheet.page_setup.orientation = sheet.ORIENTATION_LANDSCAPE

            workbook.save(local_file)
        
        return 'Database salvo com sucesso!!!'
    except Exception as e:
        return 'Ocorreu um erro durante o salvamento...\n\n{e}'

  
