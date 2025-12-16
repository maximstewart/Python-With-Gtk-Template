# Python imports

# Lib imports

# Application imports
from .source_file import SourceFile
from .source_buffer import SourceBuffer



class SourceFilesManager(list):
    def __init__(self):
        super(SourceFilesManager, self).__init__()


    def new(self):
        file = SourceFile()
        super().append(file)

        return file

    def append(self, file: SourceFile):
        if not file: return

        super().append(file)

    def get_file(self, buffer: SourceBuffer):
        if not buffer: return

        for i, file in enumerate(self):
            if not buffer == file.buffer: continue
            return file

    def pop_file(self, buffer: SourceBuffer):
        if not buffer: return

        for i, file in enumerate(self):
            if not buffer == file.buffer: continue

            popped_file  = self.pop(i)
            sibling_file = None
            if len(self) == 0:
                sibling_file = self.new()
            else:
                sibling_file = self[ i - 1 if i > 0 else i + 1]

            return sibling_file, popped_file

    def remove_file(self, buffer: SourceBuffer):
        if not buffer: return

        for file in self:
            if not buffer == file.buffer: continue
            self.remove(file)

            file.close()
            del file
            break
