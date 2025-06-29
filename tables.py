"""
    utilitário pra escrever a tabela do readme mais facilmente
"""

def write_main(target_file_path, headers, rows_dictionary):
    text_line = "| "
    separator_line = "| "
    for item in headers:
        text_line += f" {item} |"
        separator_line += f"---|"

    rows_lines = ""
    for key, values in rows_dictionary.items():
        software_name = key
        software_icon = f'<img src="{ICONS_ROOT}/{values["icon_name"]}.svg" width="24"/>'

        icon_source = values.get("icon_source")
        changes = values.get("changes")

        rows_lines += f"{software_icon} {software_name} | {icon_source} | {changes}\n"
    
    condensed_info = f"{text_line} \n {separator_line} \n {rows_lines}"

    with open(target_file_path, 'w') as f:
        f.write(condensed_info)
        print(f"{target_file_path} sobreescrito")

ICONS_ROOT = "./coral/apps/scalable/"

headers = ["Software", "Icon source", "Changes"]
contents = {
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

write_main("/mnt/seagate/workspace/coding/projects/icons/coral/test.md", headers, contents)