# Python imports

# Lib imports

# Application imports
from libs.controllers.controller_base import ControllerBase
from libs.event_factory import Event_Factory, Files_Event_Types




class FilesSessionController(ControllerBase, list):
    def __init__(self):
        super(FilesSessionController, self).__init__()


    def _controller_message(self, event: Files_Event_Types.FilesEvent):
        if isinstance(event, Files_Event_Types.AddNewFileEvent):
            ...

    def create_tabs_view(self) -> TabsView:
        tabs_view = TabsView()
        self.add(tabs_view)

        self.active_view = self.length

        return tabs_view
