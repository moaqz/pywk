from pathlib import Path
from enum import Enum

from commands.builtins import BuiltInCommands
from commands.type import command_type
from commands.pwd import command_pwd


class SpecialDirectory(Enum):
    PARENT = ".."
    CURRENT = "."
    HOME = "~"


class Shell:
    _pwd: Path

    def __init__(self) -> None:
        self._pwd = Path()
        self._commands = {
            "type": command_type,
            "pwd": command_pwd,
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
                    if cmd == BuiltInCommands.EXIT.value:
                        break

                    fn = self._commands.get(cmd)
                    if fn is not None:
                        fn(args)
                else:
                    print(f"{cmd}: command not found")

        except EOFError:
            print("")
            return

    def _build_prompt(self) -> str:
        if self._pwd == Path.home():
            return f"{SpecialDirectory.HOME.value}$"

        return f"{self._pwd}$"

    def _is_command_builtin(self, cmd: str) -> bool:
        try:
            BuiltInCommands(cmd)
            return True
        except ValueError:
            return False
