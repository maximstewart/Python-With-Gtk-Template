# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource
from gi.repository import Gio

# Application imports



def execute(
    editor: GtkSource.View,
    uri: str
):
    logger.debug("DnD Load File To Buffer Command")
    if not uri: return

    buffer = editor.get_buffer()
    file   = editor.files.get_file(buffer)

    if not file.ftype == "buffer": return

    gfile  = Gio.File.new_for_uri(uri)
    editor.command.exec_with_args(
        "load_file",
        (editor, gfile, file)
    )

    ctx        = editor.get_parent().get_style_context()
    is_focused = ctx.has_class("source-view-focused")
    if is_focused:
        editor.command.exec("update_info_bar")

    return uri
