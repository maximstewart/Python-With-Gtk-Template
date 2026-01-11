# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    view: GtkSource.View  = None
):
    logger.info("Command: Save File As")
    file   = view.command.get_file(view)
    buffer = file.buffer

    file.save_as()

    language   = view.language_manager \
                       .guess_language(file.fname, None)
    file.ftype = language
    file.buffer.set_language(language)

    view.command.exec("update_info_bar")
