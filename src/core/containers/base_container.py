# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .left_container import LeftContainer
from .center_container import CenterContainer
from .right_container import RightContainer



class BaseContainer(Gtk.Box):
    def __init__(self):
        super(BaseContainer, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._load_widgets()

        self.show_all()


    def _setup_styling(self):
        self.set_orientation(Gtk.Orientation.VERTICAL)
        ctx = self.get_style_context()
        ctx.add_class("base-container")

    def _setup_signals(self):
        ...

    def _load_widgets(self):
        self.add(LeftContainer())
        self.add(CenterContainer())
        self.add(RightContainer())
