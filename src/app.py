# Python imports
import signal
import os

# Lib imports

# Application imports
from utils.debugging import debug_signal_handler
from utils.ipc_server import IPCServer
from core.window import Window



class AppLaunchException(Exception):
    ...


class Application(IPCServer):
    """ docstring for Application. """

    def __init__(self, args, unknownargs):
        super(Application, self).__init__()

        if not settings_manager.is_trace_debug():
            self.socket_realization_check()

            if not self.is_ipc_alive:
                for arg in unknownargs + [args.new_tab,]:
                    if os.path.isfile(arg):
                        message = f"FILE|{arg}"
                        self.send_ipc_message(message)

                raise AppLaunchException(f"{app_name} IPC Server Exists: Will send path(s) to it and close...")

        self.setup_debug_hook()
        Window(args, unknownargs)


    def socket_realization_check(self):
        try:
            self.create_ipc_listener()
        except Exception:
            self.send_test_ipc_message()

        try:
            self.create_ipc_listener()
        except Exception as e:
            ...

    def setup_debug_hook(self):
        try:
            # kill -SIGUSR2 <pid> from Linux/Unix or SIGBREAK signal from Windows
            signal.signal(
                vars(signal).get("SIGBREAK") or vars(signal).get("SIGUSR1"),
                debug_signal_handler
            )
        except ValueError:
            # Typically: ValueError: signal only works in main thread
            ...
