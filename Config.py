from pathlib import Path

class Config:
    """
    Manages values defined in the config
    """
    @staticmethod
    def get_archives_path() -> Path:
        """
        Returns the path to where archives are stored
        """
        return Path("/home/fcorp/Downloads/") # TODO Fix