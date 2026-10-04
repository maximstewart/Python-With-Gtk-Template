# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

# Application imports



class FilesView(Gtk.ScrolledWindow):
    def __init__(self):
        super(FilesView, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

        self.show()


    def _setup_styling(self):
        ...

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        ...

    def _load_widgets(self):
        ...

    def get_icon_grid(self) -> Gtk.IconView:
        return self.get_children()[0].get_children()[0]

    def bind_icon_grid(self, icon_grid: Gtk.IconView):
        self.add(icon_grid)

        # viewport = Gtk.Viewport(icon_grid)

        # viewport.show()
        # self.add(viewport)
