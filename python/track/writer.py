from pathlib import Path
from pytablewriter import MarkdownTableWriter
from contents import *

def generate_table_rows(tuple_list: list[tuple]):
    # variáveis pra futura organização
    # assim, é possível ordenar os arquivos reais antes dos symlinks
    real_files = []
    symlinks = []

    for t in tuple_list:
        origin_dir = t[0] # ex: places/scalable
        icon_name = t[1] # ex: folder-pictures.svg

        # reconstruir o path de onde o ícone vem, incluindo a extensão do arquivo
        icon_ext = icon_name + '.svg' if not icon_name.endswith('.svg') else icon_name
        icon_path = Path('./copycat/', origin_dir, icon_ext)

        # formatar os dados da entrada do dicionário de conteúdos
        icon_image = f'<img src="{icon_path}">'
        full_path =  f'`{icon_path}`'
        file_name =  f'`{icon_name}`'
        norm_origin_dir = f'`{origin_dir}`'
        points_to = '' # é decidido por código depois

        # adicionar verificação se o ícone é ou não um symlink
        # se ele NÃO for, ganha a checkmark verde, pra indicar que é real
        # ícones de: lucide icons
        resolved_path = Path(__file__).resolve().parent.parent.parent / 'copycat' / origin_dir / icon_ext
        checkmark_width = 15
        if not resolved_path.is_symlink():
            is_symlink = f'<img src="./python/track/check.svg" width={checkmark_width}>'
        else:
            is_symlink = f'<img src="./python/track/ban.svg" width={checkmark_width}>'

            # deixar os textos do row em itálico caso seja um symlink
            full_path = f'<i>{full_path}</i>'
            file_name = f'<i>{file_name}</i>'
            norm_origin_dir = f'<i>{norm_origin_dir}</i>'
            points_to = f'<i>`{resolved_path.readlink()}`</i>' # ler pra onde o symlink do arquivo aponta

        # adicionar mais um row aos arrays que serão condesados no array final
        final_row = [icon_image, is_symlink, full_path, file_name, points_to or '', norm_origin_dir]
        if resolved_path.is_symlink():
            symlinks.append(final_row)
        else:
            real_files.append(final_row)

    # sempre ordena os symlinks pra virem por último, apenas após todos os arquivos reais
    rows = real_files + symlinks
    return rows

def resolve_table_writing(content_dict: dict):
    """
    escreve uma tabela markdown indicando:
    - o ícone
    - se o ícone é um symlink
    - paths etc.

    :param content_dict:
        dicionário contendo o nome do grupo
        e um array de tuplas com o path relativo do diretório de origem e o nome do arquivo
    """

    # obter as informações no dicionário
    group_name = content_dict.get('group_name')
    copies = content_dict.get('copies')

    # construir um row novo pra cada tupla dentro do array de cópias
    rows = generate_table_rows(copies)

    # gerar a tabela markdown contendo os rows obtidos
    # e escrever ela como uma string com .dumps
    writer = MarkdownTableWriter(
        table_name=group_name,
        headers=['Icon', 'Is real', 'Full path', 'File name', 'Points to', 'Origin directory'],
        value_matrix=rows
    )

    string_table = writer.dumps()
    return string_table

# escrever todas as tabelas e inseri-las em um array
# esse array vai ser condensado em uma só string pra ser escrito no arquivo final
table_plain = resolve_table_writing(plain_folder_group)
table_variations = resolve_table_writing(variations_group)
table_derivations = resolve_table_writing(derivations_group)

table_locked = resolve_table_writing(folder_locked_group)
table_home = resolve_table_writing(folder_home_group)
table_favorites = resolve_table_writing(folder_favorites_group)
table_download = resolve_table_writing(folder_download_group)
table_pictures = resolve_table_writing(folder_pictures_group)
table_remote = resolve_table_writing(folder_remote_group)
table_network = resolve_table_writing(network_manager_group)
table_desktop = resolve_table_writing(user_desktop_group)

table_cloud = resolve_table_writing(folder_cloud_group)
table_uniques = resolve_table_writing(folder_uniques_group)
table_documents = resolve_table_writing(folder_documents_group)
table_image_people = resolve_table_writing(folder_image_people_group)
table_megasync = resolve_table_writing(folder_megasync_group)
table_publicshare = resolve_table_writing(folder_publicshare_group)
table_saved_search = resolve_table_writing(folder_saved_search_group)
table_text = resolve_table_writing(folder_text_group)
table_unlocked = resolve_table_writing(folder_unlocked_group)
table_visiting = resolve_table_writing(folder_visiting_group)
table_open = resolve_table_writing(folder_open_group)
table_drive = resolve_table_writing(folder_drive_group)
table_image = resolve_table_writing(folder_image_group)
table_recent = resolve_table_writing(folder_recent_group)
table_templates = resolve_table_writing(folder_templates_group)

all_tables = [
    table_plain,
    table_variations,
    table_derivations,

    table_locked,
    table_home,
    table_favorites,
    table_download,
    table_pictures,
    table_remote,
    table_network,
    table_desktop,

    table_recent,
    table_templates,
    table_cloud,
    table_drive,
    table_image,
    table_open,
    table_uniques,
    table_documents,
    table_image_people,
    table_megasync,
    table_publicshare,
    table_saved_search,
    table_text,
    table_unlocked,
    table_visiting,
]

# escrever o resultado final no arquivo markdown
with open('../../TRACK.md', 'w') as f:
    condensed = ''
    for table in all_tables:
        condensed += table
    f.write(condensed)