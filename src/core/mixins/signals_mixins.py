# Python imports

# Lib imports

# Application imports
from .signals.ipc_signals_mixin import IPCSignalsMixin
from .signals.keyboard_signals_mixin import KeyboardSignalsMixin




class SignalsMixins(KeyboardSignalsMixin, IPCSignalsMixin):
    ...
