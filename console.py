#!/usr/bin/python3
""" The Console CLI Code. """

import cmd

class MyCommand(cmd.Cmd):
    """ Begin Console CLI Function """
    def do_EOF(self, line_arg):
        """ Gracefully Ends The Program """
        print()
        return True

    def default(self, line_arg):
        """ Gracefully Catch Errors """
        print(f'Invalid Command: {line_arg}')

# ALLOWs THE FUNC() TO RUN.
if __name__ == "__main__":
    MyCommand().cmdloop()
