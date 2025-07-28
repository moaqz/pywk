import os

def command_pwd(args: list[str]):
  if len(args) > 1:
    print("pwd: too many arguments")
    return
  
  cwd = os.getcwd()
  print(cwd)
  
