# AGENTS.md - LSP Manager Plugin

## Project Overview

This is a Newton editor plugin providing LSP (Language Server Protocol) code completion via WebSocket. Written in Python using GTK3/GtkSource.

## Build/Lint/Test Commands

### Running Tests

```bash
# Run all websocket library tests
python -m unittest discover -s libs/websocket/tests

# Run a single test file
python -m unittest libs.websocket.tests.test_websocket

# Run a single test
python -m unittest libs.websocket.tests.test_websocket.WebSocketTest.test_default_timeout
```

### Environment

- Python 3.x
- GTK 3.0 with GtkSource 4
- No build system (pyproject.toml/setup.py) - direct execution

## Code Style Guidelines

### Import Organization

Always use three-section ordering:
```python
# Python imports
import json
from os import path

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '4')
from gi.repository import Gtk

# Application imports
from libs.event_factory import Event_Factory
from plugins.plugin_types import PluginCode
from .lsp_manager import LSPManager
```

### Formatting

- 4-space indentation
- Line length: ~100 chars (soft limit)
- No trailing whitespace
- Use f-strings for string formatting: `f"{variable} text"`

### Naming Conventions

- **Classes**: PascalCase (`LSPManager`, `ProviderResponseCache`)
- **Methods/functions**: snake_case (`create_client`, `load_lsp_servers_config`)
- **Private members**: leading underscore (`_setup_styling`, `_init_params`)
- **Constants**: SCREAMING_SNAKE_CASE

### Type Hints

- Use Python 3.x type hints
- Common types: `str`, `int`, `dict`, `list`, `bool`
- For untyped parameters, use `any`:
  ```python
  def execute(view: any, *args, **kwargs)
  ```

### Error Handling

- Use try/except blocks with specific exception types
- Use `logger.error()` for logging errors with context
- Return early on failure conditions:
  ```python
  if not lang_id: return
  if not lang_id in self.servers_config: return
  ```

### Class Structure

```python
class LSPManager(Gtk.Dialog):
    def __init__(self):
        super(LSPManager, self).__init__()
        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._load_widgets()

    def _setup_styling(self):
        ...

    def _setup_signals(self):
        ...
```

### GTK Patterns

- Use `gi.require_version()` before importing GTK modules
- Use `GLib.idle_add()` for deferred UI updates
- Connect signals with `widget.connect("signal_name", handler)`

### Empty Methods

Use ellipsis for stub/placeholder methods:
```python
def _subscribe_to_events(self):
    ...
```

### Logging

- Import `logger` from application (available globally)
- Use `logger.debug()`, `logger.error()` for appropriate levels
- Include context in error messages:
  ```python
  logger.error( f"LSP Controller: {_LSP_INIT_CONFIG}\n\t\t{repr(e)}" )
  ```

### Inheritance Patterns

```python
class Provider(GObject.GObject, GtkSource.CompletionProvider):
    __gtype_name__ = 'LSPProvider'

    def do_get_name(self):
        return "LSP Code Completion"
```

### Testing Patterns (websocket library)

- Use `unittest.TestCase`
- Skip tests with decorators:
  ```python
  @unittest.skipUnless(TEST_WITH_INTERNET, "Internet-requiring tests are disabled")
  def test_remote(self):
      ...
  ```
- Environment variables for test configuration:
  - `TEST_WITH_INTERNET=1` - enable internet tests
  - `LOCAL_WS_SERVER_PORT=9999` - enable local server tests

### File Organization

- Main plugin: `plugin.py`
- Core logic: `lsp_manager.py`, `provider.py`, `provider_response_cache.py`
- Controllers: `controllers/` directory
- Config: `configs/` directory
- Embedded libs: `libs/websocket/`

### Anti-Patterns to Avoid

- Avoid bare `except:` - use specific exceptions
- Avoid global mutable state where possible
- Don't commit secrets or credentials
