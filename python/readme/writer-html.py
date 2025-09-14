from xml.dom import minidom

from yattag import Doc

import contents

def create_table(rows: list[dict], root_dir: str, summary_text: str):
    doc, tag, text = Doc().tagtext()

    # remover a / caso ela exista no final do path
    if root_dir.endswith("/"):
        root_dir = root_dir[:-1]

    # criar o campo expansível
    with tag("details"):
        with tag("summary"): text(f"{summary_text} (click to expand)")
    
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
                    display_name = row["display_name"]
                    icon_name = row["icon_name"]
                    icon_source = row["icon_source"]
                    icon_changes = row.get("icon_changes", "")

                    with tag("td"):
                        # inserir uma img e texto comum
                        doc.stag("img", src=f"{root_dir}/{icon_name}.svg", width="24")
                        text(f" {display_name}")
                    with tag("td"):
                        # inserir html dentro do html sem escapar
                        doc.asis(icon_source)
                    with tag("td"):
                        text(icon_changes)

    # renderizar a tabela e retornar
    raw_html = doc.getvalue()
    pretty_html = minidom.parseString(raw_html).toprettyxml()
    
    return pretty_html

def main():
    first_chunk = """
<img src="./copycat_banner.svg" width="256" alt="Copycat" style="display: block;">
An icon theme forked from Kora, replacing/modifying a few icons while trying to make them more accurate to the original software logo's colors and shapes  
  
Small inconsistencies in the gradients of folder icons were also normalized to be exactly the same tone  
  
[![Static Badge](https://img.shields.io/badge/tar.gz-download_icon_pack-yellow)](https://github.com/loofxtrt/copycat/releases/latest)  
## Conventions and rules  
- the default (blue) folders should follow the standard:
    - #0083d5 solid color for the background
    - #1075f6 -> #12c5ff gradient for the folder itself
    - #126c98ff -> #0b4f94ff for the symbol on top of the folder (if present)
  
## Credits
Icons from different packs are included in this repo, **all licensed under the GPL3 license**  
Those packs includes:  
[Kora](https://store.kde.org/p/1256209), [Breeze](https://github.com/KDE/breeze-icons), [Marwaita](https://www.gnome-look.org/p/1239855), [MoreWaita](https://www.gnome-look.org/p/2276064), [PlasmaX](https://www.gnome-look.org/p/1367155), [Infinity](https://www.gnome-look.org/p/2112373), [Reversal](https://www.gnome-look.org/p/1340791), [Flat Remix](https://store.kde.org/p/1012430), [FairyWren](https://www.gnome-look.org/p/1684521), [Yosa Max](https://www.gnome-look.org/p/1196255/), [Papirus](https://www.gnome-look.org/p/1166289/)  
  
## Major differences  
"""

    apps_table = create_table(contents.APPS_ROWS, "./copycat/apps/scalable", "Software")
    places_table = create_table(contents.PLACES_ROWS, "./copycat/places/scalable", "Places")
    mimetypes_table = create_table(contents.MIMETYPES_ROWS, "./copycat/mimetypes/scalable", "Mimetypes")
    others_table = create_table(contents.OTHERS_ROWS, "./copycat/apps/scalable", "Others")

    last_chunk = """
## License
[GPL3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
"""

    condensed = first_chunk + apps_table + places_table + mimetypes_table + others_table + last_chunk

    with open("README.md", "w") as f:
        f.write(condensed)

main()