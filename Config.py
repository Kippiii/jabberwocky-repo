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

    @staticmethod
    def set_archives_path(path: Path) -> None:
        """
        Set the path where archives are stored
        """
        with open(str(Path(__file__).parent / "config.json")) as file:
            config = json.load(file)
        config["archives_path"] = str(path)
        with open(str(Path(__file__).parent / "config.json"), "w") as file:
            json.dump(config, file)
