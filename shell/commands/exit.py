from commands.command import Command
import sys

class ExitCommand(Command):
  def execute(self, args: list[str]):
    total_args = len(args)

    if total_args == 0:
      sys.exit(0)

    if total_args > 1:
      print("exit: too many arguments")
      return
    
    sys.exit(args[0])
