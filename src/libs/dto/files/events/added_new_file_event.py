# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports
from .files_event import FilesEvent



@dataclass
class AddedNewFileEvent(FilesEvent):
    ...
