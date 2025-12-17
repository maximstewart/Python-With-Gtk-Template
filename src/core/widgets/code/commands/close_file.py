# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Close File Command")
    file   = editor.files.new()
    buffer = editor.get_buffer()
    editor.set_buffer(file.buffer)

    editor.files.remove_file(buffer)
    editor.command.exec("update_info_bar")
