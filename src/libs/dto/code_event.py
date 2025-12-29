# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports
from .observable_event import ObservableEvent



@dataclass
class CodeEvent(ObservableEvent):
    etype: str  = ""
    view: any   = None
    file: any   = None
    buffer: any = None