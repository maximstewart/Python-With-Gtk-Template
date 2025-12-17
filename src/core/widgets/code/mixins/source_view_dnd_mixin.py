# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio

# Application imports



class SourceViewDnDMixin:

    def _set_up_dnd(self):
        PLAIN_TEXT_TARGET_TYPE = 70
        URI_TARGET_TYPE        = 80
        text_target        = Gtk.TargetEntry.new('text/plain', Gtk.TargetFlags(0), PLAIN_TEXT_TARGET_TYPE)
        uri_target         = Gtk.TargetEntry.new('text/uri-list', Gtk.TargetFlags(0), URI_TARGET_TYPE)
        targets            = [ text_target, uri_target ]
        self.drag_dest_set_target_list(targets)

    def _on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        if info == 70: return

        if info == 80:
            uris   = data.get_uris()
            buffer = self.get_buffer()
            file   = self.files.get_file(buffer)

            if len(uris) == 0:
                uris = data.get_text().split("\n")

            if file.ftype == "buffer":
                gfile = Gio.File.new_for_uri(uris[0])
                self.command.exec_with_args(
                    "load_file",
                    (self, gfile, file)
                )

                self.command.exec("update_info_bar")
                uris.pop(0)

            for uri in uris:
                try:
                    gfile = Gio.File.new_for_uri(uri)
                except Exception as e:
                    gfile = Gio.File.new_for_path(uri)

                self.command.exec_with_args("load_file", (self, gfile))
