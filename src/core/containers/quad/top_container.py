# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports



class TopContainer(Gtk.Paned):
    def __init__(self):
        super(TopContainer, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()

        self.show()


    def _setup_styling(self):
        self.ctx = self.get_style_context()
        self.ctx.add_class("quad-top-container")

        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_wide_handle(True)
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

    def _setup_signals(self):
        self.connect("show", self._handle_show)

    def _subscribe_to_events(self):
        pass

    def _handle_show(self, widget):
        self.disconnect_by_func( self._handle_show )
        self._load_widgets()
        self.show_all()

    def _load_widgets(self):
        widget_registery.expose_object("quad-top-container", self)
