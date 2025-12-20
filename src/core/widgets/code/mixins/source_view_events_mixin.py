# Python imports

# Lib imports

# Application imports



class SourceViewEventsMixin:
    def _focus_in_event(self, view, eve):
        self.command.exec("set_miniview")
        self.command.exec("set_focus_border")
        self.command.exec("update_info_bar")

    def _move_cursor(self, view, step, count, extend_selection):
        self.command.exec("update_info_bar")

    def _button_press_event(self, view, eve):
        self.command.exec("update_info_bar")

    def _button_release_event(self, view, eve):
        self.command.exec("update_info_bar")

    def _key_press_event(self, view, eve):
        command = self.key_mapper._key_press_event(eve)
        if not command: return False

        self.command.exec(command)
        return True

    def _key_release_event(self, view, eve):
        command = self.key_mapper._key_release_event(eve)
        if not command: return False

        self.command.exec(command)
        return True

    def notify(self, file, buffer, etype: str):
        has_focus = self.command.exec("has_focus")
        if not has_focus: return

        self.command.exec("update_info_bar")
        match etype:
            case "changed":
                logger.debug("SourceFile._changed")
            case "modified_changed":
                logger.debug("SourceFile._modified_changed")
            case "insert_text":
                logger.debug("SourceFile._insert_text")
            case "mark_set":
                # logger.debug("SourceFile._mark_set")
                ...
            case _:
                ...

