# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports



class FooterContainer(Gtk.Box):
    def __init__(self):
        super(FooterContainer, self).__init__()

        self.ctx = self.get_style_context()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

        self.show()


    def _setup_styling(self):
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.set_hexpand(True)

        self.ctx.add_class("footer-container")

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        ...


    def _load_widgets(self):
        ...
