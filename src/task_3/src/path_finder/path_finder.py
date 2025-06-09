from pathlib import Path
from src.color_log.color_log import log_folder, log_file, log_error

"""
Path finder module

This module is used to find all files and folders in a given path.

It will log the path in a tree structure.

- blue color for folders
- yellow color for files
"""

def path_finder(pathFolder: str, lvl: int = 0):
  path = Path(pathFolder)

  if not path.exists():
    log_error(f"Path {pathFolder} does not exist")
    return

  pathFiles = path.glob('*')

  for file in pathFiles:
    space = ""
    if lvl > 0:
      space = " " * (2 * lvl)

    if file.is_file():
      if file.parent.is_dir() and lvl > 0:
        log_file(space + "|_ " + file.name)
      else:
        log_file(space + file.name)
    elif file.is_dir():
      if lvl > 0:
        log_folder(space + "|_ " + file.name)
      else:
        log_folder(space + file.name)
      path_finder(file, lvl + 1)
