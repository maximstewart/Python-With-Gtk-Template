# Python imports

# Lib imports

# Application imports
from plugins import plugins_controller

from libs.controllers.controller_manager import ControllerManager

from .controllers.files_session_controller import FilesSessionController
from .controllers.commands_controller import CommandsController
from .controllers.tab_views_controller import TabViewsController



class FilesBase:
    def __init__(self):
        super(FilesBase, self).__init__()

        self.controller_manager: ControllerManager = ControllerManager()

        self._subscribe_to_events()
        self._load_controllers()


    def _subscribe_to_events(self):
        event_system.subscribe("handle-file", self._load_ipc_file)
        event_system.subscribe("handle-files", self._load_ipc_files)

    def _load_controllers(self):
        files_session_controller = FilesSessionController()
        # commands_controller      = CommandsController() # Uncomment if not used with 'code' widget
        tab_views_controller     = TabViewsController()

        self.controller_manager.register_controller("files_session", files_session_controller)
        # self.controller_manager.register_controller("commands", commands_controller)
        self.controller_manager.register_controller("tab_views", tab_views_controller)
        # self.controller_manager.register_controller("widgets", widget_registery)

    def create_sessioned_tabs_view(self):
        return self.controller_manager["files_session"].create_tabs_view()

    def create_tabs_view(self):
        return self.controller_manager["tab_views"].create_tabs_view()

    def _load_ipc_file(self, fpath: str):
        active_view = self.controller_manager["tab_views"].get_active_tabs_view()
        uris        = [ f"file://{fpath}" ]
        # active_view._on_uri_data_received(uris)
        pass

    def _load_ipc_files(self, uris: list):
        active_view = self.controller_manager["tab_views"].get_active_tabs_view()
        # active_view._on_uri_data_received(uris)
