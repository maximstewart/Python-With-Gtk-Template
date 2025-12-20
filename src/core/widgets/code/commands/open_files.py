# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Open File(s) Command")
    gfiles = event_system.emit_and_await("open-files")
    if not gfiles: return

    size   = len(gfiles)
    for i, gfile in enumerate(gfiles):
        file = editor.files.new()
        editor.command.exec_with_args("load_file", (editor, gfile, file))

        if i == (size - 1):
            buffer = editor.get_buffer()
            _file  = editor.files.get_file(buffer)
            _file.unsubscribe(editor)

            editor.set_buffer(file.buffer)
            file.subscribe(editor)
            editor.command.exec("update_info_bar")
