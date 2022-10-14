# Python imports
import os
import time

# Lib imports

# Application imports
from utils.ipc_server import IPCServer
from utils.settings import Settings
from core.window import Window



class AppLaunchException(Exception):
    ...

class ControllerStartExceptiom(Exception):
    ...


class Application(IPCServer):
    ''' Create Settings and Controller classes. Bind signal to Builder. Inherit from Builtins to bind global methods and classes.'''

    def __init__(self, args, unknownargs):
        super(Application, self).__init__()
        if args.debug == "true":
            settings.set_debug(True)

        if args.trace_debug == "true":
            settings.set_trace_debug(True)

        if not settings.is_trace_debug():
            self.create_ipc_listener()
            time.sleep(0.05)

            if not self.is_ipc_alive:
                if unknownargs:
                    for arg in unknownargs:
                        if os.path.isdir(arg):
                            message = f"FILE|{arg}"
                            self.send_ipc_message(message)

                raise AppLaunchException(f"IPC Server Exists: Will send path(s) to it and close...\nNote: If no fm exists, remove /tmp/{app_name}-ipc.sock")

        Window(args, unknownargs)
