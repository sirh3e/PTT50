from enum import Enum

class Ringing(Enum):
    IsNot = "1",
    Is = "0"

def read_from_file_is_not_ringing(path):
    return read_file_first_line(path) == Ringing.IsNot

def read_file_first_line(path):
    with open(path, "r") as file:
       return file.readline(1)

def write_is_not_ringing(path):
    write_into_file(path, Ringing.IsNot)

def write_is_ringing(path):
    write_into_file(path, Ringing.Is)

def write_into_file(path, mode):
    with open(path, "w") as file:
        file.write(mode)
        file.flush()