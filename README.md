# Flask Set Up

# TODO

- fix issue with .flaskenv
- write scripts to auto handle db migrations
- add cli command for common cases
- add setup script for project case

# Installation

- Clone the repository
- rename all instances of project_name, with your desired project name
- rename app_1 and all it's instances
- add more apps and register it's blueprint as well.
- this setup used postgres config, but you can update the url and corresponding variables to one of your choice.
- create a .env file and add the following variables to it.
    - FLASK_APP=wsgi.py
    - FLASK_DEBUG=False
    - ENV="development"
    - SECRET_KEY=""
    - MAIL_SERVER=""
    - MAIL_USERNAME=""
    - MAIL_PASSWORD=""
    - MAIL_DEFAULT_SENDER=""
    - MAIL_USE_TLS=""
    - MAIL_USE_SSL=""
    - DATABASE_USER=""
    - DATABASE_NAME=""
    - DATABASE_PASSWORD=""
- run `export FLASK_APP=uwsgi.py`
- run `flask run`

###To migrate database

- `flask run db init`
- `flask run db migrate`
- `flask run db upgrade`  

# Known Bugs

- .flaskenv doesn't seem to have any effect whatsoever, hence we still have to export FLASK_APP env.
