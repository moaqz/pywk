from pathlib import Path
import subprocess


from commands.builtins import BuiltInCommands
from commands.type import TypeCommand
from commands.pwd import PWDCommand
from commands.exit import ExitCommand
from commands.command import Command
from commands.cd import CDCommand
from utils.directories import SpecialDirectory
from utils.find_command import find_command, CommandNotFound


class Shell:
    def __init__(self) -> None:
        self._cwd = Path.home()
        self._commands: dict[str, Command] = {
            "type": TypeCommand(),
            "pwd": PWDCommand(self),
            "exit": ExitCommand(),
            "cd": CDCommand(self),
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
                    self._exec_external_command(cmd, args)

        except EOFError:
            print("")
            return

    def _exec_external_command(self, cmd: str, args: list[str]) -> None:
        try:
            cmd_path = find_command(cmd)
            result = subprocess.run(
                [cmd_path, *args], capture_output=True, text=True, cwd=self._cwd
            )

            # Use end="" to prevent adding extra newline to command output
            if result.stdout:
                print(result.stdout, end="")
            if result.stderr:
                print(result.stderr, end="")

        except CommandNotFound:
            print(f"{cmd}: command not found")

    def _build_prompt(self) -> str:
        home_path = Path.home()

        if self._cwd == home_path:
            return f"{SpecialDirectory.HOME.value}$"
        elif self._cwd.is_relative_to(home_path):
            relative_path = self._cwd.relative_to(home_path)
            return f"{SpecialDirectory.HOME.value}/{relative_path}$"
        else:
            return f"{self._cwd}$"

    def _is_command_builtin(self, cmd: str) -> bool:
        try:
            BuiltInCommands(cmd)
            return True
        except ValueError:
            return False

    def set_cwd(self, src_path: Path) -> None:
        self._cwd = src_path

    def get_cwd(self) -> Path:
        return self._cwd
