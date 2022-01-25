# Python imports
import threading, subprocess, time


# Gtk imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

# Application imports
from .mixins import *
from . import Controller_Data



def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper


class Controller(DummyMixin, Controller_Data):
    def __init__(self, _settings, args, unknownargs):
        self.setup_controller_data(_settings)
        self.window.show()
        self.print_hello_world() # A mixin method from the DummyMixin file


    def tear_down(self, widget=None, eve=None):
        event_system.send_ipc_message("close server")

        time.sleep(event_sleep_time)
        Gtk.main_quit()


    @threaded
    def gui_event_observer(self):
        while True:
            time.sleep(event_sleep_time)
            event = event_system.consume_gui_event()
            if event:
                try:
                    type, target, data = event
                    method = getattr(self.__class__, type)
                    GLib.idle_add(method, (self, data,))
                except Exception as e:
                    print(repr(e))



    def get_clipboard_data(self):
        proc    = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        retcode = proc.wait()
        data    = proc.stdout.read()
        return data.decode("utf-8").strip()

    def set_clipboard_data(self, data):
        proc = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        proc.stdin.write(data)
        proc.stdin.close()
        retcode = proc.wait()
