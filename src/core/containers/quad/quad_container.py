# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .top_container import TopContainer
from .bottom_container import BottomContainer



class QuadContainer(Gtk.Paned):
    def __init__(self):
        super(QuadContainer, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()

        self.show()


    def _setup_styling(self):
        self.ctx = self.get_style_context()
        self.ctx.add_class("quad-container")

        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_wide_handle(True)
        self.set_orientation(Gtk.Orientation.VERTICAL)

    def _setup_signals(self):
        self.connect("show", self._handle_show)
        self.connect("size-allocate", self._size_allocate)

    def _subscribe_to_events(self):
        pass

    def _handle_show(self, widget):
        self.disconnect_by_func( self._handle_show )
        self._load_widgets()

    def _size_allocate(self, widget, allocation):
        self.disconnect_by_func( self._size_allocate )

        self.top_container.set_position( allocation.width / 2 )
        self.bottom_container.set_position( allocation.width / 2 )
        self.set_position( allocation.height / 2 )

    def _load_widgets(self):
        widget_registery.expose_object("quad-container", self)

        self.top_container    = TopContainer()
        self.bottom_container = BottomContainer()

        self.pack1(self.top_container, True, True)
        self.pack2(self.bottom_container, True, True)
