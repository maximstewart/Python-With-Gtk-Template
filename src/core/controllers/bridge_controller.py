# Python imports
import base64
import json

# Lib imports

# Application imports
from libs.event_factory import Event_Factory, App_Event_Types



class BridgeController:
    def __init__(self):

        self._setup_signals()
        self._subscribe_to_events()


    def _setup_signals(self):
        ...

    def _subscribe_to_events(self):
        event_system.subscribe("handle-bridge-event", self.handle_bridge_event)


    def handle_bridge_event(self, event_str: str):
        event = Event_Factory.create_event( **json.loads(event_str) )

        if isinstance(event, App_Event_Types.DisplayMessageEvent):
            match event.topic:
                case "alert":
                    message = base64.b64decode( event.message.encode() ).decode("utf-8")
                    logger.info(f"\nMessage Topic:  {event.topic}\nMessage Content:  {message}")
                case "error":
                    message = base64.b64decode( event.message.encode() ).decode("utf-8")
                    logger.info(message)
                case _:
                    ...
        elif isinstance(event, App_Event_Types.GenericEvent):
            match event.action:
                case "save":
                    event_system.emit(f"handle-file-event-{event.originator}", (event,))
                case "close":
                    event_system.emit(f"handle-file-event-{event.originator}", (event,))
                case "load_buffer":
                    event_system.emit(f"handle-file-event-{event.originator}", (event,))
                case "load_file":
                    event_system.emit(f"handle-file-event-{event.originator}", (event,))
                case "alert":
                    content = base64.b64decode( event.content.encode() ).decode("utf-8")
                    logger.info(f"\nEvent Action:  {event.action}\nEvent Content:  {content}")
                case _:
                    ...
