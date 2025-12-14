# Python imports

# Lib imports

# Application imports
from .commands import *



class CommandSystem:
    def __init__(self):
        super(CommandSystem, self).__init__()

        self.data: list = ()


    def set_data(self, *args, **kwargs):
        self.data = (args, kwargs)

    def exec(self, command: str):
        if not command in globals(): return

        # method = getattr(self, command, None)
        method       = globals()[command]
        args, kwargs = self.data
        if kwargs:
            method.execute(*args, kwargs)
        else:
            method.execute(*args)
