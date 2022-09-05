# Python imports
import os, inspect, time

# Lib imports

# Application imports
from __builtins__ import *
from utils.ipc_server import IPCServer
from utils.settings import Settings
from context.controller import Controller


class App_Launch_Exception(Exception):
    ...

class Controller_Start_Exceptio(Exception):
    ...


class Application(IPCServer):
    ''' Create Settings and Controller classes. Bind signal to Builder. Inherit from Builtins to bind global methods and classes.'''

    def __init__(self, args, unknownargs):
        super(Application, self).__init__()

        if not trace_debug:
            self.create_ipc_listener()
            time.sleep(0.05)

            if not self.is_ipc_alive:
                if unknownargs:
                    for arg in unknownargs:
                        if os.path.isdir(arg):
                            message = f"FILE|{arg}"
                            self.send_ipc_message(message)

                raise App_Launch_Exception(f"IPC Server Exists: Will send path(s) to it and close...\nNote: If no fm exists, remove /tmp/{app_name}-ipc.sock")


        settings = Settings()
        settings.create_window()

        controller = Controller(settings, args, unknownargs)
        if not controller:
            raise Controller_Start_Exceptio("Controller exited and doesn't exist...")

        # Gets the methods from the classes and sets to handler.
        # Then, builder from settings will connect to any signals it needs.
        classes  = [controller]
        handlers = {}
        for c in classes:
            methods = None
            try:
                methods = inspect.getmembers(c, predicate=inspect.ismethod)
                handlers.update(methods)
            except Exception as e:
                print(repr(e))

        settings.get_builder().connect_signals(handlers)
