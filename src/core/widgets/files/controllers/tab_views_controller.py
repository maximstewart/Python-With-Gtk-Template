# Python imports

# Lib imports

# Application imports
from libs.controllers.controller_base import ControllerBase
from libs.event_factory import Event_Factory, Files_Event_Types

from ..tabs_view import TabsView
from ..tab_dto import TabDTO



class TabViewsController(ControllerBase, list):
    def __init__(self):
        super(TabViewsController, self).__init__()

        self.active_view: int = 0


    def _controller_message(self, event: Files_Event_Types.FilesEvent):
        if isinstance(event, Files_Event_Types.CreateFilesViewEvent):
            ...

    def _get_command_system(self):
        event   = Event_Factory.create_event("create_command_system")
        self.message_to("commands", event)
        command = event.response

        del event
        return command

    def create_tabs_view(self) -> TabsView:
        tabs_view = TabsView()

        tabs_view.command = self._get_command_system()

        self.append(tabs_view)
        self.active_view = len(self)

        return tabs_view

    def set_active_tabs_view(self, i: int):
        if i < 0:
            i = len(self)
        elif i > len(self):
            i = 0

        self.active_view = i

    def get_active_tabs_view(self) -> TabsView:
        return self.get(i)

    def get_tabs_view(self, i: int = 0) -> TabsView:
        if i < 0:
            i = len(self)
        elif i > len(self):
            i = 0

        return self.get(i)

    def create_new_tab(self, name: str, tabs_view: TabsView = None) -> TabDTO:
        if not name:
            logger.error("Must give a Tab 'name' to create new tab...")
            return

        if not tabs_view:
            tabs_view = self.get_active_tabs_view()

        return tabs_view.create_new_tab(name)
