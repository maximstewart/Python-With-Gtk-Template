# Python imports

# Lib imports

# Application imports




class IPCSignalsMixin:
    """ IPCSignalsMixin handle messages from another starting solarfm process. """

    def print_to_console(self, message=None):
        logger.debug(message)

    def handle_file_from_ipc(self, path: str) -> None:
        logger.debug(f"File From IPC: {path}")

    def handle_dir_from_ipc(self, path: str) -> None:
        logger.debug(f"Dir From IPC: {path}")