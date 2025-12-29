# Python imports

# Lib imports
import gi

gi.require_version('GtkSource', '4')

from gi.repository import GtkSource

# Application imports



def execute(
    view: GtkSource.View  = None
):
    logger.debug("Move To Left Sibling Command")
    if not view.sibling_left: return

    buffer = view.get_buffer()
    popped_file, sibling_file = view.files_manager.swap_file(buffer)

    if sibling_file:
        sibling_file.add_observer(view)
        view.set_buffer(sibling_file.buffer)
    else:
        sibling_file = view.command.exec("new_file")

    popped_file.remove_observer(view)
    popped_file.add_observer(view.sibling_left)

    view.sibling_left.set_buffer(buffer)
    view.sibling_left.grab_focus()
