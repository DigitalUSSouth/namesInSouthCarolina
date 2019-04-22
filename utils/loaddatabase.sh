#!/bin/sh
#******************************************************************************
# Author:  Judson James
# Purpose: Simplicity command to load the database with a Django fixture in
#          json format.
#******************************************************************************
docker exec names_django python3 manage.py loaddata frontend/fixtures/dump.json