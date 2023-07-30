# Python imports
import os
import subprocess

# Lib imports

# Application imports
from plugins.plugins_controller import PluginsController



class ControllerData:
    ''' ControllerData contains most of the state of the app at ay given time. It also has some support methods. '''

    def setup_controller_data(self) -> None:
        self.window      = settings_manager.get_main_window()
        self.builder     = None
        self.base_container   = None
        self.was_midified_key = False
        self.ctrl_down   = False
        self.shift_down  = False
        self.alt_down    = False

        self.setup_builder_and_container()
        self.plugins     = PluginsController()


    def clear_console(self) -> None:
        ''' Clears the terminal screen. '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def call_method(self, _method_name: str, data: type) -> type:
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
        return method(*data) if data else method()

    def has_method(self, obj: type, method: type) -> type:
        ''' Checks if a given method exists. '''
        return callable(getattr(obj, method, None))

    def clear_children(self, widget: type) -> None:
        ''' Clear children of a gtk widget. '''
        for child in widget.get_children():
            widget.remove(child)

    def get_clipboard_data(self, encoding="utf-8") -> str:
        proc    = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        retcode = proc.wait()
        data    = proc.stdout.read()
        return data.decode(encoding).strip()

    def set_clipboard_data(self, data: type, encoding="utf-8") -> None:
        proc = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        proc.stdin.write(data.encode(encoding))
        proc.stdin.close()
        retcode = proc.wait()
