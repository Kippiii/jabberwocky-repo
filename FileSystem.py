import tarfile
from typing import List
from os import listdir
from pathlib import Path

from Config import Config

class FileSystem:
    """
    Manages the file system of the repo
    """
    @staticmethod
    def get_archives() -> List[str]:
        """
        Gets a list of all of the archives on the server
        """
        archives_path: Path = Config.get_archives_path()
        files: List[str] = listdir(str(archives_path))
        return list(filter(lambda x : FileSystem.is_archive(archives_path / x), files))

    @staticmethod
    def is_archive(path: Path) -> List[str]:
        """
        Determines if a path points to an archive
        """
        if not path.is_file():
            return False
        return tarfile.is_tarfile(str(path))
