from enum import Enum

class Ringing(Enum):
    IsNot = "1",
    Is = "0"

def write_is_not_ringing(path):
    write_into_file(path, Ringing.IsNot)

def write_is_ringing(path):
    write_into_file(path, Ringing.Is)

def write_into_file(path, mode):
    with open(path, "w") as file:
        file.write(mode)
        file.flush()