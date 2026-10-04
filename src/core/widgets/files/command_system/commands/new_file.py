# Python imports


# Lib imports
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

# Application imports



def execute(
    view: Gtk.Notebook,
    *args,
    **kwargs
):
    logger.debug("Command: New File")
