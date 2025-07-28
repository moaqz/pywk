from commands.command import Command
from utils.directories import SpecialDirectory
from pathlib import Path
import os


class CDCommand(Command):
    def __init__(self, shell):
        self._shell = shell

    def execute(self, args: list[str]):
        if len(args) > 1:
            print("cd: too many arguments")
            return

        cwd: Path = self._shell.get_cwd()
        if len(args) == 0:
            self._shell.set_cwd(Path.home())
            return

        target_dir = args[0]

        # Absolute path
        if target_dir.startswith("/"):
            dest_path = Path(target_dir)
            if self._can_change_directory(dest_path):
                self._shell.set_cwd(dest_path)
        elif target_dir == SpecialDirectory.HOME.value:
            self._shell.set_cwd(Path.home())
        elif target_dir == SpecialDirectory.PARENT.value:
            self._shell.set_cwd(cwd.parent)
        elif target_dir == SpecialDirectory.CURRENT.value:
            # no action required
            return
        else:
            if target_dir.startswith(SpecialDirectory.HOME.value):
                dest_path = Path(target_dir).expanduser()
            else:
              dest_path = cwd.joinpath(target_dir)

            if self._can_change_directory(dest_path):
                self._shell.set_cwd(dest_path)

    def _can_change_directory(self, dest_path: Path) -> bool:
        if not dest_path.exists():
            print(f"cd: {dest_path}: No such file or directory")
            return False

        if not dest_path.is_dir():
            print(f"cd: {dest_path}: Not a directory")
            return False

        if not os.access(dest_path, os.X_OK):
            print(f"cd: {dest_path}: Permission denied")
            return False

        return True
