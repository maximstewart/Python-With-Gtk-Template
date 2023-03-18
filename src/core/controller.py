# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib

# Application imports
from .mixins.signals_mixins import SignalsMixins
from .mixins.dummy_mixin import DummyMixin
from .controller_data import ControllerData
from .core_widget import CoreWidget




class Controller(DummyMixin, SignalsMixins, ControllerData):
    def __init__(self, args, unknownargs):
        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()

        self.setup_controller_data()
        self.print_hello_world() # A mixin method from the DummyMixin file

        logger.info(f"Made it past {self.__class__} loading...")


    def _setup_styling(self):
        ...

    def _setup_signals(self):
        ...


    def _subscribe_to_events(self):
        event_system.subscribe("handle_file_from_ipc", self.handle_file_from_ipc)

    def load_glade_file(self):
        self.builder     = Gtk.Builder()
        self.builder.add_from_file(settings.get_glade_file())
        self.builder.expose_object("main_window", self.window)

        settings.set_builder(self.builder)
        self.core_widget = CoreWidget()

        settings.register_signals_to_builder([self, self.core_widget])

    def get_core_widget(self):
        return self.core_widget
