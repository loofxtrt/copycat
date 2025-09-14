from pathlib import Path
from xml.dom import minidom
from yattag import Doc
from contents import *

# NÃO DÁ PRA USAR MARKDOWN PORQUE PRA INCLUIR A TABELA DENTRO DE UMA TAG DETAILS
# ELA PRECISA SER HTML OBRIGATORIAMENTE
#
# from pytablewriter import MarkdownTableWriter
#
# def generate_table_rows(contents_dict_list: list[dict], target_dir: Path):
#     formatted_rows = []
#
#     for d in contents_dict_list:
#         # obter os valores do dicionário passado
#         icon_display_name = d.get('display_name')
#         icon_source = d.get('icon_source')
#         icon_changes = d.get('icon_changes')
#
#         # montar o caminho completo do ícone pra visualização
#         icon_name = d.get('icon_name') + '.svg'
#         i_path = target_dir / icon_name
#         i_image = f'<img src="{i_path}" width="24">' # html pra poder controlar o tamanho
#
#         formatted_rows.append([i_image, icon_display_name, icon_source, icon_changes])
#
#     return formatted_rows
#
# def resolve_table_writing(contents_dict_list: list[dict], target_dir: Path):
#     # gerar os rows pra cada dicionário da lista
#     rows = generate_table_rows(contents_dict_list, target_dir)
#
#     # gerar a tabela e guardar ela numa string
#     writer = MarkdownTableWriter(
#         headers=['Icon', 'Icon name', 'Source', 'Changes'],
#         value_matrix=rows
#     )
#
#     string_table = writer.dumps()
#     return string_table

def resolve_table_writing(rows: list[dict], target_dir: Path, summary_text: str):
    doc, tag, text = Doc().tagtext()

    # criar o campo expansível
    with tag('details'):
        with tag('summary'):
            text(f'{summary_text} (click to expand)')

        # criar a tabela com borda, largura etc.
        with tag('table', border='1', width='100%'):
            # cabeçalho
            with tag('tr'):
                for header in ['Icon', 'Icon name', 'Source', 'Changes']:
                    with tag('th'): text(header)

            # criar um table row pra cada entrada do array de dicts
            for row in rows:
                with tag('tr'):
                    # obter os valores primários
                    display_name = row.get('display_name')
                    icon_source  = row.get('icon_source')
                    icon_changes = row.get('icon_changes', '')

                    # montar o caminho completo do ícone pra visualização
                    icon_name = row.get('icon_name') + '.svg'
                    i_path = str(target_dir / icon_name)

                    # células da imagem e nome do ícone
                    with tag('td'):
                        doc.stag('img', src=i_path, width='24')
                    with tag('td'):
                        text(display_name)

                    # células da fonte e mudanças no ícone
                    # doc.asis insere html dentro do html sem precisar escapar
                    with tag('td'):
                        doc.asis(icon_source)
                    with tag('td'):
                        doc.asis(icon_changes)

    # renderizar a tabela e retornar
    raw_html = doc.getvalue()
    pretty_html = minidom.parseString(raw_html).toprettyxml()

    return pretty_html

def run_writer():
    # criar as tabelas
    pack_root = Path('./copycat')
    scal_dir_apps = pack_root / 'apps' / 'scalable'
    scal_dir_places = pack_root / 'places' / 'scalable'
    scal_dir_mimetypes = pack_root / 'mimetypes' / 'scalable'

    apps_table = resolve_table_writing(APPS_ROWS, scal_dir_apps, 'Apps')
    places_table = resolve_table_writing(PLACES_ROWS, scal_dir_places, 'Places')
    mimetypes_table = resolve_table_writing(MIMETYPES_ROWS, scal_dir_mimetypes, 'Mimetypes')
    others_table = resolve_table_writing(OTHERS_ROWS, scal_dir_apps, 'Others')

    # condensar as informações junto com as tabelas em uma só string
    # e depois escrever o arquivo markdown final
    condensed = FIRST_CHUNK + apps_table + places_table + mimetypes_table + others_table + LAST_CHUNK

    with open('README.md', 'w') as f:
        f.write(condensed)

run_writer()