def make_hyperlink(url: str, text: str):
    return f'<a href="{url}" target="_blank">{text}</a>'

icon_packs_credits = [
    {
        'var_name': 'kora',
        'display_name': 'Kora',
        'url': 'https://store.kde.org/p/1256209'
    },
    {
        'var_name': 'breeze',
        'display_name': 'Breeze',
        'url': 'https://github.com/KDE/breeze-icons'
    },
    {
        'var_name': 'marwaita',
        'display_name': 'Marwaita',
        'url': 'https://www.gnome-look.org/p/1239855'
    },
    {
        'var_name': 'morewaita',
        'display_name': 'MoreWaita',
        'url': 'https://www.gnome-look.org/p/2276064'
    },
    {
        'var_name': 'plasma_x',
        'display_name': 'PlasmaX',
        'url': 'https://www.gnome-look.org/p/1367155'
    },
    {
        'var_name': 'infinity',
        'display_name': 'Infinity',
        'url': 'https://www.gnome-look.org/p/2112373'
    },
    {
        'var_name': 'reversal',
        'display_name': 'Reversal',
        'url': 'https://www.gnome-look.org/p/1340791'
    },
    {
        'var_name': 'flat_remix',
        'display_name': 'Flat Remix',
        'url': 'https://store.kde.org/p/1012430'
    },
    {
        'var_name': 'fairywren',
        'display_name': 'FairyWren',
        'url': 'https://www.gnome-look.org/p/1684521'
    },
    {
        'var_name': 'yosa_max',
        'display_name': 'Yosa Max',
        'url': 'https://www.gnome-look.org/p/1196255/'
    },
    {
        'var_name': 'papirus',
        'display_name': 'Papirus',
        'url': 'https://www.gnome-look.org/p/1166289/'
    }
]
scratch = 'made from scratch'

for i_pack in icon_packs_credits:
    # obter os valores do icon pack atual
    pack_var_name = i_pack.get('var_name')
    pack_display_name = i_pack.get('display_name')
    pack_url = i_pack.get('url')

    # criar uma variável global com o nome indicado no dicionário
    # e contendo o conteúdo que make_hyperlink retorna
    globals()[pack_var_name] = make_hyperlink(pack_url, pack_display_name)






"""
# variáveis de cŕeditos/source
kora = '<a href="https://store.kde.org/p/1256209" target="_blank">Kora</a>'
breeze = '<a href="https://github.com/KDE/breeze-icons" target="_blank">Breeze</a>'
marwaita = '<a href="https://www.gnome-look.org/p/1239855" target="_blank">Marwaita</a>'
more_waita = '<a href="https://www.gnome-look.org/p/2276064" target="_blank">MoreWaita</a>'
plasma_x = '<a href="https://www.gnome-look.org/p/1367155" target="_blank">PlasmaX</a>'
infinity = '<a href="https://www.gnome-look.org/p/2112373" target="_blank">Infinity</a>'
reversal = '<a href="https://www.gnome-look.org/p/1340791" target="_blank">Reversal</a>'
flat_remix = '<a href="https://store.kde.org/p/1012430" target="_blank">Flat Remix</a>'
fairy_wren = '<a href="https://www.gnome-look.org/p/1684521" target="_blank">FairyWren</a>'
yosa_max = '<a href="https://www.gnome-look.org/p/1196255/" target="_blank">Yosa Max</a>'
papirus = '<a href="https://www.gnome-look.org/p/1166289/" target="_blank">Papirus</a>'
scratch = 'made from scratch'
"""

APPS_ROWS = [
    {
        'display_name': 'Blender',
        'icon_name': 'blender',
        'icon_source': '<a href="https://commons.wikimedia.org/wiki/File:Blender_logo_no_text.svg">original Blender SVG</a>',
        'icon_changes': 'added a subtle gradient'
    },
    {
        'display_name': 'Godot',
        'icon_name': 'godot',
        'icon_source': plasma_x,
        'icon_changes': 'edited SVG to make the tones match'
    },
    {
        'display_name': 'Inkscape',
        'icon_name': 'inkscape',
        'icon_source': plasma_x,
        'icon_changes': 'edited SVG to make it darker'
    },
    {
        'display_name': 'Krita',
        'icon_name': 'krita',
        'icon_source': marwaita
    },
    {
        'display_name': 'Spotify',
        'icon_name': 'spotify-client',
        'icon_source': marwaita,
        'icon_changes': 'added a subtle gradient'
    },
    {
        'display_name': 'Discord',
        'icon_name': 'discord',
        'icon_source': kora,
        'icon_changes': 'edited SVG to make the color closer to the official Discord burple'
    },
    {
        'display_name': 'Discord Canary',
        'icon_name': 'discord-canary',
        'icon_source': kora,
        'icon_changes': 'background shape changed to be like regular Discord'
    },
    {
        'display_name': 'Discord Development',
        'icon_name': 'discord-development',
        'icon_source': kora,
        'icon_changes': 'modified to match size and style of other Discord variants'
    },
    {
        'display_name': 'GIMP',
        'icon_name': 'gimp',
        'icon_source': breeze,
        'icon_changes': 'edited SVG to make it bigger'
    },
    {
        'display_name': 'Steam',
        'icon_name': 'steam',
        'icon_source': marwaita
    },
    {
        'display_name': 'OBS',
        'icon_name': 'obs',
        'icon_source': kora,
        'icon_changes': 'edited SVG to make it darker'
    },
    {
        'display_name': 'Libresprite',
        'icon_name': 'libresprite',
        'icon_source': scratch
    },
    {
        'display_name': 'Aseprite',
        'icon_name': 'aseprite',
        'icon_source': scratch
    },
    {
        'display_name': 'PureRef',
        'icon_name': 'pureref',
        'icon_source': kora,
        'icon_changes': 'edited SVG to make it darker'
    },
    {
        'display_name': 'DB Browser for SQLite',
        'icon_name': 'sqlitebrowser',
        'icon_source': scratch
    },
    {
        'display_name': 'Audacity',
        'icon_name': 'audacity',
        'icon_source': f'based on {reversal}, but made from scratch',
        'icon_changes': 'changed colors and shapes'
    },
    {
        'display_name': 'VSCodium',
        'icon_name': 'vscodium',
        'icon_source': '<a href="https://github.com/VSCodium/icons/blob/main/icons/linux/nobg/blue1/paulo22s.png">from VSCodium\'s repository</a>'
    },
    {
        'display_name': 'AppImageLauncher',
        'icon_name': 'AppImageLauncher',
        'icon_source': flat_remix,
        'icon_changes': 'modified colors and shapes'
    },
    #{
    #    'display_name': 'Android Studio',
    #    'icon_name': 'android-studio',
    #    'icon_source': fairy_wren,
    #    'icon_changes': 'adjusted colors'
    #},
    # {
    #     'display_name': 'Android Studio Beta',
    #     'icon_name': 'android-studio-beta',
    #     'icon_source': fairy_wren,
    #     'icon_changes': 'adjusted colors'
    # },
    {
        'display_name': 'Android Studio Canary',
        'icon_name': 'android-studio-canary',
        'icon_source': fairy_wren,
        'icon_changes': 'adjusted colors'
    },
    {
        'display_name': 'btop++',
        'icon_name': 'btop',
        'icon_source': f'partially from {kora}',
        'icon_changes': 'remade btop logo from scratch, used Kora\'s system monitor background, MoreWaita\'s btop color'
    },
    {
        'display_name': 'Ark',
        'icon_name': 'ark',
        'icon_source': yosa_max,
        'icon_changes': 'made the gradient more noticeable, rounded the corners and replaced the original zipper with Kora\'s zipper (from the application-x-sogouskin icon)'
    },
    {
        'display_name': 'GitHub Desktop',
        'icon_name': 'appimagekit-github-desktop',
        'icon_source': kora,
        'icon_changes': 'adjusted colors'
    },
    {
        'display_name': 'Color Picker',
        'icon_name': 'nl.hjdskes.gcolor3',
        'icon_source': f'{marwaita} and {yosa_max}',
        'icon_changes': 'used Marwaita\'s color picker background and Yosa Max drop symbol'
    },
    {
        'display_name': 'Kvantum',
        'icon_name': 'kvantum',
        'icon_source': kora,
        'icon_changes': 'switched the colors to Marwaita\'s Kvantum icon'
    },
    {
        'display_name': 'CMake',
        'icon_name': 'cmake',
        'icon_source': kora,
        'icon_changes': 'removed background and added gradients'
    },
    {
        'display_name': 'Roblox',
        'icon_name': 'grapejuice-roblox-player',
        'icon_source': scratch
    },
    {
        'display_name': 'Roblox Studio',
        'icon_name': 'org.vinegarhq.Vinegar.studio',
        'icon_source': scratch
    },
    {
        'display_name': 'Vinegar',
        'icon_name': 'org.vinegarhq.Vinegar',
        'icon_source': 'made from scratch, then added <a href="https://www.svgrepo.com/svg/443560/brand-winehq">this SVG</a> on top of it' 
    },
    {
        'display_name': 'Sober',
        'icon_name': 'org.vinegarhq.Sober',
        'icon_source': scratch
    },
    {
        'display_name': 'OpenJDK Java 21 Shell',
        'icon_name': 'java21-openjdk',
        'icon_source': kora
    },
    {
        'display_name': 'Minecraft',
        'icon_name': 'minecraft',
        'icon_source': scratch
    },
    {
        'display_name': 'Trenchbroom',
        'icon_name': 'com.kristianduske.TrenchBroom',
        'icon_source': scratch
    },
    {
        'display_name': 'Librewolf',
        'icon_name': 'librewolf',
        'icon_source': 'vectorized version of <a href="https://www.reddit.com/r/LibreWolf/comments/t9c84n/icon_update/">this Reddit post</a>'
    },
    {
        'display_name': 'AnimeEffects',
        'icon_name': 'AnimeEffects',
        'icon_source': 'vectorized version based on <a href="https://github.com/AnimeEffectsDevs/AnimeEffects">AnimeEffects repository</a>'
    },
    {
        'display_name': 'Proton Calendar',
        'icon_name': 'protoncalendar',
        'icon_source': kora,
        'icon_changes': 'removed background to match other Proton applications'
    },
    # AINDA NÃO DECIDIDO
    # {
    #     'display_name': 'Krusader',
    #     'icon_name': 'krusader_user',
    #     'icon_source': f'base and cursor from {kora} (apps/preferences-desktop-cursors), colors from <a href="https://commons.wikimedia.org/wiki/File:User-krusader.svg">this SVG</a>'
    # },
    # {
    #     'display_name': 'Krusader (root)',
    #     'icon_name': 'krusader_root',
    #     'icon_source': 'same as above'
    # }

]








"""
PLACES_ROWS = [
    {
        "display_name": "Home",
        "icon_name": "user-home",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Desktop",
        "icon_name": "user-desktop",
        "icon_source": kora,
        "icon_changes": "added a taskbar and icons"
    },
    {
        "display_name": "Documents",
        "icon_name": "folder-documents",
        "icon_source": kora,
        "icon_changes": "added Kora's clip icon to it"
    },
    {
        "display_name": "Music",
        "icon_name": "folder-music",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Music (open)",
        "icon_name": "folder-music-open",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Pictures",
        "icon_name": "folder-pictures",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Pictures (open)",
        "icon_name": "folder-pictures-open",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Videos",
        "icon_name": "folder-videos",
        "icon_source": kora,
        "icon_changes": "changed icon to a play button and added details"
    },
    {
        "display_name": "Public",
        "icon_name": "folder-publicshare",
        "icon_source": f'{kora} and <a href="https://www.svgrepo.com/svg/451439/walking">this stickman</a>',
        "icon_changes": 'changed the symbol to a stickman from SVG Repo'
    },
    {
        "display_name": "Public (open)",
        "icon_name": "folder-publicshare-open",
        "icon_source": kora,
        "icon_changes": "same as above"
    },
    {
        "display_name": "User share",
        "icon_name": "user-share",
        "icon_source": kora,
        "icon_changes": "changed the symbol color from white to dark blue to match other folder icons"
    },

    # a partir daqui, só normalização de gradiente

    {
        "display_name": "Books",
        "icon_name": "folder-books",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Wine",
        "icon_name": "folder-wine",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "HTML",
        "icon_name": "folder-html",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Locked",
        "icon_name": "folder-locked",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Unlocked",
        "icon_name": "folder-unlocked",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "3DPrint",
        "icon_name": "folder-3dprint",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Add",
        "icon_name": "folder-add",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Android",
        "icon_name": "folder-android",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Applications",
        "icon_name": "folder-applications",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Arduino",
        "icon_name": "folder-arduino",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Backup",
        "icon_name": "folder-backup",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "CD",
        "icon_name": "folder-cd",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Copy Cloud",
        "icon_name": "folder-copy-cloud",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Development",
        "icon_name": "folder-development",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Dropbox",
        "icon_name": "folder-dropbox",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Favorites",
        "icon_name": "folder-favorites",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "GDrive",
        "icon_name": "folder-gdrive",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Go",
        "icon_name": "folder-go",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Image people",
        "icon_name": "folder-image-people",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "KDE",
        "icon_name": "folder-kde",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Linux",
        "icon_name": "folder-linux",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Megasync",
        "icon_name": "folder-megasync",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Nextcloud",
        "icon_name": "folder-nextcloud",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Owncloud",
        "icon_name": "folder-owncloud",
        "icon_source": f'{kora} and {papirus}',
        "icon_changes": "normalized gradient and replaced Kora's symbol with Papirus' Owncloud symbol instead"
    },
    {
        "display_name": "Projects",
        "icon_name": "folder-projects",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Recent",
        "icon_name": "folder-recent",
        "icon_source": kora,
        "icon_changes": "normalized gradient and converted the symbol to a SVG path"
    },
    {
        "display_name": "Root",
        "icon_name": "folder-root",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Saved search",
        "icon_name": "folder-saved-search",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Script",
        "icon_name": "folder-script",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Snap",
        "icon_name": "folder-snap",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Sync",
        "icon_name": "folder-sync",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "Syncthing",
        "icon_name": "folder-syncthing",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "System",
        "icon_name": "folder-system",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    },
    {
        "display_name": "VBox",
        "icon_name": "folder-vbox",
        "icon_source": kora,
        "icon_changes": "normalized gradient and converted the symbol to a SVG path"
    },
    {
        "display_name": "Network",
        "icon_name": "folder-network",
        "icon_source": kora,
        "icon_changes": "normalized gradient"
    }
]









MIMETYPES_ROWS = [
    {
        "display_name": "Zipped",
        "icon_name": "zip",
        "icon_source": kora,
        "icon_changes": "fused the original zip icon with application-x-sogouskin.svg, and adjusted colors to match Ark"
    },
    {
        "display_name": "Kotlin",
        "icon_name": "text-x-kotlin",
        "icon_source": f'{kora} and <a href="https://commons.wikimedia.org/wiki/File:Kotlin_icon_(2021-present).svg">Wikimedia</a>',
        "icon_changes": "updated the symbol to the new Kotlin logo and applied the colors of its gradient"
    },
    {
        "display_name": "Rust",
        "icon_name": "text-rust",
        "icon_source": f'{kora} and <a href="https://commons.wikimedia.org/wiki/File:Kotlin_icon_(2021-present).svg">the original Rust SVG</a>',
        "icon_changes": "changed the 'RS' text to the Rust symbol (without the gear)"
    }

]









OTHERS_ROWS = [
    {
        "display_name": "Settings",
        "icon_name": "systemsettings",
        "icon_source": f"{infinity} and {reversal}",
        "icon_changes": f"remade based on a fusion of Infinity's + Reversal' gear icon"
    },
    {
        "display_name": "EndeavourOS",
        "icon_name": "endeavouros",
        "icon_source": "original EndeavourOS SVG"
    }
]
"""