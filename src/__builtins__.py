# Python imports
import builtins
import threading
import sys

# Lib imports

# Application imports
from libs.db import DB
from libs.event_system import EventSystem
from libs.endpoint_registry import EndpointRegistry
from libs.keybindings import Keybindings
from libs.logger import Logger
from libs.settings_manager.manager import SettingsManager



# NOTE: Threads WILL NOT die with parent's destruction.
def threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target = fn, args = args, kwargs = kwargs, daemon = False)
        thread.start()
        return thread
    return wrapper

# NOTE: Threads WILL die with parent's destruction.
def daemon_threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target = fn, args = args, kwargs = kwargs, daemon = True)
        thread.start()
        return thread
    return wrapper



# NOTE: Just reminding myself we can add to builtins two different ways...
# __builtins__.update({"event_system": Builtins()})
builtins.app_name          = "<change_me>"

builtins.keybindings       = Keybindings()
builtins.event_system      = EventSystem()
builtins.endpoint_registry = EndpointRegistry()
builtins.settings_manager  = SettingsManager()
builtins.db                = DB()

settings_manager.load_settings()

builtins.settings          = settings_manager.settings
builtins.logger            = Logger(settings_manager.get_home_config_path(), \
                                    _ch_log_lvl=settings.debugging.ch_log_lvl, \
                                    _fh_log_lvl=settings.debugging.fh_log_lvl).get_logger()

builtins.threaded          = threaded_wrapper
builtins.daemon_threaded   = daemon_threaded_wrapper



def custom_except_hook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = custom_except_hook