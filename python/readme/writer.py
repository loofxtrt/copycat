from pathlib import Path
from pytablewriter import MarkdownTableWriter
from contents import APPS_ROWS



def generate_table_rows(content_dict_list: list[dict], target_dir: Path):
    formatted_rows = []

    for d in content_dict_list:
        # obter os valores do dicionário passado
        icon_display_name = d.get('display_name')
        icon_source = d.get('icon_source')
        icon_changes = d.get('icon_changes')

        # montar o caminho completo do ícone pra visualização
        icon_name = d.get('icon_name') + '.svg'
        i_path = target_dir / icon_name
        i_image = f'<img src="{i_path}" width="24">' # html pra poder controlar o tamanho

        formatted_rows.append([i_image, icon_display_name, icon_source, icon_changes])

    return formatted_rows

def write_table():
    pack_root = Path('../../copycat')
    rows = generate_table_rows(
        content_dict_list=APPS_ROWS,
        target_dir=pack_root / 'apps' / 'scalable'
    )

    writer = MarkdownTableWriter(
        headers=['Icon', 'Icon name', 'Source', 'Changes'],
        value_matrix=rows
    )

    string_final = writer.dumps()
    with open('TEST.md', 'w') as f:
        f.write(string_final)

write_table()