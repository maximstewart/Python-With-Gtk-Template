# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

# Application imports
from .tab_dto import  TabDTO



class TabsView(Gtk.Notebook):
    def __init__(self):
        super(TabsView, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

        self.show()


    def _setup_styling(self):
        self.set_scrollable(True)

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        ...

    def _load_widgets(self):
        ...

    def create_new_tab(self, name: str) -> TabDTO:
        if not name:
            logger.error("Must give a path to load...")
            return

        tab_dto = TabDTO()
        tab_dto.tab_header.label.set_label(name)

        self.append_page(
            tab_dto.files_view,
            tab_dto.tab_header
        )

        self.set_tab_detachable(tab_dto.files_view, True)
        self.set_tab_reorderable(tab_dto.files_view, True)

        return tab_dto
