# Python imports
from dataclasses import dataclass

# Lib imports

# Application imports
from .files_event import FilesEvent



@dataclass
class CreateFilesViewEvent(FilesEvent):
    ...
