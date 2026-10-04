# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports
from ...base_event import BaseEvent



@dataclass
class FilesEvent(BaseEvent):
    view: any      = None
    tab: any       = None
    response: any  = None
