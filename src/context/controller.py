# Python imports
import subprocess, time


# Gtk imports
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib

# Application imports
from .mixins.dummy_mixin import DummyMixin
from .controller_data import Controller_Data




class Controller(DummyMixin, Controller_Data):
    def __init__(self, _settings, args, unknownargs):
        self.setup_controller_data(_settings)
        self.window.show()
        self.print_hello_world() # A mixin method from the DummyMixin file


    def tear_down(self, widget=None, eve=None):
        time.sleep(event_sleep_time)
        Gtk.main_quit()


    @daemon_threaded
    def gui_event_observer(self):
        while True:
            time.sleep(event_sleep_time)
            event = event_system.consume_gui_event()
            if event:
                try:
                    sender_id, method_target, parameters = event
                    if sender_id:
                        method = getattr(self.__class__, "handle_gui_event_and_return_message")
                        GLib.idle_add(method, *(self, sender_id, method_target, parameters))
                    else:
                        method = getattr(self.__class__, method_target)
                        GLib.idle_add(method, *(self, *parameters,))
                except Exception as e:
                    print(repr(e))

    def handle_gui_event_and_return_message(self, sender, method_target, parameters):
        method = getattr(self.__class__, f"{method_target}")
        data   = method(*(self, *parameters))
        event_system.push_module_event([sender, None, data])

    def handle_file_from_ipc(self, path: str) -> None:
        print(f"Path From IPC: {path}")

    def on_global_key_release_controller(self, widget: type, event: type) -> None:
        """Handler for keyboard events"""
        keyname = Gdk.keyval_name(event.keyval).lower()
        if keyname.replace("_l", "").replace("_r", "") in ["control", "alt", "shift"]:
            if "control" in keyname:
                self.ctrl_down    = False
            if "shift" in keyname:
                self.shift_down   = False
            if "alt" in keyname:
                self.alt_down     = False


        mapping = self.keybindings.lookup(event)
        if mapping:
            getattr(self, mapping)()
            return True
        else:
            print(f"on_global_key_release_controller > key > {keyname}")
            print(f"Add logic or remove this from: {self.__class__}")



    def get_clipboard_data(self) -> str:
        proc    = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        retcode = proc.wait()
        data    = proc.stdout.read()
        return data.decode("utf-8").strip()

    def set_clipboard_data(self, data: type) -> None:
        proc = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        proc.stdin.write(data)
        proc.stdin.close()
        retcode = proc.wait()
