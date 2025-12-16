# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Focus Left Sibling Command")
    if not editor.sibling_left: return
    editor.sibling_left.grab_focus()
