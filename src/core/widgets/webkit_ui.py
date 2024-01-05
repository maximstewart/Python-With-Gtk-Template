

# Python imports

# Lib imports
import gi
gi.require_version('Gdk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gdk
from gi.repository import WebKit2

# Application imports



class WebkitUI(WebKit2.WebView):
    def __init__(self):
        super(WebkitUI, self).__init__()

        self._setup_styling()
        self._subscribe_to_events()
        self._load_view()
        self._setup_content_manager()
        
        self.show_all()


    def _setup_styling(self):
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_background_color( Gdk.RGBA(0, 0, 0, 0.0) )

    def _subscribe_to_events(self):
        # event_system.subscribe("handle_file_from_ipc", self.handle_file_from_ipc)
        ...
    
    def _load_settings(self):
        self.set_settings( WebkitUISettings() )

    def _load_view(self):
        path = settings_manager.get_context_path()
        data = settings_manager.wrap_html_to_body("")
        self.load_html(content = data, base_uri = f"file://{path}/")

    def _setup_content_manager(self):
        content_manager = self.get_user_content_manager()
        content_manager.register_script_message_handler("backend")
        content_manager.connect("script-message-received", self._process_js_message)

    def _process_js_message(self, user_content_manager, js_result):
        js_value = js_result.get_js_value()
        print(js_value.to_string())
        # self._web_view.run_javascript("do_stuff()", None, None)


class WebkitUISettings(WebKit2.Settings):
    def __init__(self):
        super(WebkitUISettings, self).__init__()
        
        self._set_default_settings()


    # Note: Highly insecure setup but most "app" like setup I could think of.
    #       Audit heavily any scripts/links ran/clicked under this setup! 
    def _set_default_settings(self):
        self.set_enable_offline_web_application_cache(False)
        self.enable_html5_local_storage(False)
        self.enable_html5_database(False)
        self.enable_xss_auditor(False)
        self.set_enable_hyperlink_auditing(False)
        self.set_enable_tabs_to_links(False)
        self.enable_fullscreen(False)
        self.set_print_backgrounds(False)
        self.enable_webaudio(False)
        self.set_enable_page_cache(False)

        self.enable_accelerated_2d_canvas(True)
        self.set_allow_file_access_from_file_urls(True)
        self.set_allow_universal_access_from_file_urls(True)
        self.set_enable_webrtc(True)

        sdelf.set_user_agent(f"{app_name}")