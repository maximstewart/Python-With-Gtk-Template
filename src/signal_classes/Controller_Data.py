# Python imports
import signal

# Lib imports
from gi.repository import GLib

# Application imports



class Controller_Data:
    def has_method(self, obj, name):
        return callable(getattr(obj, name, None))

    def setup_controller_data(self, _settings):
        self.settings      = _settings
        self.builder       = self.settings.get_builder()
        self.window        = self.settings.get_main_window()
        self.logger        = self.settings.get_logger()

        self.home_path     = self.settings.get_home_path()
        self.success_color = self.settings.get_success_color()
        self.warning_color = self.settings.get_warning_color()
        self.error_color   = self.settings.get_error_color()

        self.window.connect("delete-event", self.tear_down)
        GLib.unix_signal_add(GLib.PRIORITY_DEFAULT, signal.SIGINT, self.tear_down)
