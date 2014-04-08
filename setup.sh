#!/bin/bash
# Simple setup.sh for configuring Ubuntu 12.04 LTS EC2 instance

sudo apt-get install -y git
git config --global user.name 'RupayanB'
git config --global user.email basu.rupayan@gmail.com
git clone https://github.com/RupayanB/allergyworld.git

sudo apt-get install python-pip
pip install Django==1.6.2
pip install django-csvimport
pip install django-bootstrap-pagination


# setup django
# chmod 744 manage.py
# ./manage.py syncdb
# ./manage.py csvimport --mappings='' --model='allergyworld.Restaurant' restaurants_coord.csv
# ./manage.py runserver inet_ip:port