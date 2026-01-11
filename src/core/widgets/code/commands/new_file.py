# Python imports


# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    view: GtkSource.View  = None
):
    logger.debug("Command: New File")

    file       = view.command.new_file(view)
    language   = view.language_manager \
                      .guess_language("file.txt", None)

    file.buffer.set_language(language)
    file.buffer.set_style_scheme(view.syntax_theme)

    view.set_buffer(file.buffer)

    has_focus = view.command.exec("has_focus")
    if not has_focus: return file

    view.command.exec("update_info_bar")
    return file
