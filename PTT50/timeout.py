from enum import Enum

class Timeout(Enum):
    NotAny = 0.0
    Short = 0.01
    Long = 0.02
