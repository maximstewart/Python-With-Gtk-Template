# Python imports

# Lib imports

# Application imports
from libs.event_factory import Event_Factory, Files_Event_Types
from libs.command_system import CommandSystem

from ..tabs_view import TabsView


from . import commands



class FilesViewCommandSystem(CommandSystem):
    def __init__(self):
        super(FilesViewCommandSystem, self).__init__(commands)


    def toggle_plugins_ui(self):
        event = Event_Factory.create_event( "toggle_plugins_ui" )

        self.emit_to("plugins", event)

    def emit(self, event: Files_Event_Types.FilesEvent):
        """ Monkey patch 'emit' from command controller... """
        ...

    def emit_to(self, controller: str, event: Files_Event_Types.FilesEvent):
        """ Monkey patch 'emit_to' from command controller... """
        ...
