#!/usr/bin/python3
""" The Console CLI Code. """

import cmd

class MyCommand(cmd.Cmd):
    """ Begin Console CLI Function """
    def do_EOF(self, arg):
        """ Gracefully Ends The Program """
        print("")
        if arg:
            pass
        return True

# ALLOWs THE FUNC() TO RUN.
if __name__ == "__main__":
    MyCommand().cmdloop()
