def make_hyperlink(url: str, text: str):
    return f'<a href="{url}" target="_blank">{text}</a>'

kora       = make_hyperlink('https://store.kde.org/p/1256209', 'Kora')
breeze     = make_hyperlink('https://github.com/KDE/breeze-icons', 'Breeze')
marwaita   = make_hyperlink('https://www.gnome-look.org/p/1239855', 'Marwaita')
morewaita  = make_hyperlink('https://www.gnome-look.org/p/2276064', 'MoreWaita')
plasma_x   = make_hyperlink('https://www.gnome-look.org/p/1367155', 'PlasmaX')
infinity   = make_hyperlink('https://www.gnome-look.org/p/2112373', 'Infinity')
reversal   = make_hyperlink('https://www.gnome-look.org/p/1340791', 'Reversal')
flat_remix = make_hyperlink('https://store.kde.org/p/1012430', 'Flat Remix')
fairywren  = make_hyperlink('https://www.gnome-look.org/p/1684521', 'FairyWren')
yosa_max   = make_hyperlink('https://www.gnome-look.org/p/1196255/', 'Yosa Max')
papirus    = make_hyperlink('https://www.gnome-look.org/p/1166289/', 'Papirus')
qogir      = make_hyperlink('https://github.com/vinceliuice/Qogir-icon-theme', 'Qogir')
fluent     = make_hyperlink('https://store.kde.org/p/1477945', 'Fluent')
scratch = 'made from scratch'

FIRST_CHUNK = f'''
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
{kora}, {breeze}, {marwaita}, {morewaita}, {plasma_x}, {infinity}, {reversal}, {flat_remix}, {fairywren}, {yosa_max}, {papirus}, {qogir}, {fluent}

## Major differences
'''

LAST_CHUNK = '''
## License
[GPL3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
'''

APPS_ROWS = [
    {
        'display_name': 'Blender',
        'icon_name': 'blender',
        'icon_source': make_hyperlink('https://commons.wikimedia.org/wiki/File:Blender_logo_no_text.svg', 'original Blender logo'),
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
        'icon_name': 'com.github.libresprite.LibreSprite',
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
        'icon_source': f'adapted from {make_hyperlink('https://www.svgrepo.com/svg/28272/database-analysing', 'SVG Repo')}'
    },
    {
        'display_name': 'Audacity',
        'icon_name': 'audacity',
        'icon_source': f'{yosa_max} and {fluent}',
        'icon_changes': f'changed the headphones symbol to {fluent} headphones, normalized the background shape with other rectangular {kora} icons and adjusted the gradients'
    },
    {
        'display_name': 'VSCodium',
        'icon_name': 'vscodium',
        'icon_source': make_hyperlink('https://github.com/VSCodium/icons/blob/main/icons/linux/nobg/blue1/paulo22s.png', 'from VSCodium repository')
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
    # {
    #     'display_name': 'Android Studio Canary',
    #     'icon_name': 'android-studio-canary',
    #     'icon_source': fairywren,
    #     'icon_changes': 'adjusted colors'
    # },
    {
        'display_name': 'btop++',
        'icon_name': 'btop',
        'icon_source': f'partially from {kora}',
        'icon_changes': f'remade btop logo from scratch, used {kora} system monitor background, {morewaita} btop color'
    },
    # {
    #     'display_name': 'Ark',
    #     'icon_name': 'accessories-archiver',
    #     'icon_source': yosa_max,
    #     'icon_changes': f'made the gradient more noticeable, rounded the corners and replaced the original zipper with {kora} zipper (from the application-x-sogouskin icon)'
    # },
    {
        'display_name': 'Ark',
        'icon_name': 'accessories-archiver',
        'icon_source': qogir,
        'icon_changes': f'made the colors match with the zip mimetypes and replaced the original zipper with {kora} zipper (from the application-x-sogouskin icon)'
    },
    {
        'display_name': 'GitHub Desktop',
        'icon_name': 'github-desktop',
        'icon_source': kora,
        'icon_changes': 'adjusted colors'
    },
    {
        'display_name': 'Color Picker',
        'icon_name': 'gcolor3',
        'icon_source': f'{marwaita} and {yosa_max}',
        'icon_changes': f'used {marwaita} color picker background and Yosa Max drop symbol'
    },
    {
        'display_name': 'Kvantum',
        'icon_name': 'kvantum',
        'icon_source': kora,
        'icon_changes': f'switched the colors to {marwaita} Kvantum icon'
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
        'icon_name': 'grapejuice-roblox-studio',
        'icon_source': scratch
    },
    {
        'display_name': 'Vinegar',
        'icon_name': 'io.github.vinegarhq.Vinegar',
        'icon_source': f'made from scratch, then added {make_hyperlink('https://www.svgrepo.com/svg/443560/brand-winehq', 'this SVG')} on top of it'
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
    # {
    #     'display_name': 'Minecraft',
    #     'icon_name': 'minecraft',
    #     'icon_source': scratch
    # },
    # {
    #     'display_name': 'Trenchbroom',
    #     'icon_name': 'com.kristianduske.TrenchBroom',
    #     'icon_source': scratch
    # },
    {
        'display_name': 'Librewolf',
        'icon_name': 'librewolf',
        'icon_source': f'vectorized version of {make_hyperlink('https://www.reddit.com/r/LibreWolf/comments/t9c84n/icon_update/', 'this Reddit post')}'
    },
    {
        'display_name': 'AnimeEffects',
        'icon_name': 'AnimeEffects',
        'icon_source': f'vectorized version based on {make_hyperlink('https://github.com/AnimeEffectsDevs/AnimeEffects', 'AnimeEffects repository')}'
    },
    {
        'display_name': 'Proton Calendar',
        'icon_name': 'protoncalendar',
        'icon_source': kora,
        'icon_changes': 'removed background to match other Proton applications'
    },
    {
        'display_name': 'Mail',
        'icon_name': 'mail_generic',
        'icon_source': papirus,
        'icon_changes': f'changed colors to match {kora} original mail icons and added gradients. @ symbol taken from the icon application-mbox'
    },
    {
        'display_name': 'BlueMail',
        'icon_name': 'bluemail',
        'icon_source': papirus,
        'icon_changes': 'changed colors to be closer to the original logo and added gradients'
    },
    {
        'display_name': 'Bitwig',
        'icon_name': 'bitwig',
        'icon_source': kora,
        'icon_changes': 'adjusted to match the colors and proportions of Bitwig mimetypes'
    },
    # AINDA NÃO DECIDIDO
    # {
    #     'display_name': 'Krusader',
    #     'icon_name': 'krusader_user',
    #     'icon_source': f'base and cursor from {kora} (apps/preferences-desktop-cursors), colors from {make_hyperlink('https://commons.wikimedia.org/wiki/File:User-krusader.svg', 'this SVG')}
    # },
    # {
    #     'display_name': 'Krusader (root)',
    #     'icon_name': 'krusader_root',
    #     'icon_source': 'same as above'
    # },
    {
        'display_name': 'Vesktop',
        'icon_name': 'dev.vencord.Vesktop',
        'icon_source': f'vectorized version of the {make_hyperlink("https://github.com/Vencord/Vesktop", "original logo")} and {kora}',
        'icon_changes': f'fused the {make_hyperlink("https://github.com/Vencord/Vesktop", "original logo")} with the with the base shape of the agentdesktop icon from {kora} (and used {make_hyperlink('https://vencord.dev/', 'this alternative logo')} to recreate the Z pattern in the "C" letter)'
    },
    {
        'display_name': 'Calculator',
        'icon_name': 'accessories-calculator',
        'icon_source': make_hyperlink('www.svgrepo.com/svg/362041/calculator', 'SVG Repo'),
        'icon_changes': 'changed colors and added gradients'
    }
]

PLACES_ROWS = [
    {
        'display_name': 'Home',
        'icon_name': 'user-home',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Desktop',
        'icon_name': 'user-desktop',
        'icon_source': kora,
        'icon_changes': 'added a taskbar and icons'
    },
    # {
    #     'display_name': 'Documents',
    #     'icon_name': 'folder-documents',
    #     'icon_source': kora,
    #     'icon_changes': f'added {kora} clip icon to it'
    # },
    {
        'display_name': 'Music',
        'icon_name': 'folder-music',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Music (open)',
        'icon_name': 'folder-music-open',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Pictures',
        'icon_name': 'folder-pictures',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Pictures (open)',
        'icon_name': 'folder-pictures-open',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Videos',
        'icon_name': 'folder-videos',
        'icon_source': kora,
        'icon_changes': 'changed icon to a play button and added details'
    },
    {
        'display_name': 'Public',
        'icon_name': 'folder-publicshare',
        'icon_source': f'{kora} and {make_hyperlink('https://www.svgrepo.com/svg/451439/walking', 'this stickman')}',
        'icon_changes': f'changed the symbol to a stickman from SVG Repo'
    },
    {
        'display_name': 'Public (open)',
        'icon_name': 'folder-publicshare-open',
        'icon_source': kora,
        'icon_changes': 'same as above'
    },
    {
        'display_name': 'User share',
        'icon_name': 'user-share',
        'icon_source': kora,
        'icon_changes': f'changed the symbol color from white to dark blue to match other folder icons'
    },
    {
        'display_name': 'Books',
        'icon_name': 'folder-books',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Wine',
        'icon_name': 'folder-wine',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'HTML',
        'icon_name': 'folder-html',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Locked',
        'icon_name': 'folder-locked',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Unlocked',
        'icon_name': 'folder-unlocked',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': '3DPrint',
        'icon_name': 'folder-3dprint',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Add',
        'icon_name': 'folder-add',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Android',
        'icon_name': 'folder-android',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Applications',
        'icon_name': 'folder-applications',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Arduino',
        'icon_name': 'folder-arduino',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Backup',
        'icon_name': 'folder-backup',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'CD',
        'icon_name': 'folder-cd',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Copy Cloud',
        'icon_name': 'folder-copy-cloud',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Development',
        'icon_name': 'folder-development',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Dropbox',
        'icon_name': 'folder-dropbox',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Favorites',
        'icon_name': 'folder-favorites',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'GDrive',
        'icon_name': 'folder-gdrive',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Go',
        'icon_name': 'folder-go',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Image people',
        'icon_name': 'folder-image-people',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'KDE',
        'icon_name': 'folder-kde',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Linux',
        'icon_name': 'folder-linux',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Megasync',
        'icon_name': 'folder-megasync',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Nextcloud',
        'icon_name': 'folder-nextcloud',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Owncloud',
        'icon_name': 'folder-owncloud',
        'icon_source': f'{kora} and {papirus}',
        'icon_changes': f'normalized gradient and replaced {kora} symbol with {papirus} Owncloud symbol instead'
    },
    {
        'display_name': 'Projects',
        'icon_name': 'folder-projects',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Recent',
        'icon_name': 'folder-recent',
        'icon_source': kora,
        'icon_changes': 'normalized gradient and converted the symbol to a SVG path'
    },
    {
        'display_name': 'Root',
        'icon_name': 'folder-root',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Saved search',
        'icon_name': 'folder-saved-search',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Script',
        'icon_name': 'folder-script',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Snap',
        'icon_name': 'folder-snap',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Sync',
        'icon_name': 'folder-sync',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'Syncthing',
        'icon_name': 'folder-syncthing',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'System',
        'icon_name': 'folder-system',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    },
    {
        'display_name': 'VBox',
        'icon_name': 'folder-vbox',
        'icon_source': kora,
        'icon_changes': 'normalized gradient and converted the symbol to a SVG path'
    },
    {
        'display_name': 'Network',
        'icon_name': 'network-manager',
        'icon_source': kora,
        'icon_changes': 'normalized gradient'
    }
]

MIMETYPES_ROWS = [
    # {
    #     'display_name': 'Zipped',
    #     'icon_name': 'zip',
    #     'icon_source': kora,
    #     'icon_changes': 'fused the original zip icon with application-x-sogouskin.svg, and adjusted colors to match Ark'
    # },
    {
        'display_name': 'Kotlin',
        'icon_name': 'text-x-kotlin',
        'icon_source': f'{kora} and {make_hyperlink('https://commons.wikimedia.org/wiki/File:Kotlin_icon_(2021-present).svg', 'Wikimedia')}',
        'icon_changes': 'updated the symbol to the new Kotlin logo and applied the colors of its gradient'
    },
    {
        'display_name': 'Rust',
        'icon_name': 'text-rust',
        'icon_source': f'{kora} and {make_hyperlink('https://commons.wikimedia.org/wiki/File:Kotlin_icon_(2021-present).svg', 'the original Rust SVG')}',
        'icon_changes': "changed the 'RS' text to the Rust symbol (without the gear)"
    }
]

OTHERS_ROWS = [
    {
        'display_name': 'Settings',
        'icon_name': 'preferences-system',
        'icon_source': make_hyperlink('https://www.svgrepo.com/svg/362053/cog', 'SVG Repo'),
        'icon_changes': 'added gradients and modified proportions'
        #'icon_source': f'{infinity} and {reversal}',
        #'icon_changes': f'remade based on a fusion of {infinity} and {reversal} gear icon'
    },
    {
        'display_name': 'EndeavourOS',
        'icon_name': 'endeavouros',
        'icon_source': make_hyperlink('https://github.com/endeavouros-team/EndeavourOS-Development?tab=readme-ov-file', 'original EndeavourOS SVG')
    }
]