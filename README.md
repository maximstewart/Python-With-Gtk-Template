# Python-With-Gtk-Template
A template project for Python with Gtk applications.

### Requirements
* PyGObject

### Note
There are several "\<change_me\>" strings that need to be set according to your app's name located at:
* \_\_builtins\_\_.py
* \_\_main\_\_.py
* user_config/usr/share/app_name

In addition, check the 'ipc_server.py' \_\_init\_\_ section to change the socket information.

For the user_config, traverse all the way down and copy the contents to either:
* /usr/share/\<your_app_name_as_all_lowercase\>
* /\<your_home_dir\>/.config/\<your_app_name_as_all_lowercase\>
