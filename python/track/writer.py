from pathlib import Path
from pytablewriter import MarkdownTableWriter
import contents

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

def run_writer():
    all_tables = []

    # obter todas as variáveis dentro do módulo contents
    # e se a var obtida for um dict, e tiver a chave 'copies', como esperado
    # passar essa variável pro gerador de tabelas, e depois adicionar a tabela gerada ao array final
    for name, obj in vars(contents).items():
        if isinstance(obj, dict) and 'copies' in obj:
            table = resolve_table_writing(obj)
            all_tables.append(table)

    # escrever o resultado, juntando todas as tabelas em uma só string
    with open('../../TRACK.md', 'w') as f:
        f.write(''.join(all_tables))

run_writer()