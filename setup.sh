#!/bin/bash
# Simple setup.sh for configuring Ubuntu 12.04 LTS EC2 instance

sudo apt-get install -y git
sudo apt-get install python-pip
pip install Django==1.6.2
pip install django-csvimport

# Use manage.py csvimport --mappings='' --model='app_label.model_name' importfile.csv