# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports
from ...base_event import BaseEvent



class GenericEvent(BaseEvent):
    event_type: str = "generic"
