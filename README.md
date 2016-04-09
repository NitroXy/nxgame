# NXGame

## Initial setup

### install and configure postgresql
    sudo apt-get install postgresql-9.3
    in /etc/postgresql/9.3/main/pg_hba.conf:
    change
    local   all             all                                     peer
    to
    local   all             all                                     md5

    Create user and database as specified in your settings.py


### Set up the python environment and packages
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

## Running

    (if not already running under virtualenv)
    source venv/bin/activate

    python manage.py runserver
