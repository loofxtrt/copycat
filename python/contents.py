software_headers = ["Software", "Icon source", "Changes"]
software_rows = {
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
    },
    "AppImageLauncher": {
        "icon_name": "AppImageLauncher",
        "icon_source": "Flat Remix",
        "changes": "modified colors and shapes"
    },
    "Android Studio": {
        "icon_name": "android-studio",
        "icon_source": "from FairyWren",
        "changes": "adjusted colors"
    },
    "Android Studio Canary": {
        "icon_name": "android-studio-canary",
        "icon_source": "from FairyWren",
        "changes": "adjusted colors"
    },
    "btop++": {
        "icon_name": "btop",
        "icon_source": "made from scratch"
    }
}

places_headers = ["Places", "Icon source", "Changes"]
places_rows = {
    #"Home": {
    #    "icon_name": "user-home",
    #    "icon_source": "from Kora",
    #    "changes": "added an additional gradient"
    #},
    "Desktop": {
        "icon_name": "user-desktop",
        "icon_source": "from Kora",
        "changes": "added a taskbar and icons"
    },
    "Documents": {
        "icon_name": "folder-documents",
        "icon_source": "from Kora",
        "changes": "added Kora's clip icon to it"
    },
    "Downloads": {
        "icon_name": "folder-download",
        "icon_source": "from Kora",
        "changes": "modified the arrow"
    },
    "Music": {
        "icon_name": "folder-music",
        "icon_source": "from Kora",
        "changes": "changed colors"
    },
    "Music (open)": {
        "icon_name": "folder-music-open",
        "icon_source": "from Kora",
        "changes": "changed colors"
    },
    "Pictures": {
        "icon_name": "folder-pictures",
        "icon_source": "from Kora",
        "changes": "changed colors"
    },
    "Pictures (open)": {
        "icon_name": "folder-pictures-open",
        "icon_source": "from Kora",
        "changes": "changed colors"
    },
    "Videos": {
        "icon_name": "folder-videos",
        "icon_source": "from Kora",
        "changes": "changed icon to a play button and added details"
    }
}

first_chunk = """
# Copycat
An icon theme forked from Kora, replacing/modifying a few icons

## Differences
Icons from different packs are included in this repo, **all licensed under the GPL3 license**  
Those packs includes:  
[Marwaita](https://www.gnome-look.org/p/1239855)  
[PlasmaX](https://www.gnome-look.org/p/1367155)  
[Infinity](https://www.gnome-look.org/p/2112373)  
[Reversal](https://www.gnome-look.org/p/1340791)  
[Flat Remix](https://store.kde.org/p/1012430)  
[FairyWren](https://www.gnome-look.org/p/1684521)  

### Major changes
"""

last_chunk = """
### Other changes
- <img src="./copycat/apps/scalable/systemsettings.svg" width="24"/> Settings-related icons have also been remade based on a fusion of Infinity's + Reversal's gear icon
- <img src="./copycat/apps/scalable/endeavouros.svg" width="24"/> EndeavourOS (original Endeavour SVG)
- <img src="./copycat/apps/scalable/computer-log-out.svg" width="24"/> Symbolic icons have been modified/replaced

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