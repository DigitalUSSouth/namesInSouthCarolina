pipenv run names_of_sc/manage.py dumpdata --exclude=auth --exclude=contenttypes --exclude=admin --exclude=sessions > dump.json
mv dump.json names_of_sc/frontend/fixtures/
