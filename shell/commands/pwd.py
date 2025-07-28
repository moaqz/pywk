from commands.command import Command
from pathlib import Path


class PWDCommand(Command):
    def __init__(self, shell):
        self._shell = shell

    def execute(self, args: list[str]):
        if len(args) > 1:
            print("pwd: too many arguments")
            return

        cwd: Path = self._shell.get_cwd()
        print(cwd.expanduser())
