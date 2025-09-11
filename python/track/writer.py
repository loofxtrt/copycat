from xml.dom import minidom
from pathlib import Path

from yattag import Doc

import contents

def create_table(rows: list[dict]):
    doc, tag, text = Doc().tagtext()

    # criar a tabela com borda, largura etc.
    with tag("table", border="1", width="100%"):
        # cabeçalho
        with tag("tr"):
            for header in ["Icon", "Source", "Changes"]:
                with tag("th"): text(header)
        
        # criar um table row pra cada entrada do array de dicts
        for row in rows:
            with tag("tr"):
                # escrever cada valor do dicionário como um table data
                icon_name = row["icon_name"]
                if not icon_name.endswith(".svg"):
                    icon_name += ".svg"

                origin_dir = row["origin_dir"]

                full_path = Path(origin_dir, icon_name)

                with tag("td"):
                    # imagem do ícone
                    doc.stag("img", src=f"{origin_dir}/{icon_name}.svg", width="24")
                with tag("td"):
                    text(f" {icon_name}")
                with tag("td"):
                    text(origin_dir)
                with tag("td"):
                    text(full_path)

    # renderizar a tabela e retornar
    raw_html = doc.getvalue()
    pretty_html = minidom.parseString(raw_html).toprettyxml()
    
    return pretty_html