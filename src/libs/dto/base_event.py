# Python imports
from dataclasses import dataclass, field

# Lib imports

# Application imports



@dataclass(slots = True)
class BaseEvent:
    event_type: str   = "base"
    action: str       = ""
    content: any      = None
    raw_content: any  = None
    success: callable = None
    fail: callable    = None
