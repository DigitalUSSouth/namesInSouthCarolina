#!/bin/sh
#******************************************************************************
# Author:  Judson James
# Purpose: Simplicity command to dump the database with a Django fixture in
#          json format.
#******************************************************************************
docker exec names_django python3 manage.py dumpdata --exclude=auth --exclude=contenttypes \
        --exclude=admin --exclude=sessions > dump.json
mv dump.json names_of_sc/frontend/fixtures/
