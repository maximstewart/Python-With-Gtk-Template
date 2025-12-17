# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Set Focus Border Command")
    ctx = editor.get_style_context()
    ctx.add_class("source-view-focused")

    if editor.sibling_right:
        ctx = editor.sibling_right.get_style_context()
    elif editor.sibling_left:
        ctx = editor.sibling_left.get_style_context()

    ctx.remove_class("source-view-focused")
