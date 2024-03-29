# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.transparency_scale import TransparencyScale



class HeaderContainer(Gtk.Box):
    def __init__(self):
        super(HeaderContainer, self).__init__()

        self.ctx = self.get_style_context()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

        self.show_all()


    def _setup_styling(self):
        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.ctx.add_class("header-container")

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        ...


    def _load_widgets(self):
        button    = Gtk.Button(label = "Interactive Debug")
        button.connect("clicked", self._interactive_debug)

        self.add(TransparencyScale())
        self.add(button)

    def _interactive_debug(self, widget = None, eve = None):
        event_system.emit("load_interactive_debug")
