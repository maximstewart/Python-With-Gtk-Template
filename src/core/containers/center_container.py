# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.webkit.webkit_ui import WebkitUI



class CenterContainer(Gtk.Box):
    def __init__(self):
        super(CenterContainer, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()

        self.show()


    def _setup_styling(self):
        self.ctx = self.get_style_context()
        self.ctx.add_class("center-container")

        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_hexpand(True)
        self.set_vexpand(True)

    def _setup_signals(self):
        self.connect("show", self._handle_show)

    def _subscribe_to_events(self):
        ...

    def _handle_show(self, widget):
        self.disconnect_by_func( self._handle_show )
        self._load_widgets()

    def _load_widgets(self):
        widget_registery.expose_object("center-container", self)

        glade_box = widget_registery.get_object("glade_box")
        button    = Gtk.Button(label = "Click Me!")
        webkit_ui = WebkitUI()

        webkit_ui.load_context_base_path()

        button.connect("clicked", self._hello_world)

        button.show()
        glade_box.show()

        self.add(button)
        self.add(glade_box)
        self.add(webkit_ui)

    def _hello_world(self, widget = None, eve = None):
        logger.debug("Hello, World!")