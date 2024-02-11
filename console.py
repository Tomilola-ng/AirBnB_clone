#!/usr/bin/python3
""" The Console CLI Code. """

import cmd

class MyCommand(cmd.Cmd):
    """ Begin Console CLI Function """

    def do_sayHello(self, line):
        """ Say Basicly Hello """
        print("Hello there :)")

    def do_EOF(self, line):
        """ Gracefully Ends The Program """
        print()
        return True

    def emptyline(self):
        """ Ignore this request, when no arguments """
        pass

    def default(self, line):
        """ Gracefully Catch Errors """
        print(f'Invalid Command: {line}')

# ALLOWs THE FUNC() TO RUN.
if __name__ == "__main__":
    MyCommand().cmdloop()
