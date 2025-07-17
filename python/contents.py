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
        "icon_source": "from Marwaita",
        "changes": "added a subtle gradient"
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
        "icon_source": "from Reversal Black",
        "changes": "changed colors and shapes"
    },
    "VSCodium": {
        "icon_name": "vscodium",
        "icon_source": "from VSCodium's repository"
    }
}

first_chunk = """
# Coral
An icon theme forked from Kora, replacing/modifying a few icons

## Differences
Icons from different packs are included in this repo, **all licensed under the GPL3 license**  
Those packs includes:  
[Marwaita](https://www.gnome-look.org/p/1239855)  
[PlasmaX](https://www.gnome-look.org/p/1367155)  
[Infinity](https://www.gnome-look.org/p/2112373)  
[Reversal](https://www.gnome-look.org/p/1340791)

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

All Roblox-related icons are based off the original Sober and Vinegar SVGs

## License
[GPL3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
"""