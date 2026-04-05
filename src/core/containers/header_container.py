# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from core.widgets.separator_widget import Separator
from core.widgets.controls.open_files_button import OpenFilesButton
from core.widgets.controls.transparency_scale import TransparencyScale



class HeaderContainer(Gtk.Box):
    def __init__(self):
        super(HeaderContainer, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()

        self.show()


    def _setup_styling(self):
        self.ctx = self.get_style_context()
        self.ctx.add_class("header-container")

        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_hexpand(True)

    def _setup_signals(self):
        self.connect("show", self._handle_show)

    def _subscribe_to_events(self):
        event_system.subscribe("tggl-top-main-menubar", self.tggl_top_main_menubar)

    def _handle_show(self, widget):
        self.disconnect_by_func( self._handle_show )
        self._load_widgets()

    def _load_widgets(self):
        widget_registery.expose_object("header-container", self)

        button = Gtk.Button(label = "Interactive Debug")
        button.connect("clicked", self._interactive_debug)

        self.add( Separator("separator-header", 0) )
        self.add( OpenFilesButton() )
        self.add( TransparencyScale() )
        self.add(button)

    def _interactive_debug(self, widget = None, eve = None):
        event_system.emit("load-interactive-debug")

    def tggl_top_main_menubar(self):
        self.hide() if self.is_visible() else self.show_all()