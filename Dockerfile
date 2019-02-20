#*******************************************************************************
# Names Of South Carolina Site Dockerfile
# Author: Judson James
# Purpose: Dockerfile for Names of South Carolina website
#*******************************************************************************

# Base installation for OS and stuff
FROM ubuntu:18.04
FROM python:3

# Install Ubuntu Package Libraries
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove && \
    apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim

# Project Files and Settings
WORKDIR /var/www
# RUN git clone https://github.com/DigitalUSSouth/namesInSouthCarolina
ADD . /var/www/namesInSouthCarolina
RUN pip install -U pipenv
WORKDIR /var/www/namesInSouthCarolina

# Pipenv management
RUN pipenv lock
RUN pipenv sync
RUN pipenv run names_of_sc/manage.py migrate
RUN pipenv run names_of_sc/manage.py loaddata \ 
                names_of_sc/frontend/fixtures/dump.json

# Runs the actual Django Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["pipenv", "run", "names_of_sc/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
