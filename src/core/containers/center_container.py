# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports



class CenterContainer(Gtk.Box):
    def __init__(self):
        super(CenterContainer, self).__init__()

        self._builder = settings_manager.get_builder()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()


    def _setup_styling(self):
        self.set_orientation(Gtk.Orientation.VERTICAL)
        ctx = self.get_style_context()
        ctx.add_class("center-container")

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        # event_system.subscribe("handle_file_from_ipc", self.handle_file_from_ipc)
        ...

    def _load_widgets(self):
        glade_box = self._builder.get_object("glade_box")
        button    = Gtk.Button(label="Click Me!")

        button.connect("clicked", self._hello_world)

        self.add(button)
        self.add(glade_box)


    def _hello_world(self, widget=None, eve=None):
        logger.debug("Hello, World!")
