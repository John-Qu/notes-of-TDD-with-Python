Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    |         ├── bin etc
    |              ├── python, gunicorn, pip etc
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
---
# For stating site

fab deploy:host=johnqu@superlists-staging.grapegraph.com

export SITENAME=superlists-staging.grapegraph.com DJANGO_DEBUG_FALSE=y DJANGO_SECRET_KEY=secret_key

echo $SITENAME

./virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging.grapegraph.com.socket  superlists.wsgi:application

./virtualenv/bin/gunicorn --bind unix:/tmp/$SITENAME.socket  superlists.wsgi:application

sudo systemctl daemon-reload

sudo systemctl enable gunicorn-superlists-staging.grapegraph.com

sudo systemctl start gunicorn-superlists-staging.grapegraph.com

sudo systemctl status gunicorn-superlists-staging.grapegraph.com

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/superlists-staging.grapegraph.com/g" \
    | sudo tee /etc/nginx/sites-available/superlists-staging.grapegraph.com

sudo ln -s /etc/nginx/sites-available/superlists-staging.grapegraph.com \
    /etc/nginx/sites-enabled/superlists-staging.grapegraph.com

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/superlists-staging.grapegraph.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-superlists-staging.grapegraph.com.service

export DJANGO_DEBUG_FALSE=y SITENAME=superlists-staging.grapegraph.com DJANGO_SECRET_KEY=not_so_secret

echo $DJANGO_SECRET_KEY

---

## For Production

DNS the domain name on server control panel.

### On local term:

fab deploy:host=johnqu@superlists.grapegraph.com

### On server term

cd ~/sites/superlists.grapegraph.com/

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/superlists.grapegraph.com/g" \
    | sudo tee /etc/nginx/sites-available/superlists.grapegraph.com

sudo ln -s /etc/nginx/sites-available/superlists.grapegraph.com \
    /etc/nginx/sites-enabled/superlists.grapegraph.com

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/superlists.grapegraph.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-superlists.grapegraph.com.service

sudo systemctl daemon-reload

sudo /etc/init.d/nginx reload

sudo systemctl enable gunicorn-superlists.grapegraph.com

sudo systemctl start gunicorn-superlists.grapegraph.com

### On local term

STAGING_SERVER=superlists.grapegraph.com python manage.py test functional_tests

### For checking status

sudo systemctl status gunicorn-superlists.grapegraph.com

./virtualenv/bin/gunicorn --bind unix:/tmp/superlists.grapegraph.com.socket  superlists.wsgi:application

sudo vi /etc/nginx/sites-available/superlists.grapegraph.com

sudo vi /etc/systemd/system/gunicorn-superlists.grapegraph.com.service

---
