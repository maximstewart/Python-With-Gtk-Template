# Python imports

# Lib imports

# Application imports
from .tab_header import TabHeader
from .files_view import FilesView
from .icon_grid import  IconGrid



class TabDTO:
    def __init__(self):
        super(TabDTO, self).__init__()

        self.tab_header: TabHeader = TabHeader()
        self.files_view: FilesView = FilesView()
        self.icon_grid: IconGrid   = IconGrid()

        self.files_view.bind_icon_grid(self.icon_grid)
