# Python-With-Gtk-Template
A template project for Python with Gtk applications.

### Requirements
* PyGObject (Gtk introspection library)
* pyxdg (Desktop ".desktop" file parser)
* setproctitle (Define process title to search and kill more easily)
* sqlmodel (SQL databases and is powered by Pydantic and SQLAlchemy)

### Note
There are a "\<change_me\>" strings and files that need to be set according to your app's name located at:
* \_\_builtins\_\_.py
* user_config/bin/app_name
* user_config/usr/share/app_name
* user_config/usr/share/app_name/icons/app_name.png
* user_config/usr/share/app_name/icons/app_name-64x64.png
* user_config/usr/share/applications/app_name.desktop


For the user_config, after changing names and files, copy all content to their respective destinations.
The logic follows Debian Dpkg packaging and its placement logic.
