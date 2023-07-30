# Python imports
from dataclasses import dataclass

# Lib imports

# Application imports


@dataclass
class Config:
    base_of_home: str
    hide_hidden_files: str
    thumbnailer_path: str
    blender_thumbnailer_path: str
    go_past_home: str
    lock_folder: str
    locked_folders: []
    mplayer_options: str
    music_app: str
    media_app: str
    image_app: str
    office_app: str
    pdf_app: str
    code_app: str
    text_app: str
    file_manager_app: str
    terminal_app: str
    remux_folder_max_disk_usage: str
    make_transparent: int
    main_window_x: int
    main_window_y: int
    main_window_min_width: int
    main_window_min_height: int
    main_window_width: int
    main_window_height: int
