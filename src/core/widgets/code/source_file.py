# Python imports
import os

# Lib imports
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '4')

from gi.repository import Gtk
from gi.repository import GtkSource
from gi.repository import Gio

# Application imports
from .source_buffer import SourceBuffer



class SourceFile(GtkSource.File):
    def __init__(self):
        super(SourceFile, self).__init__()

        self.encoding: str        = "UTF-8"
        self.fname: str           = "buffer"
        self.fpath: str           = "buffer"
        self.ftype: str           = "buffer"

        self.buffer: SourceBuffer = SourceBuffer()

        self._set_signals()


    def load_path(self, gfile: Gio.File):
        if not gfile: return

        self.set_path(gfile)
        data = gfile.load_bytes()[0].get_data().decode("UTF-8")

        self.buffer.insert_at_cursor(data)

    def set_path(self, gfile: Gio.File):
        if not gfile: return
        self.set_location(gfile)

        self.fpath = gfile.get_path()
        self.fname = gfile.get_basename()

    def _set_signals(self):
        self.buffer.set_signals(
            self._changed,
            self._mark_set,
            self._insert_text,
            self._modified_changed
        )

    def _insert_text(
        self,
        buffer: SourceBuffer,
        location: Gtk.TextIter,
        text: str,
        length: int
    ):
        logger.info("SourceFile._insert_text")

    def _changed(self, buffer: SourceBuffer):
        logger.info("SourceFile._changed")

    def _mark_set(
        self,
        buffer: SourceBuffer,
        location: Gtk.TextIter,
        mark: Gtk.TextMark
    ):
        # logger.info("SourceFile._mark_set")
        ...

    def _modified_changed(self, buffer: SourceBuffer):
        logger.info("SourceFile._modified_changed")

    def _write_file(self, gfile: Gio.File):
        if not gfile: return

        with open(gfile.get_path(), 'w') as f:
            start_itr = self.buffer.get_start_iter()
            end_itr   = self.buffer.get_end_iter()
            text      = self.buffer.get_text(start_itr, end_itr, True)

            f.write(text)

        return gfile

    def save(self):
        self._write_file( self.get_location() )

    def save_as(self):
        file = event_system.emit_and_await("save-file-dialog")
        if not file: return

        self._write_file(file)
        self.set_path(file)

        return file

    def close(self):
        del self.buffer