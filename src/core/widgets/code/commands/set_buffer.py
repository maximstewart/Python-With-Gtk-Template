# Python imports


# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports
from ..source_file import SourceFile



def execute(
    view: GtkSource.View,
    file: SourceFile
):
    logger.debug("Command: Set Buffer")

    if not file:
        view.command.new_file(view)
        return

    view.set_buffer(file.buffer)

    has_focus = view.command.exec("has_focus")
    if has_focus:
        view.command.exec("update_info_bar")

