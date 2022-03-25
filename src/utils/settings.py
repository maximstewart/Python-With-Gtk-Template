# Python imports
import os, json

# Gtk imports
import gi, cairo
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk


# Application imports
from .logger import Logger
from .keybindings import Keybindings



class Settings:
    def __init__(self):
        self._SCRIPT_PTH    = os.path.dirname(os.path.realpath(__file__))
        self._USER_HOME     = os.path.expanduser('~')
        self._CONFIG_PATH   = f"{self._USER_HOME}/.config/{app_name.lower()}"
        self._PLUGINS_PATH  = f"{self._CONFIG_PATH}/plugins"
        self._GLADE_FILE    = f"{self._CONFIG_PATH}/Main_Window.glade"
        self._KEY_BINDINGS  = f"{self._CONFIG_PATH}/key-bindings.json"
        self._CSS_FILE      = f"{self._CONFIG_PATH}/stylesheet.css"
        self._DEFAULT_ICONS = f"{self._CONFIG_PATH}/icons"
        self._WINDOW_ICON   = f"{self._DEFAULT_ICONS}/{app_name.lower()}.png"
        self._USR_PATH      = f"/usr/share/{app_name.lower()}"

        if not os.path.exists(self._CONFIG_PATH):
            os.mkdir(self._CONFIG_PATH)
        if not os.path.exists(self._PLUGINS_PATH):
            os.mkdir(self._PLUGINS_PATH)

        if not os.path.exists(self._GLADE_FILE):
            self._GLADE_FILE   = f"{self._USR_PATH}/Main_Window.glade"
        if not os.path.exists(self._KEY_BINDINGS):
            self._KEY_BINDINGS  = f"{self._USR_SOLARFM}/key-bindings.json"
        if not os.path.exists(self._CSS_FILE):
            self._CSS_FILE     = f"{self._USR_PATH}/stylesheet.css"
        if not os.path.exists(self._WINDOW_ICON):
            self._WINDOW_ICON  = f"{self._USR_PATH}/icons/{app_name.lower()}.png"
        if not os.path.exists(self._DEFAULT_ICONS):
            self.DEFAULT_ICONS = f"{self._USR_PATH}/icons"

        # '_filters'
        self._office_filter = ('.doc', '.docx', '.xls', '.xlsx', '.xlt', '.xltx', '.xlm', '.ppt', 'pptx', '.pps', '.ppsx', '.odt', '.rtf')
        self._vids_filter   = ('.mkv', '.avi', '.flv', '.mov', '.m4v', '.mpg', '.wmv', '.mpeg', '.mp4', '.webm')
        self._txt_filter    = ('.txt', '.text', '.sh', '.cfg', '.conf')
        self._music_filter  = ('.psf', '.mp3', '.ogg' , '.flac')
        self._images_filter = ('.png', '.jpg', '.jpeg', '.gif', '.ico', '.tga')
        self._pdf_filter    = ('.pdf')

        self._success_color = "#88cc27"
        self._warning_color = "#ffa800"
        self._error_color   = "#ff0000"

        self._keybindings = Keybindings()
        with open(self._KEY_BINDINGS) as file:
            keybindings = json.load(file)["keybindings"]
            self._keybindings.configure(keybindings)

        self._main_window   = None
        self._logger        = Logger(self._CONFIG_PATH).get_logger()
        self._builder       = Gtk.Builder()
        self._builder.add_from_file(self._GLADE_FILE)



    def create_window(self) -> None:
        # Get window and connect signals
        self._main_window = self._builder.get_object("Main_Window")
        self.set_window_data()

    def set_window_data(self)  -> None:
        self._main_window.set_icon_from_file(self._WINDOW_ICON)
        screen = self._main_window.get_screen()
        visual = screen.get_rgba_visual()

        if visual != None and screen.is_composited():
            self._main_window.set_visual(visual)
            self._main_window.set_app_paintable(True)
            self._main_window.connect("draw", self.draw_area)

        # bind css file
        cssProvider  = Gtk.CssProvider()
        cssProvider.load_from_path(self._CSS_FILE)
        screen       = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def get_monitor_data(self) -> list:
        screen = self._builder.get_object("Main_Window").get_screen()
        monitors = []
        for m in range(screen.get_n_monitors()):
            monitors.append(screen.get_monitor_geometry(m))
            print("{}x{}|{}+{}".format(monitor.width, monitor.height, monitor.x, monitor.y))

        return monitors

    def draw_area(self, widget, cr):
        cr.set_source_rgba(0, 0, 0, 0.54)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)



    def get_main_window(self)   -> Gtk.ApplicationWindow: return self._main_window
    def get_builder(self)       -> Gtk.Builder:  return self._builder
    def get_logger(self)        -> Logger:       return self._logger
    def get_keybindings(self)   -> Keybindings:  return self._keybindings
    def get_plugins_path(self)  -> str:          return self._PLUGINS_PATH
    def get_home_path(self)     -> str:          return self._USER_HOME

    # Filter returns
    def get_office_filter(self) -> tuple: return self._office_filter
    def get_vids_filter(self)   -> tuple: return self._vids_filter
    def get_text_filter(self)   -> tuple: return self._txt_filter
    def get_music_filter(self)  -> tuple: return self._music_filter
    def get_images_filter(self) -> tuple: return self._images_filter
    def get_pdf_filter(self)    -> tuple: return self._pdf_filter

    def get_success_color(self) -> str:   return self._success_color
    def get_warning_color(self) -> str:   return self._warning_color
    def get_error_color(self)   -> str:   return self._error_color
