#!/usr/bin/python3

# Python imports
import argparse
import faulthandler
import traceback
from setproctitle import setproctitle

import tracemalloc
tracemalloc.start()


# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from __builtins__ import *
from app import Application


if __name__ == "__main__":
    ''' Set process title, get arguments, and create GTK main thread. '''

    try:
        setproctitle('<change_me>')
        faulthandler.enable()  # For better debug info

        parser = argparse.ArgumentParser()
        # Add long and short arguments
        parser.add_argument("--debug", "-d", default="false", help="Do extra console messaging.")
        parser.add_argument("--trace-debug", "-td", default="false", help="Disable saves, ignore IPC lock, do extra console messaging.")
        parser.add_argument("--file", "-f", default="default", help="JUST SOME FILE ARG.")

        # Read arguments (If any...)
        args, unknownargs = parser.parse_known_args()

        Application(args, unknownargs)
        Gtk.main()
    except Exception as e:
        traceback.print_exc()
        quit()
