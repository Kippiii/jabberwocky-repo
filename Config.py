import json
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
        with open(str(Path(__file__).parent / "config.json")) as file:
            config = json.load(file)
            if "archives_path" not in config:
                raise ValueError("archives_path not in config.json")
            return Path(config['archives_path'])
