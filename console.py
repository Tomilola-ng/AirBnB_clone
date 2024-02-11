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
        """ Print default, when no arguments """
        print('Empty Line Command')

    def default(self, line):
        """ Gracefully Catch Error or Unknown Commands """
        print(f'Invalid Command: {line}')

# ALLOWs THE FUNC() TO RUN.
if __name__ == "__main__":
    MyCommand().cmdloop()
