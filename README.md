# Jabberwocky Repo

These are servers that host container archives for students to install for their coursework. They allow for a list of archives to be obtained as well as download an archive of the users choice. Also, after being authenticated with a username and password, users can upload a container to the server.

## How to Start

```sh
# Only need to run first time
git clone https://github.com/Kippiii/jabberwocky-repo
cd jabberwocky-repo
poetry install

poetry shell
flask --app main run
```

> :warning: **If you want to allow user uploads**, please fill in your own authentication algorithm in `Auth.py::auth`.