#!/usr/bin/python3
"shebang"
import cmd


class HBNBCommand(cmd.Cmd):
    "instantation"

    prompt = "(hbnb) "

    def do_help(self, arg):
        "help function"
        return super().do_help(arg)

    def do_EOF(self, line):
        "End Of Function"
        return True

    def do_quit(self, arg):
        "Quit function"
        return True

    def emptyline(self):
        "emptyline function"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
