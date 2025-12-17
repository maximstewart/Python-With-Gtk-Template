# Python imports

# Lib imports

# Application imports
from . import commands



class CommandSystem:
    def __init__(self):
        super(CommandSystem, self).__init__()

        self.data: list = ()


    def set_data(self, *args, **kwargs):
        self.data = (args, kwargs)

    def exec(self, command: str):
        if not hasattr(commands, command): return
        method = getattr(commands, command)

        args, kwargs = self.data
        if kwargs:
            method.execute(*args, kwargs)
        else:
            method.execute(*args)

    def exec_with_args(self, command: str, args: list):
        if not hasattr(commands, command): return

        method = getattr(commands, command)
        method.execute(*args)
