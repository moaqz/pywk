import os
from commands.command import Command


class PWDCommand(Command):
    def execute(self, args: list[str]):
        if len(args) > 1:
            print("pwd: too many arguments")
            return

        cwd = os.getcwd()
        print(cwd)
