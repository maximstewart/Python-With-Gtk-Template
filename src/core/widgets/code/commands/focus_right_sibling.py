# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Focus Right Sibling Command")
    if not editor.sibling_right: return
    editor.sibling_right.grab_focus()
    editor.sibling_right.command.exec("set_miniview")