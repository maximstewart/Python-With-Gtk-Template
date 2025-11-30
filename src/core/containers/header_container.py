# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.controls.open_files_button import OpenFilesButton
from ..widgets.controls.transparency_scale import TransparencyScale



class HeaderContainer(Gtk.Box):
    def __init__(self):
        super(HeaderContainer, self).__init__()

        self.ctx = self.get_style_context()

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

        self.show()


    def _setup_styling(self):
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.set_hexpand(True)

        self.ctx.add_class("header-container")

    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        event_system.subscribe("tggl-top-main-menubar", self.tggl_top_main_menubar)


    def _load_widgets(self):
        button = Gtk.Button(label = "Interactive Debug")
        button.connect("clicked", self._interactive_debug)

        self.add( OpenFilesButton() )
        self.add( TransparencyScale() )
        self.add(button)

    def _interactive_debug(self, widget = None, eve = None):
        event_system.emit("load-interactive-debug")

    def tggl_top_main_menubar(self):
        self.hide() if self.is_visible() else self.show_all()