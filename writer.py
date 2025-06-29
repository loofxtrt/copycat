"""
    utilitário pra escrever a tabela do readme mais facilmente
"""

def set_table(headers, rows_dictionary):
    # gerar as linhas dos cabeçalhos e do separador
    text_line = "| "
    separator_line = "| "
    for item in headers:
        text_line += f" {item} |"
        separator_line += f"---|"

    # gerar os conteúdos da tabela
    rows_lines = ""
    for key, values in rows_dictionary.items():
        # obter o nome e ícone do software
        software_name = key
        software_icon = f'<img src="{ICONS_ROOT}/{values["icon_name"]}.svg" width="24"/>'

        # obter os valores ou deixa-los vazios caso sejam none
        icon_source = values.get("icon_source") or ""
        changes = values.get("changes") or ""

        # formatar a linha
        rows_lines += f"| {software_icon} {software_name} | {icon_source} | {changes}|\n"
    
    # condensar as informações em uma única string
    condensed_info = f"{text_line} \n {separator_line} \n {rows_lines}"
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

ICONS_ROOT = "./coral/apps/scalable/"

headers = ["Software", "Icon source", "Changes"]
rows = {
    "Blender": {
        "icon_name": "blender",
        "icon_source": "original Blender SVG",
        "changes": "added a subtle gradient"
    },
    "Godot": {
        "icon_name": "godot",
        "icon_source": "from PlasmaX",
        "changes": "edited SVG to make the tones match"
    },
    "Inkscape": {
        "icon_name": "inkscape",
        "icon_source": "from PlasmaX",
        "changes": "edited SVG to make it darker"
    },
    "Krita": {
        "icon_name": "krita",
        "icon_source": "from Marwaita"
    },
    "Spotify": {
        "icon_name": "spotify-client",
        "icon_source": "from Marwaita"
    },
    "Discord": {
        "icon_name": "discord",
        "icon_source": "from Kora",
        "changes": "edited SVG to make the color closer to the official Discord burple"
    },
    "Discord Canary": {
        "icon_name": "discord-canary",
        "icon_source": "from Kora",
        "changes": "background shape changed to be like regular Discord"
    },
    "Discord Development": {
        "icon_name": "discord-development",
        "icon_source": "from Kora",
        "changes": "modified to match size and style of other Discord variants"
    },
    "GIMP": {
        "icon_name": "gimp",
        "icon_source": "from KDE's Breeze Dark",
        "changes": "edited SVG to make it bigger"
    },
    "Steam": {
        "icon_name": "steam",
        "icon_source": "from Marwaita"
    },
    "OBS": {
        "icon_name": "obs",
        "icon_source": "from Kora",
        "changes": "edited SVG to make it darker"
    },
    "Libresprite": {
        "icon_name": "libresprite",
        "icon_source": "made from scratch"
    },
    "Aseprite": {
        "icon_name": "aseprite",
        "icon_source": "made from scratch"
    },
    "PureRef": {
        "icon_name": "pureref",
        "icon_source": "from Kora",
        "changes": "edited SVG to make it darker"
    },
    "DB Browser for SQLite": {
        "icon_name": "sqlitebrowser",
        "icon_source": "made from scratch"
    },
    "Audacity": {
        "icon_name": "audacity",
        "icon_source": "from Kora",
        "changes": "edited SVG to change the soundwaves and colors"
    },
    "VSCodium": {
        "icon_name": "vscodium",
        "icon_source": "from VSCodium's repository"
    }
}

table = set_table(headers, rows)
first_chunk = """
# Coral
An icon theme forked from Kora, replacing/modifying a few icons

## Differences
*Icons from different packs are included in this repo, all licensed under the GPL3 license*  
Those packs includes:  
**Marwaita**: https://www.gnome-look.org/p/1239855  
**PlasmaX**: https://www.gnome-look.org/p/1367155  
**Infinity**: https://www.gnome-look.org/p/2112373  

### Major changes
"""
last_chunk = """
### Other changes
- <img src="./coral/apps/scalable/computersettings.svg" width="24"/> Settings-related icons have also been replaced by Infinity's system settings SVG
- <img src="./coral/apps/scalable/endeavouros.svg" width="24"/> EndeavourOS (original Endeavour SVG)
- <img src="./coral/apps/scalable/computer-log-out.svg" width="24"/> Symbolic icons have been modified/replaced

### Manual changes
Some specific app icons have to be changed manually to match the theme. Those includes:
- <img src="./manual/roblox.svg" width="24"/> Roblox Player
- <img src="./manual/roblox-studio.svg" width="24"/> Roblox Studio
- <img src="./manual/sober.svg" width="24"/> Sober
- <img src="./manual/vinegar.svg" width="24"/> Vinegar  

*All Roblox-related icons are based off the original Sober and Vinegar SVGs*

## License
[GPL3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
"""

write_all(
    target_file_path="/mnt/seagate/workspace/coding/projects/icons/coral/test.md",
    contents=[first_chunk, table, last_chunk]
)