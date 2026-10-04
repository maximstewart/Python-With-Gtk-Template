# Python imports
from dataclasses import dataclass

# Lib imports

# Application imports
from .files_event import FilesEvent
from libs.dto.states.source_view_states import SourceViewStates



@dataclass
class RemoveFilesViewEvent(FilesEvent):
    ...
