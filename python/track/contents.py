apps = 'apps/scalable/'
places = 'places/scalable'
mimetypes = 'mimetypes/scalable'

# as tuplas devem seguir o padrão (origem, nome do ícone)

# --- apps (com algumas exceções) --------------------------------------------------
plain_folder_group = {
    'group_name': 'Folder-likes - Plain',
    'copies': [
        (apps, 'd3lphin'),
        (apps, 'org.kde.plasma.folder'),
        (apps, 'thunar-filemanager'),
        (apps, 'xfce-filemanager'),
        (apps, 'file-manager-blue'),
        (apps, 'com.system76.CosmicFiles'),
        (apps, 'file-manager'),
        (apps, 'folder_doc_q4os_startmenu'),
        (apps, 'org.kde.dolphin'),
        (apps, 'spacefm-blue'),
        (apps, 'dde-file-manager'),
        (apps, 'dolphin'),
        (apps, 'gnome-commander'),
        (apps, 'gnome-encfs-manager'),
        (apps, 'kfm'),
        (apps, 'nautilus'),
        (apps, 'nemo'),
        (apps, 'redhat-filemanager'),
        (apps, 'system-file-manager'),
        (apps, 'thunar'),
        (apps, 'Thunar'),
        (apps, 'user-file-manager'),
        (apps, 'mc'),
        (apps, 'MidnightCommander'),
        (apps, 'mucommander'),
        (apps, 'nautilus-actions-config-tool'),
        (apps, 'nautilus-actions'),
        (apps, 'org.gnome.files'),
        (apps, 'org.gnome.Files'),
        (apps, 'org.gnome.nautilus'),
        (apps, 'org.gnome.Nautilus'),
        (apps, 'org.kde.index'),
        (apps, 'org.xfce.filemanager'),
        (apps, 'org.xfce.panel.directorymenu'),
        (apps, 'org.xfce.thunar'),
        (apps, 'pcmanfm-qt'),
        (apps, 'spacefm'),
        (apps, 'fma-config-tool'),
        (apps, 'caja-actions'),
        (places, 'folder'),
        (places, 'folder_2'),
        (places, 'gnome-folder'),
        (places, 'gnome-fs-directory-accept'),
        (places, 'gnome-fs-directory'),
        (places, 'gtk-directory'),
        (places, 'inode-directory'),
        (places, 'stock_folder'),
        (mimetypes, 'inode-directory')
    ]
}

variations_group = {
    'group_name': 'Folder-likes - Variations',
    'copies': [
        (apps, 'AirPortUtility'),
        (apps, 'athena'),
        (apps, 'cs-network'),
        (apps, 'gnome-network-properties'),
        (apps, 'kali-wireless-attacks-trans'),
        (apps, 'kfoldersync'),
        (apps, 'krusader_blue'),
        (apps, 'krusader_red'),
        (apps, 'krusader_root'),
        (apps, 'krusader_user'),
        (apps, 'linssid'),
        (apps, 'mate-netspeed-applet'),
        (apps, 'mate-network-properties'),
        (apps, 'nautilus-alt'),
        (apps, 'network-manager'),
        (apps, 'network-workgroup'),
        (apps, 'networkmanager'),
        (apps, 'org.kde.plasma.vault'),
        (apps, 'plasmavault'),
        (apps, 'wicd'),
        (apps, 'wicd-gtk'),
        (apps, 'wifi-radar'),
        (apps, 'winefile'),
    ]
}

derivations_group = {
    'group_name': 'Folder-likes - Derivations',
    'copies': [
        (apps, 'file-manager-green'),
        (apps, 'file-manager-red'),
        (apps, 'spacefm-green'),
        (apps, 'spacefm-red'),
        (apps, 'system-file-manager-root'),
        (places, 'folder-black'),
        (places, 'folder-blue'),
        (places, 'folder-brown'),
        (places, 'folder-cyan'),
        (places, 'folder-green'),
        (places, 'folder-grey'),
        (places, 'folder-magenta'),
        (places, 'folder-orange'),
        (places, 'folder-red'),
        (places, 'folder-violet'),
        (places, 'folder-yellow'),
    ]
}

# --- places --------------------------------------------------
folder_locked_group = {
    'group_name': 'Folder-likes - Locked',
    'copies': [
        (places, 'folder-locked'),
        (places, 'certificate-server'),
        (places, 'folder-ecrypted'),
        (places, 'folder-encrypted'),
    ]
}

folder_home_group = {
    'group_name': 'Folder-likes - Home',
    'copies': [
        (places, 'folder_home'),
        (places, 'folder-home'),
        (places, 'folder-home2'),
        (places, 'gnome-fs-home'),
        (places, 'gnome-home'),
        (places, 'user-home'),
        (places, 'user-home-drag-accept'),
        (places, 'user-home-open')
    ]
}

folder_favorites_group = {
    'group_name': 'Folder-likes - Favorites',
    'copies': [
        (places, 'folder-favorites'),
        (places, 'favorites'),
        (places, 'user-bookmarks'),
        (places, 'folder-bookmarks'),
        (places, 'folder-bookmark'),
        (places, 'gnome-fs-bookmark'),
        (places, 'stock_bookmark'),
        (places, 'bookmark-missing'),
        (places, 'gnome-fs-bookmark-missing'),
        (places, 'stock_delete-bookmark')
    ]
}

folder_download_group = {
    'group_name': 'Folder-likes - Downloads',
    'copies': [
        (places, 'folder-download-open'),
        (places, 'folder-downloads'),
        (places, 'folder-download'),
    ]
}

folder_pictures_group = {
    'group_name': 'Folder-likes - Pictures',
    'copies': [
        (places, 'folder-pictures'),
        (places, 'folder_pictures'),
        (places, 'folder-picture'),
        (places, 'user-images'),
        (places, 'user-pictures'),
        (places, 'folder-pictures-open'),
    ]
}

folder_music_group = {
    'group_name': 'Folder-likes - Music',
    'copies': [
        (places, 'folder-music'),
        (places, 'folder-music-open'),
        (places, 'library-music'),
        (places, 'folder-sound')
    ]
}

folder_remote_group = {
    'group_name': 'Folder-likes - Remote',
    'copies': [
        (places, 'folder-remote-apf'),
        (places, 'folder-remote-ftp'),
        (places, 'folder-remote-nfs'),
        (places, 'folder-remote-smb'),
        (places, 'folder-remote-ssh'),
        (places, 'folder-remote'),
        (places, 'knetattach'),
    ]
}

network_manager_group = {
    'group_name': 'Folder-likes - Network',
    'copies': [
        (places, 'network-manager'),
        (places, 'folder-network'),
        (places, 'network_local'),
        (places, 'network-server'),
        (places, 'network'),
        (places, 'network-workgroup'),
        (places, 'repository'),
    ]
}

user_desktop_group = {
    'group_name': 'Folder-likes - Desktop',
    'copies': [
        (places, 'user-desktop'),
        (places, 'desktop'),
        (places, 'gnome-ccdesktop'),
        (places, 'gnome-desktop-config'),
        (places, 'gnome-desktop'),
        (places, 'gnome-fs-desktop'),
    ]
}

folder_open_group = {
    'group_name': 'Folder-likes - Open',
    'copies': [
        (places, 'folder-open'),
        (places, 'folder_open'),
        (places, 'folder-music-open'),
        (places, 'folder-download-open'),
        (places, 'folder-pictures-open'),
        (places, 'folder-publicshare-open'),
        (places, 'folder-templates-open'),
        (places, 'gnome-fs-directory-open'),
        (places, 'stock_open'),
        (places, 'user-home-open'),
    ]
}

folder_image_group = {
    'group_name': 'Folder-likes - Image',
    'copies': [
        (places, 'folder-image'),
        (places, 'folder-images')
    ]
}

folder_drive_group = {
    'group_name': 'Folder-likes - Drive',
    'copies': [
        (places, 'folder-gdrive'),
        (places, 'folder-google-drive'),
        (places, 'insync-folder')
    ]
}

folder_uniques_group = {
    'group_name': 'Folder-likes - Uniques',
    'copies': [
        (places, 'folder-activities'),
        (places, 'folder-add'),
        (places, 'folder-android'),
        (places, 'folder-applications'),
        (places, 'folder-arduino'),
        (places, 'folder-books'),
        (places, 'folder-cd'),
        (places, 'folder-development'),
        (places, 'folder-dropbox'),
        (places, 'folder-yandex-disk'),
        (places, 'folder-drag-accept.svg'),
        (places, 'folder-steam'),
        (places, 'folder-git'),
        (places, 'folder-gitlab'),
        (places, 'folder-github'),
        (places, 'folder-gnome'),
        (places, 'folder-go'),
        (places, 'folder-important'),
        (places, 'folder-java'),
        (places, 'folder-kde'),
        (places, 'folder-linux'),
        (places, 'folder-mail'),
        (places, 'folder-nextcloud'),
        (places, 'folder-print'),
        (places, 'folder-private'),
        (places, 'folder-projects'),
        (places, 'folder-root'),
        (places, 'folder-snap'),
        (places, 'folder-system'),
        (places, 'folder-tar'),
        (places, 'folder-backup'),
        (places, 'folder-wine'),
        (places, 'folder-3dprint'),
        (places, 'folder-pcloud'),
        (places, 'folder-copy-cloud'),
        (places, 'folder-nextcloud'),
        (places, 'folder-owncloud'),
        (places, 'folder-sync'),
        (places, 'folder-syncthing'),
        (places, 'folder-torrent'),
        (places, 'folder-vbox')
    ]
}

folder_videos_group = {
    'group_name': 'Folder-likes - Videos',
    'copies': [
        (places, 'folder-videos'),
        (places, 'folder-video-alt'),
        (places, 'folder-video')
    ]
}

folder_templates_group = {
    'group_name': 'Folder-likes - Templates',
    'copies': [
        (places, 'folder-templates'),
        (places, 'folder-templates-open')
    ]
}

folder_recent_group = {
    'group_name': 'Folder-likes - Recent',
    'copies': [
        (places, 'folder-recent'),
        (places, 'folder-temp')
    ]
}

folder_cloud_group = {
    'group_name': 'Folder-likes - Cloud',
    'copies': [
        (places, 'folder-cloud'),
        (places, 'folder-CloudStation'),
        (places, 'folder-mail-cloud'),
        (places, 'folder-meocloud'),
        (places, 'folder-synology')
    ]
}

folder_documents_group = {
    'group_name': 'Folder-likes - Documents',
    'copies': [
        (places, 'folder-documents'),
        (places, 'folder_man'),
        (places, 'folder_wordprocessing'),
    ]
}

folder_image_people_group = {
    'group_name': 'Folder-likes - Image People',
    'copies': [
        (places, 'folder-image-people'),
        (places, 'folder_home2'),
    ]
}

folder_megasync_group = {
    'group_name': 'Folder-likes - Mega',
    'copies': [
        (places, 'folder-megasync'),
        (places, 'folder-mega'),
    ]
}

folder_public_group = {
    'group_name': 'Folder-likes - Public',
    'copies': [
        (places, 'folder-publicshare'),
        (places, 'folder-public'),
        (places, 'folder-publicshare-open'),
    ]
}

folder_share_group = {
    'group_name': 'Folder-likes - Share',
    'copies': [
        (places, 'gnome-mime-x-directory-share'),
        (places, 'gnome-mime-x-directory-smb-share'),
        (places, 'gnome-mime-x-directory-smb-workgroup'),
        (places, 'gnome-fs-network'),
        (places, 'gnome-network'),
        (places, 'gtk-network'),
        (places, 'network-server-database'),
        (places, 'redhat-system-group'),
        (places, 'stock_shared-by-me'),
        (places, 'stock_shared-to-me'),
        (places, 'user-share'),
        (places, 'neat'),
    ]
}

folder_saved_search_group = {
    'group_name': 'Folder-likes - Saved Search',
    'copies': [
        (places, 'folder-saved-search'),
        (places, 'application-x-gnome-saved-search'),
    ]
}

folder_text_group = {
    'group_name': 'Folder-likes - Text',
    'copies': [
        (places, 'folder-text'),
        (places, 'folder-txt'),
    ]
}

folder_unlocked_group = {
    'group_name': 'Folder-likes - Unlocked',
    'copies': [
        (places, 'folder-unlocked'),
        (places, 'folder-decrypted'),
    ]
}

folder_visiting_group = {
    'group_name': 'Folder-likes - Visiting',
    'copies': [
        (places, 'folder-visiting'),
        (places, 'gnome-fs-directory-visiting'),
    ]
}

trash_group = {
    'group_name': 'Trash',
    'copies': [
        (places, 'edittrash'),
        (places, 'emptytrash'),
        (places, 'gnome-fs-trash-empty-accept'),
        (places, 'gnome-fs-trash-empty'),
        (places, 'gnome-fs-trash-full'),
        (places, 'gnome-stock-trash-full'),
        (places, 'gnome-stock-trash'),
        (places, 'stock_trash_full'),
        (places, 'trashcan_empty'),
        (places, 'trashcan_full-new'),
        (places, 'trashcan_full'),
        (places, 'user-trash-full'),
        (places, 'user-trash'),
        (places, 'xfce-trash_empty'),
        (places, 'xfce-trash-full'),
        (places, 'xfce-trash_full'),
        (apps, 'trashindicator')
    ]
}

mail_group = {
    'group_name': 'Mail',
    'copies': [
        (places, 'mail-outbox'),
        (places, 'mail-mailbox'),
        (places, 'mail-inbox'),
        (apps, 'bluemail'),
        (apps, 'claws-mail-128x128'),
        (apps, 'claws-mail-32x32'),
        (apps, 'claws-mail-64x64'),
        (apps, 'claws-mail'),
        (apps, 'e-mail'),
        (apps, 'clawsker'),
        (apps, 'kube-mail'),
        (apps, 'xfce-newmail'),
        (apps, 'unity-mail'),
        (apps, 'yast-mail'),
        (apps, 'email-client'),
        (apps, 'email'),
        (apps, 'x-office-mail'),
        (apps, 'xfce-mail'),
        (apps, 'io.elementary.mail'),
        (apps, 'unity-webapps-mail-ru'),
        (apps, 'ximian-evolution-email'),
        (apps, 'internet-mail'),
        (apps, 'deepin-mail'),
        (apps, 'kmailcvt'),
        (apps, 'org.kde.merkuro.mail'),
        (apps, 'org.xfce.mailreader'),
        (apps, 'xfmail'),
        (apps, 'redhat-email'),
        (apps, 'mail-client'),
        (apps, 'mail-generic'),
        (apps, 'mail-notification'),
        (apps, 'mail'),
        (apps, 'mailnag'),
        (apps, 'mailru-mail.ru'),
        (apps, 'mail_generic'),
        (apps, 'package_internet_email'),
        (apps, 'kmail'),
        (apps, 'kmail2'),
        (apps, 'evolution-mail'),
        (apps, 'preferences-mail'),
        (apps, 'internet_mail'),
        (apps, 'org.claws_mail.Claws-Mail'),
    ]
}