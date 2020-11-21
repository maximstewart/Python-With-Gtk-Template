# Python imports
import os

# Gtk imports
import gi, cairo
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk


# Application imports


class Settings:
    def __init__(self):
        self.SCRIPT_PTH = os.path.dirname(os.path.realpath(__file__)) + "/"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.SCRIPT_PTH + "../resources/Main_Window.glade")

        # 'Filters'
        self.office = ('.doc', '.docx', '.xls', '.xlsx', '.xlt', '.xltx', '.xlm',
                                '.ppt', 'pptx', '.pps', '.ppsx', '.odt', '.rtf')
        self.vids   = ('.mkv', '.avi', '.flv', '.mov', '.m4v', '.mpg', '.wmv',
                                                    '.mpeg', '.mp4', '.webm')
        self.txt    = ('.txt', '.text', '.sh', '.cfg', '.conf')
        self.music  = ('.psf', '.mp3', '.ogg' , '.flac')
        self.images = ('.png', '.jpg', '.jpeg', '.gif')
        self.pdf    = ('.pdf')


    def createWindow(self):
        # Get window and connect signals
        window = self.builder.get_object("Main_Window")
        window.connect("delete-event", gtk.main_quit)
        self.setWindowData(window, False)
        return window

    def setWindowData(self, window, paintable):
        screen = window.get_screen()
        visual = screen.get_rgba_visual()

        if visual != None and screen.is_composited():
            window.set_visual(visual)

        # bind css file
        cssProvider  = gtk.CssProvider()
        cssProvider.load_from_path(self.SCRIPT_PTH + '../resources/stylesheet.css')
        screen       = gdk.Screen.get_default()
        styleContext = gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, gtk.STYLE_PROVIDER_PRIORITY_USER)

        window.set_app_paintable(paintable)
        if paintable:
            window.connect("draw", self.area_draw)

    def getMonitorData(self):
        screen = self.builder.get_object("Main_Window").get_screen()
        monitors = []
        for m in range(screen.get_n_monitors()):
            monitors.append(screen.get_monitor_geometry(m))

        for monitor in monitors:
            print("{}x{}+{}+{}".format(monitor.width, monitor.height, monitor.x, monitor.y))

        return monitors

    def area_draw(self, widget, cr):
        cr.set_source_rgba(0, 0, 0, 0.54)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)


    def returnBuilder(self):             return self.builder

    # Filter returns
    def returnOfficeFilter(self):        return self.office
    def returnVidsFilter(self):          return self.vids
    def returnTextFilter(self):          return self.txt
    def returnMusicFilter(self):         return self.music
    def returnImagesFilter(self):        return self.images
    def returnPdfFilter(self):           return self.pdf
