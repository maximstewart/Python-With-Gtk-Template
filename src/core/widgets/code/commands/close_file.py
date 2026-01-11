# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    view: GtkSource.View  = None
):
    logger.debug("Command: Close File")
    view.command.remove_file()
    view.command.exec("update_info_bar")
