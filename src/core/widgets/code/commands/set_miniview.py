# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource
from gi.repository import Gio

# Application imports
from ..source_file import SourceFile



def execute(
    editor: GtkSource.View,
):
    logger.debug("Set MiniView  Command")
    event_system.emit("set-mini-view", (editor,))

