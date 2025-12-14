"""
    Commands Package
"""

import os


__all__ = [
    command.replace(".py", "") for command in os.listdir(
        os.path.dirname(__file__)
    ) if "__init__" not in command
]