# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    editor: GtkSource.View  = None
):
    logger.debug("Move To Right Sibling Command")
    if not editor.sibling_right: return

    buffer = editor.get_buffer()
    sibling_file, popped_file = editor.files.pop_file(buffer)

    editor.set_buffer(sibling_file.buffer)
    editor.sibling_right.set_buffer(buffer)
    editor.sibling_right.files.append(popped_file)
    editor.sibling_right.grab_focus()

