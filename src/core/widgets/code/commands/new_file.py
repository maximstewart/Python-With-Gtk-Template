# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("New File Command")
    file       = editor.files.new()
    language   = editor.language_manager \
                       .guess_language("file.txt", None)

    file.buffer.set_language(language)
    file.buffer.set_style_scheme(editor.syntax_theme)

    editor.set_buffer(file.buffer)
    editor.exec_command("update_info_bar")
