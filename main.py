from flask import Flask, abort, send_file

from FileSystem import FileSystem
from Config import Config

app = Flask(__name__)

@app.route("/")
def get_file_list():
    return {
        "archives": FileSystem.get_archives(),
    }

@app.route("/get/<archive_name>")
def get_archive_by_name(archive_name: str):
    archives: List[str] = FileSystem.get_archives()
    if archive_name not in archives:
        abort(404)
    return send_file(Config.get_archives_path() / archive_name)
