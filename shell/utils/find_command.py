import os
from pathlib import Path
from typing import List

class CommandNotFound(Exception):
    pass

def expand_path() -> List[str]:
    path = os.getenv("PATH")
    if not path:
        return []
    
    path = path.strip()
    if path == "":
        return []
    
    return path.split(":")

def find_command(cmd: str):
  for directory in expand_path():
      dir_path = Path(directory)

      if not dir_path.exists():
          continue
      
      cmd_path = dir_path.joinpath(dir_path, cmd)
      if cmd_path.exists() and os.access(cmd_path, os.X_OK):
          return str(cmd_path)
      
  raise CommandNotFound(f"Command '{cmd}' not found in PATH")      
