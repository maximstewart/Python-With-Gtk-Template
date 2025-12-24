# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource
from gi.repository import Gio

# Application imports
from ..source_file import SourceFile



def execute(
    editor: GtkSource.View,
):
    logger.debug("Load Start File(s) Command")

    starting_files = settings_manager.get_starting_files()

    if len(starting_files) == 0: return

    file   = starting_files.pop()
    file   = file.replace("FILE|", "")
    gfile  = Gio.File.new_for_path(file)
    buffer = editor.get_buffer()
    file   = editor.files.get_file(buffer)

    editor.command.exec_with_args(
        "load_file",
        (editor, gfile, file)
    )

    if len(starting_files) == 0: return

    for file in starting_files:
        file  = file.replace("FILE|", "")
        gfile = Gio.File.new_for_path(file)

        editor.command.exec_with_args("load_file", (editor, gfile))
