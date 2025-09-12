from pathlib import Path

from pytablewriter import MarkdownTableWriter

#from contents_old import folder_like, default_folder_copies
from contents import *

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
    group_name = content_dict.get("group_name")
    copies = content_dict.get("copies")

    # separação de variáveis pra futura organização
    real_files = []
    symlinks = []

    # construir um row novo pra cada tupla dentro do array de cópias
    for copy in copies:
        origin_dir = copy[0] # ex: places/scalable
        icon_name = copy[1] # ex: folder-pictures.svg

        if not icon_name.endswith(".svg"):
            print(f"{icon_name} é inválido por não terminar em .svgs")
            continue

        # extrair os dados da entrada do dicionário de conteúdos
        icon_path = Path("./copycat/", origin_dir, icon_name)
        icon_image = f'<img src="{icon_path}">'
        full_path = f"`{icon_path}`"
        file_name = f"`{icon_name}`"
        norm_origin_dir = f"`{origin_dir}`"

        # adicionar verificação se o ícone é ou não um symlink
        # se ele NÃO for, ganha a checkmark verde, pra indicar que é real
        # ícones de: lucide icons
        resolved_path = Path(__file__).resolve().parent.parent.parent / "copycat" / origin_dir / icon_name
        checkmark_width = 15
        if not resolved_path.is_symlink():
            is_symlink = f'<img src="./python/track/check.svg" width={checkmark_width}>'
        else:
            is_symlink = f'<img src="./python/track/ban.svg" width={checkmark_width}>'

            # deixar os textos do row em itálico caso seja um symlink
            full_path = f"<i>{full_path}</i>"
            file_name = f"<i>{file_name}</i>"
            norm_origin_dir = f"<i>{norm_origin_dir}</i>"

        # adicionar mais um row aos arrays que serão condesados no array final
        final_row = [icon_image, is_symlink, full_path, file_name, norm_origin_dir]
        if resolved_path.is_symlink():
            symlinks.append(final_row)
        else:
            real_files.append(final_row)

    # sempre ordena os symlinks pra virem por último, apenas após todos os arquivos reais
    rows = real_files + symlinks

    # gerar a tabela markdown contendo os rows obtidos
    # e escrever ela como uma string com .dumps
    writer = MarkdownTableWriter(
        table_name=group_name,
        headers=["Icon", "Is real", "Full path", "File name", "Origin directory"],
        value_matrix=rows
    )

    string_table = writer.dumps()
    return string_table

#table_default = resolve_table_writing(folder_like)
#table_default = resolve_table_writing(default_folder_copies)

table_file_manager_blue = resolve_table_writing(file_manager_blue_group)
table_file_manager = resolve_table_writing(file_manager_group)
table_mc = resolve_table_writing(mc_group)
table_nautilus = resolve_table_writing(nautilus_group)
table_system_file_manager = resolve_table_writing(system_file_manager_group)
table_spacefm = resolve_table_writing(spacefm_group)
table_krusader = resolve_table_writing(krusader_group)
table_fma_config = resolve_table_writing(fma_config_group)

table_folder = resolve_table_writing(folder_group)
table_folder_locked = resolve_table_writing(folder_locked_group)
table_folder_favorites = resolve_table_writing(folder_favorites_group)
table_folder_download = resolve_table_writing(folder_download_group)
table_folder_image = resolve_table_writing(folder_image_group)
table_folder_remote = resolve_table_writing(folder_remote_group)
table_network_manager = resolve_table_writing(network_manager_group)
table_user_desktop = resolve_table_writing(user_desktop_group)

all_tables = [
    table_file_manager_blue,
    table_file_manager,
    table_mc,
    table_nautilus,
    table_system_file_manager,
    table_spacefm,
    table_krusader,
    table_fma_config,

    table_folder,
    table_folder_locked,
    table_folder_favorites,
    table_folder_download,
    table_folder_image,
    table_folder_remote,
    table_network_manager,
    table_user_desktop,
]

# escrever o resultado final no arquivo markdown
with open("../../TRACK.md", "w") as f:
    condensed = ""
    for table in all_tables:
        condensed += table
    f.write(condensed)
# with open("../../TRACK.md", "w") as f:
#     f.write(table_default)