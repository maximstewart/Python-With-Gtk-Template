# Python imports

# Lib imports
import gi
from gi.repository import GLib

# Application imports
from .custom_completion_providers.lsp_completion_provider import LSPCompletionProvider



class CompletionManager():
    def __init__(self, completer):
        super(CompletionManager, self).__init__()

        self._completor    = completer
        self._lsp_provider = LSPCompletionProvider()
        self._timeout_id   = None


    def request_completion(self):
        if self._timeout_id:
            GLib.source_remove(self._timeout_id)

        self._timeout_id = GLib.timeout_add(
            1000,
            self._process_request_completion
        )

    def _process_request_completion(self):
        print('hello')

        self._timeout_id = None
        return False

    def _do_completion(self):
        if self._completor.get_providers():
            self._mach_completion()
        else:
            self._start_completion()

    def _mach_completion(self):
        """
            Note: Use IF providers were added to completion...
        """
        self._completion.match(
            self._completion.create_context()
        )

    def _start_completion(self):
        """
            Note: Use IF NO providers have been added to completion...
        """
        self._completion.start(
            [
                self._lsp_provider
            ],
            self._completion.create_context()
        )

                                                                                                                                                  