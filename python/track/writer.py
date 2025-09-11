from pathlib import Path

from pytablewriter import MarkdownTableWriter

from contents import default_apps, default_places

def resolve_table_writing(content_dict: dict):
    group_name = content_dict.get("group_name")
    origin_dir = content_dict.get("origin_dir")
    icon_names = content_dict.get("icon_names")

    rows = []
    for i_name in icon_names:
        if not i_name.endswith(".svg"):
            print(f"{i_name} é inválido por não terminar em .svgs")
            continue

        # extrair os dados da entrada do dicionário de conteúdos
        i_path = Path("./copycat/", origin_dir, i_name)
        icon = f"![icon]({i_path})"
        full_path = f"`{i_path}`"
        file_name = f"`{i_name}`"
        norm_origin_dir = f"`{origin_dir}`"

        # adicionar verificação se o ícone é ou não um symlink
        # se ele NÃO for, ganha a checkmark verde, pra indicar que é real
        # ícones de: lucide icons
        resolved_path = Path(__file__).resolve().parent.parent.parent / "copycat" / origin_dir / i_name
        checkmark_width = 15
        if not resolved_path.is_symlink():
            is_symlink = f'<img src="./python/track/check.svg" width={checkmark_width}>'
        else:
            is_symlink = f'<img src="./python/track/ban.svg" width={checkmark_width}>'

            # deixar os textos do row em itálico caso seja um symlink
            full_path = f"<i>{full_path}</i>"
            file_name = f"<i>{file_name}</i>"
            norm_origin_dir = f"<i>{norm_origin_dir}</i>"

        # adicionar +1 row ao array final
        rows.append(
            [icon, is_symlink, full_path, file_name, norm_origin_dir]
        )

    # gerar a tabela markdown contendo os rows obtidos
    # e escrever ela como uma string com .dumps
    writer = MarkdownTableWriter(
        table_name=group_name,
        headers=["Icon", "Is real", "Full path", "File name", "Origin directory"],
        value_matrix=rows
    )

    string_table = writer.dumps()
    return string_table

table_default_apps = resolve_table_writing(default_apps)
table_default_places = resolve_table_writing(default_places)

condensed = table_default_apps + table_default_places

# escrever o resultado final no arquivo markdown
with open("../../TRACK.md", "w") as f:
    f.write(condensed)