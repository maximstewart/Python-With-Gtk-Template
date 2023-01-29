# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports




class CoreWidget(Gtk.Box):
    def __init__(self):
        super(CoreWidget, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._load_widgets()

        self.show_all()


    def _setup_styling(self):
        self.set_orientation(1)

    def _setup_signals(self):
        ...

    def _load_widgets(self):
        button = Gtk.Button(label="Click Me!")
        button.connect("clicked", self._hello_world)

        self.add(button)

    def _hello_world(self, widget=None, eve=None):
        print("Hello, World!")
