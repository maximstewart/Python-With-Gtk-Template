# Python imports
import os, signal

# Lib imports
from gi.repository import GLib

# Application imports
from plugins.plugins import Plugins


class Controller_Data:
    ''' Controller_Data contains most of the state of the app at ay given time. It also has some support methods. '''

    def setup_controller_data(self, _settings):
        self.plugins       = Plugins(_settings)

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


    def clear_console(self):
        ''' Clears the terminal screen. '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def call_method(self, _method_name, data = None):
        '''
        Calls a method from scope of class.

                Parameters:
                        a (obj): self
                        b (str): method name to be called
                        c (*): Data (if any) to be passed to the method.
                                Note: It must be structured according to the given methods requirements.

                Returns:
                        Return data is that which the calling method gives.
        '''
        method_name = str(_method_name)
        method      = getattr(self, method_name, lambda data: f"No valid key passed...\nkey={method_name}\nargs={data}")
        return method(data) if data else method()

    def has_method(self, obj, name):
        ''' Checks if a given method exists. '''
        return callable(getattr(obj, name, None))

    def clear_children(self, widget):
        ''' Clear children of a gtk widget. '''
        for child in widget.get_children():
            widget.remove(child)
