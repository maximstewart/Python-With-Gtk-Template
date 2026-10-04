# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .quad.quad_container import QuadContainer 
from core.widgets.webkit.webkit_ui import WebkitUI
from core.widgets.files.files_base import FilesBase



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
        self.set_size_request(320, -1)

    def _setup_signals(self):
        self.connect("show", self._handle_show)

    def _subscribe_to_events(self):
        ...

    def _handle_show(self, widget):
        self.disconnect_by_func( self._handle_show )
        self._load_widgets()

    def _load_widgets(self):
        widget_registery.expose_object("center-container", self)

        quad_container = QuadContainer()
        files_base     = FilesBase()
        webkit_ui      = WebkitUI()

        button         = Gtk.Button(label = "Click Me!")
        glade_box      = widget_registery.get_object("glade_box")
        files_widget   = files_base.create_tabs_view()

        button.connect("clicked", self._hello_world)
        webkit_ui.load_context_base_path()

        files_widget.create_new_tab("test")
        files_widget.create_new_tab("test2")
        files_widget.create_new_tab("test3")
        files_widget.create_new_tab("test4")
        files_widget.create_new_tab("test5")

        button.show()
        glade_box.show()

        quad_container.top_container.pack1(button, True, True)
        quad_container.top_container.pack2(glade_box, True, True)
        quad_container.bottom_container.pack1(webkit_ui, True, True)
        quad_container.bottom_container.pack2(files_widget, True, True)

        self.add(quad_container)

    def _hello_world(self, widget = None, eve = None):
        logger.debug("Hello, World!")
