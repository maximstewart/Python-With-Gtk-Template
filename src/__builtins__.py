import builtins

class Builtins:
    def hello_world():
        print("Hello, world!")

    def hello_user():
        print("Hello, user!")


   # NOTE: There areto ways to add global items. like so.
    builtins.hello_user = hello_user
    __builtins__.update({"hello_world": hello_world})
