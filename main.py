from flask import Flask

from FileSystem import FileSystem

app = Flask(__name__)

@app.route("/")
def get_file_list():
    return {
        "archives": FileSystem.get_archives(),
    }