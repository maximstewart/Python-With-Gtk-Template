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

    def remove_file(self, buffer: SourceBuffer):
        if not buffer: return

        for file in self:
            if not buffer == file.buffer: continue
            self.remove(file)

            file.close()
            del file
            break
