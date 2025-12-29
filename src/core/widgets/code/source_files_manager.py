# Python imports

# Lib imports

# Application imports
from libs.mixins.observable_mixin import ObservableMixin
from libs.singleton import Singleton
from libs.dto.code_event import CodeEvent

from .source_file import SourceFile
from .source_buffer import SourceBuffer



class SourceFilesManager(Singleton, list, ObservableMixin):
    def __init__(self):
        super(SourceFilesManager, self).__init__()

        self.observers = []


    def new(self):
        file = SourceFile()
        self.append(file)
        return file

    def append(self, file: SourceFile):
        if not file: return
        super().append(file)

        event       = CodeEvent()
        event.file  = file
        event.etype = "appended_file"

        self.notify_observers(event)

    def get_file(self, buffer: SourceBuffer):
        if not buffer: return

        for file in self:
            if not buffer == file.buffer: continue
            return file

    def pop_file(self, buffer: SourceBuffer):
        if not buffer: return

        for i, file in enumerate(self):
            if not buffer == file.buffer: continue

            popped_file  = self.pop(i)
            sibling_file = None
            size         = len(self)

            if size == 0:
                return popped_file, sibling_file

            j = 0 if size == 1 else i - 1 if i > 1 else i + 1
            sibling_file = self[j]

            event       = CodeEvent()
            event.file  = popped_file
            event.etype = "popped_file"

            self.notify_observers(event)

            return popped_file, sibling_file

    def swap_file(self, buffer: SourceBuffer):
        if not buffer: return

        for i, file in enumerate(self):
            if not buffer == file.buffer: continue

            swapped_file = self[i]
            sibling_file = None
            size         = len(self)

            if size == 0:
                return swapped_file, sibling_file

            j = 0 if size == 1 else i - 1 if i > 1 else i + 1
            sibling_file = self[j]

            return swapped_file, sibling_file

    def remove_file(self, buffer: SourceBuffer):
        if not buffer: return

        for i, file in enumerate(self):
            if not buffer == file.buffer: continue
            self.remove(file)

            event       = CodeEvent()
            event.file  = file
            event.etype = "removed_file"

            self.notify_observers(event)

            size = len(self)
            if size == 0:
                return None

            j = 0 if size == 1 else i - 1 if i > 1 else i + 1
            sibling_file = self[j]

            file.close()

            return sibling_file
