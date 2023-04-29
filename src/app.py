# Python imports
import signal
import os

# Lib imports

# Application imports
from utils.ipc_server import IPCServer
from core.window import Window



# Break into a Python console upon SIGUSR1 (Linux) or SIGBREAK (Windows:
# CTRL+Pause/Break).  To be included in all production code, just in case.
def debug_signal_handler(signal, frame):
    del signal
    del frame

    try:
        import rpdb2
        logger.debug("\n\nStarting embedded RPDB2 debugger. Password is 'foobar'\n\n")
        rpdb2.start_embedded_debugger("foobar", True, True)
        rpdb2.setbreak(depth=1)
        return
    except StandardError:
        pass

    try:
        import code
        code.interact()
    except StandardError as ex:
        logger.debug(f"{ex}, returning to normal program flow...")



class AppLaunchException(Exception):
    ...


class Application(IPCServer):
    """ docstring for Application. """

    def __init__(self, args, unknownargs):
        super(Application, self).__init__()

        if not settings.is_trace_debug():
            try:
                self.create_ipc_listener()
            except Exception:
                ...

            if not self.is_ipc_alive:
                for arg in unknownargs + [args.new_tab,]:
                    if os.path.isfile(arg):
                        message = f"FILE|{arg}"
                        self.send_ipc_message(message)

                raise AppLaunchException(f"{app_name} IPC Server Exists: Will send path(s) to it and close...")

        try:
            signal.signal(
                    vars(signal).get("SIGBREAK") or vars(signal).get("SIGUSR1"),
                    debug_signal_handler
                    )
        except ValueError:
            # Typically: ValueError: signal only works in main thread
            ...

        Window(args, unknownargs)
