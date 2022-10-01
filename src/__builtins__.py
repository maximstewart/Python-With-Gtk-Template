import builtins, threading

# Python imports
import builtins

# Lib imports

# Application imports
from utils.event_system import EventSystem
from utils.endpoint_registry import EndpointRegistry




# NOTE: Threads WILL NOT die with parent's destruction.
def threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=False).start()
    return wrapper

# NOTE: Threads WILL die with parent's destruction.
def daemon_threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper




# NOTE: Just reminding myself we can add to builtins two different ways...
# __builtins__.update({"event_system": Builtins()})
builtins.app_name          = "<change_me>"
builtins.event_system      = EventSystem()
builtins.endpoint_registry = EndpointRegistry()
builtins.threaded          = threaded_wrapper
builtins.daemon_threaded   = daemon_threaded_wrapper
builtins.event_sleep_time  = 0.05
builtins.trace_debug       = False
builtins.debug             = False
