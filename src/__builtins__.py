class Builtins:
    def hello_world():
        print("Hello, world!")


    __builtins__.update({"hello_world": hello_world})
