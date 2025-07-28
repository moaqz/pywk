from pathlib import Path
from enum import Enum

from commands.builtins import BuiltInCommands
from commands.type import TypeCommand
from commands.pwd import PWDCommand
from commands.exit import ExitCommand
from commands.command import Command


class SpecialDirectory(Enum):
    PARENT = ".."
    CURRENT = "."
    HOME = "~"


class Shell:
    _pwd: Path

    def __init__(self) -> None:
        self._pwd = Path.home()
        self._commands: dict[str, Command] = {
            "type": TypeCommand(),
            "pwd": PWDCommand(),
            "exit": ExitCommand(),
        }

    def run(self):
        try:
            while True:
                line = input(f"{self._build_prompt()} ").strip()
                if not line:
                    continue

                parts = line.split(" ")
                cmd = parts[0]
                args = parts[1:] if len(line) > 1 else []

                if self._is_command_builtin(cmd):
                    command = self._commands.get(cmd)
                    if command is not None:
                        command.execute(args)

                else:
                    print(f"{cmd}: command not found")

        except EOFError:
            print("")
            return

    def _build_prompt(self) -> str:
        home_path = Path.home()

        if self._pwd == home_path:
            return f"{SpecialDirectory.HOME.value}$"
        elif self._pwd.is_relative_to(home_path):
            relative_path = self._pwd.relative_to(home_path)
            return f"{SpecialDirectory.HOME.value}/{relative_path}$"
        else:
            return f"{self._pwd}$"

    def _is_command_builtin(self, cmd: str) -> bool:
        try:
            BuiltInCommands(cmd)
            return True
        except ValueError:
            return False
