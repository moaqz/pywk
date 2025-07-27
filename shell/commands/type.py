from commands.builtins import BuiltInCommands
from utils.find_command import find_command, CommandNotFound


def command_type(args: list[str]):
    if not args:
        return

    for cmd in args:
        try:
            BuiltInCommands(cmd)
            print(f"{cmd} is a shell builtin")
        except ValueError:
            try:
                command_path = find_command(cmd)
                print(f"{cmd} is {command_path}")
            except CommandNotFound:
                print(f"type: {cmd}: not found")
