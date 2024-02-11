#!/usr/bin/python3
""" The Console CLI Code. """

import cmd

class MyCommand(cmd.Cmd):
    """ Begin Console CLI Function """

    def do_EOF(self, line):
        """ Gracefully Ends The Program """
        print()
        return True
    
    def do_sayHello(self, line):
        """ Gracefully Ends The Program """
        print("Hello there :)")

    # def do_EOF(self, line_arg):
    #     """ Gracefully Ends The Program """
    #     print()
    #     return True

    def default(self, line):
        """ Gracefully Catch Errors """
        print(f'Invalid Command: {line}')

# ALLOWs THE FUNC() TO RUN.
if __name__ == "__main__":
    MyCommand().cmdloop()
