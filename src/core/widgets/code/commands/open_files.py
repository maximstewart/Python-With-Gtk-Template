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
    logger.debug("Open File(s) Command")
    gfiles = event_system.emit_and_await("open_files")
    if not gfiles: return

    size   = len(gfiles)
    for i, gfile in enumerate(gfiles):
        file = editor.files.new()
        file.set_path(gfile)

        language   = editor.language_manager \
                           .guess_language(file.fname, None)
        file.ftype = language
        file.buffer.set_language(language)
        file.buffer.set_style_scheme(editor.syntax_theme)

        if i == (size - 1):
            editor.set_buffer(file.buffer)
    

