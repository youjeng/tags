# Tags - A silly little Python webapp for CodePlatoon git classes

The tags webapp lists tags and stores more tags.

It displays an image based on info in a config file.

It knows about development, uat, and production environments.

It uses a SQLite database.

It uses a primitive (and rather obsolete) ORM called [Flask-Orator](https://github.com/sdispater/flask-orator).

This app is so barebones and unfinished that it begs for changes.  Using git, you will collaborate with your team to make it better.

## Environment assumptions

- You have a Python3 installed that is recent enough to have the "-m" option for configuring virtual environments.

- You have a [GitHub](https://github.com) account.

## Set up and run the webapp

Fork the Tags repo from https://github.com/walquis/tags.

Run these commands in a Terminal session:
```bash
$ cd # Start from your home directory
$ mkdir src; cd src  # Or cd to wherever you keep code projects
$ git clone https://github.com/<yourlogin>/tags # Clone your fork
# Or use ssh protocol...  $ git clone git@github.com:<yourlogin>/tags
$ cd tags
$ mkdir ../shared  # In case you want to share config across releases
$ cp config.yml.sample ../shared/config.yml
$ python3 -m venv venv  # Make a virtual env in the "venv" directory
$ source venv/bin/activate  # Enter your virtual env
$ pip install -r requirements.txt  # Populate current virtual env with packages
$ python bin/load_schema.py   # Init your DB structure. Assumes FLASK_ENV=development
$ python bin/seed.py   # Add data to your DB.  Assumes FLASK_ENV=development
$ bin/run-flask-webserver.py  # Assumes FLASK_ENV=development
```
Now visit http://localhost:5555 in your browser.
