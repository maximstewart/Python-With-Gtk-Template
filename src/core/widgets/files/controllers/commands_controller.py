# Python imports

# Lib imports

# Application imports
from libs.controllers.controller_base import ControllerBase

from libs.event_factory import Files_Event_Types

from ..command_system import FilesViewCommandSystem



class CommandsController(ControllerBase, list):
    def __init__(self):
        super(CommandsController, self).__init__()


    def _controller_message(self, event: Files_Event_Types.FilesEvent):
        if isinstance(event, Files_Event_Types.CreateCommandSystemEvent):
            event.response = self.create_command_system()

    def create_command_system(self):
        command_system         = FilesViewCommandSystem()
        command_system.emit    = self.emit
        command_system.emit_to = self.emit_to

        self.append(command_system)

        return command_system

    def remove_command_system(self, event: Files_Event_Types.RemovedFilesViewEvent):
        self.remove(event.view.command)
