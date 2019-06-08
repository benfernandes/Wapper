from pathlib import Path
from typing import List


class FileIo:
    @staticmethod
    def read_file(file_path: Path) -> List[str]:
        with file_path.open(newline='') as file:
            rows = file.read().splitlines()

        return rows
