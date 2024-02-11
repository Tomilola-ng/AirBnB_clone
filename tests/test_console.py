#!/usr/bin/python3
""" MY TESTCASE FOR THE CONSOLE """

import io
import unittest
from ..console import MyCommand
from contextlib import redirect_stdout

class TestMyCommand(unittest.TestCase):
    """ TESTCASE FOR MY MAIN COMMAND """

    def test_do_sayHello(self):
        """Tests that the do_sayHello method prints the correct message."""
        my_command = MyCommand()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            my_command.do_sayHello("")
        output = captured_output.getvalue()
        self.assertEqual(output, "Hello there :)\n")

    def test_do_EOF(self):
        """Tests that the do_EOF method prints a message and terminates."""
        my_command = MyCommand()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.assertTrue(my_command.do_EOF(""))
        output = captured_output.getvalue()
        self.assertEqual(output, "\n")

    def test_emptyline(self):
        """Tests that the emptyline method prints a default message."""
        my_command = MyCommand()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            my_command.emptyline()
        output = captured_output.getvalue()
        self.assertEqual(output, "Empty Line Command\n")

    def test_default(self):
        """Tests that the default method prints an error message."""
        my_command = MyCommand()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            my_command.default("invalid_command")
        output = captured_output.getvalue()
        self.assertEqual(output, "Invalid Command: invalid_command\n")

if __name__ == "__main__":
    unittest.main()
