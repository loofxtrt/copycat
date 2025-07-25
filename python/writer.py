from pathlib import Path

from contents import software_headers, software_rows, places_headers, places_rows, first_chunk, last_chunk

"""
    utilitário pra escrever a tabela do readme mais facilmente
"""

def set_table(header_list, row_dictionary, parent_dir):
    # gerar as linhas dos cabeçalhos e do separador
    headers_line = "| "
    separator_line = "| "
    for item in header_list:
        headers_line += f" {item} |"
        separator_line += f"---|"

    # gerar os conteúdos da tabela
    rows_lines = ""
    for key, values in row_dictionary.items():
        # obter o nome e ícone do software
        software_name = key
        software_icon = f'<img src="{parent_dir}/{values["icon_name"]}.svg" width="24"/>'

        # obter os valores ou deixa-los vazios caso sejam none
        icon_source = values.get("icon_source") or ""
        changes = values.get("changes") or ""

        # formatar a linha
        rows_lines += f"| {software_icon} {software_name} | {icon_source} | {changes}|\n"
    
    # condensar as informações em uma única string
    condensed_info = f"{headers_line} \n {separator_line} \n {rows_lines}"
    return condensed_info

def write_all(target_file_path, contents: list):
    # agrupar todos os conteúdos em um bloco só
    condensed_info = ""
    for item in contents:
        condensed_info += f"{item}\n"

    # sobreescrever o arquivo indicado
    with open(target_file_path, 'w') as f:
        f.write(condensed_info)
        print(f"{target_file_path} sobreescrito")

ROOT = Path(__file__).parent.parent # obtém o parent do parent desse script
readme = ROOT / "README.md"

software_table = set_table(
    header_list=software_headers,
    row_dictionary=software_rows,
    parent_dir="./copycat/apps/scalable/"
)

places_table = set_table(
    header_list=places_headers,
    row_dictionary=places_rows,
    parent_dir="./copycat/places/scalable/"
)

write_all(
    target_file_path=readme,
    contents=[first_chunk, software_table, places_table, last_chunk]
)