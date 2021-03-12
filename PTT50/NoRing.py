#!/usr/bin/python3
from config import Config
from utilities import write_is_not_ringing

def main():
    write_is_not_ringing(Config.RING_FILE_PATH)

if __name__ == '__main__':
    main()
