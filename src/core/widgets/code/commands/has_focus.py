# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Has Focus Command")
    ctx = editor.get_parent().get_style_context()
    return ctx.has_class("source-view-focused")
