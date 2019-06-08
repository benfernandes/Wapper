from datetime import datetime
from pathlib import Path

from file_io import FileIo
from parser import Parser

if __name__ == '__main__':
    rows = FileIo().read_file(Path('./ignore/examples/_chat.txt'))
    json_data = Parser().parse(rows)
    dt = datetime(2019, 5, 11, 15, 37, 39)
    print(dt)
