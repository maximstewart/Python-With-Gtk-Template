# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports
from ...base_event import BaseEvent



class DisplayMessageEvent(BaseEvent):
    topic: str   = None
    message: str = None
