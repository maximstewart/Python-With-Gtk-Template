# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    view: GtkSource.View  = None
):
    logger.debug("Close File Command")
    buffer = view.get_buffer()

    sibling_file = view.files_manager.remove_file(buffer)
    if not sibling_file:
        view.command.exec("new_file")
    else:
        view.set_buffer(sibling_file.buffer)

    view.command.exec("update_info_bar")
