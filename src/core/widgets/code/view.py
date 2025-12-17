# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '4')

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GtkSource

# Application imports
from .mixins.source_view_dnd_mixin import SourceViewDnDMixin

from .source_files_manager import SourceFilesManager
from .completion_manager import CompletionManager
from .command_system import CommandSystem
from .key_mapper import KeyMapper



class SourceView(SourceViewDnDMixin, GtkSource.View):
    def __init__(self):
        super(SourceView, self).__init__()

        self.sibling_right = None
        self.sibling_left  = None
        self.key_mapper    = KeyMapper()

        self._setup_styles()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()


    def _setup_styles(self):
        ctx = self.get_style_context()
        ctx.add_class("source-view")

        self.set_vexpand(True)
        self.set_bottom_margin(800)

        self.set_show_line_marks(True)
        self.set_show_line_numbers(True)
        self.set_smart_backspace(True)
        self.set_indent_on_tab(True)
        self.set_insert_spaces_instead_of_tabs(True)
        self.set_auto_indent(True)
        self.set_monospace(True)
        self.set_tab_width(4)
        self.set_show_right_margin(True)
        self.set_right_margin_position(80)
        self.set_background_pattern(0) # 0 = None, 1 = Grid
        self.set_highlight_current_line(True)

    def _setup_signals(self):
        self.map_id =  self.connect("map", self._init_map)

        self.connect("drag-data-received", self._on_drag_data_received)
        self.connect("focus-in-event", self._focus_in_event)
        self.connect("key-press-event", self._key_press_event)
        self.connect("key-release-event", self._key_release_event)
        self.connect("button-press-event", self._button_press_event)
        self.connect("button-release-event", self._button_release_event)

    def _subscribe_to_events(self):
        ...

    def _load_widgets(self):
        self._set_up_dnd()

    def _init_map(self, view):
        def _first_show_init():
            self.disconnect(self.map_id)
            del self.map_id

            self._handle_first_show()

            return False

        # GLib.timeout_add(1000, _first_show_init)
        GLib.idle_add(_first_show_init)

    def _handle_first_show(self):
        self.language_manager     = GtkSource.LanguageManager()
        self.style_scheme_manager = GtkSource.StyleSchemeManager()
        self.command              = CommandSystem()
        self.files                = SourceFilesManager()
        self.completion           = CompletionManager()

        self.command.set_data(self)
        self.completion.set_completer( self.get_completion() )

        self.style_scheme_manager.append_search_path(
            f"{settings_manager.get_home_config_path()}/code_styles"
        )
        self.syntax_theme = self.style_scheme_manager.get_scheme(
            f"{settings_manager.settings.theming.syntax_theme}"
        )

        self.exec_command("new_file")
        if self.sibling_right:
            self.grab_focus()


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
        self.command.exec("update_info_bar")

        command = self.key_mapper._key_press_event(eve)
        if not command: return False

        self.exec_command(command)
        return True

    def _key_release_event(self, view, eve):
        self.command.exec("update_info_bar")

        command = self.key_mapper._key_release_event(eve)
        if not command: return False

        self.exec_command(command)
        return True

    def exec_command(self, command: str):
        self.command.exec(command)
