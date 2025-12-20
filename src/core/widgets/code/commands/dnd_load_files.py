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
    uris: list = []
):
    logger.debug("DnD Load Files Command")
    for uri in uris:
        try:
            gfile = Gio.File.new_for_uri(uri)
        except Exception as e:
            gfile = Gio.File.new_for_path(uri)

        editor.command.exec_with_args("load_file", (editor, gfile))