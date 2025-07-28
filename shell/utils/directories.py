from enum import Enum

class SpecialDirectory(Enum):
    PARENT = ".."
    CURRENT = "."
    HOME = "~"
