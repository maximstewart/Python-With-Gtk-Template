# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports



class TabHeader(Gtk.Box):
    """docstring for TabHeader"""

    def __init__(self):
        super(TabHeader, self).__init__()

        self._setup_styling()
        self._setup_signals()
        self._load_widgets()

        self.show_all()


    def _setup_styling(self):
        self.set_orientation(0)
        self.set_hexpand(False)

    def _setup_signals(self):
        ...

    def _load_widgets(self):
        self.label      = Gtk.Label()
        self.close_bttn = Gtk.Button()
        icon            = Gtk.Image(stock = Gtk.STOCK_CLOSE)

        self.label.set_xalign(0.0)
        self.label.set_margin_left(25)
        self.label.set_margin_right(25)
        self.label.set_hexpand(True)

        self.close_bttn.add(icon)
        self.add(self.label)
        self.add(self.close_bttn)


    def bind_close_signal(self, close_method: callable):
        self._close_handler_id = self.close_bttn.connect("released", close_method)

    def clear_signals_and_data(self):
        self.close_bttn.disconnect(self._close_handler_id)
        self._close_tab        = None
        self._close_handler_id = None

        for child in self.get_children():
            child.unparent()
            child.run_dispose()
            child.destroy()
