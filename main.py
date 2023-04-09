from flask import Flask, abort, send_file, request
from werkzeug.utils import secure_filename
import click
from pathlib import Path
import logging

from FileSystem import FileSystem
from Config import Config
from Auth import auth

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_file_list():
    return {
        "archives": FileSystem.get_archives(),
    }

@app.route("/get/<archive_name>", methods=['GET'])
def get_archive_by_name(archive_name: str):
    archives: List[str] = FileSystem.get_archives()
    if archive_name not in archives:
        abort(404)
    return send_file(Config.get_archives_path() / archive_name)

@app.route("/put", methods=['POST'])
def put_archive():
    if "username" not in request.form or "password" not in request.form:
        abort(400)
    username: str = request.form['username']
    password: str = request.form['password']
    if not auth(username, password):
        abort(401)
    if "file" not in request.files or not request.files['file']:
        abort(400)
    file = request.files['file']
    filename: str = secure_filename(file.filename)
    if filename in FileSystem.get_archives():
        abort(409)
    file.save(str(Config.get_archives_path() / filename))
    return "Success!"

@app.cli.command("set-path")
@click.argument("path")
def set_path(path: str) -> None:
    Config.set_archives_path(Path(path))
