# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None,
    buffer: GtkSource.Buffer= None
):
    logger.debug("Show Completion Command")
