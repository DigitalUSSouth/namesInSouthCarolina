# Names of SC
## A website that tells the stories of odd names in SC

### Instructions for Various Issues
- Rather than relying on traditional Python Virtual Environments (venv), we
  chose to go with what the Python organization is pushing towards, Pipenv.
  - Pipenv works as a virtual environment for Pip itself, so pip3 is a mandatory
    package to run this application.
    - You can test this by running
      `pip3`
  - The Pipfile used for this project is running Python 3.7, so be sure to have
    a working version.
    - You can test this by running
      `python3.7`

- To configure Pipenv for your device and run the test server, there needs to
  be a few commands executed for accuracy.

- First, run
  ```
  pipenv sync
  ```
  This will ensure that your Pipfile is updated and is ready for your system.

- To run the Django application after syncing your Pipfile
  ```
  pipenv run names_of_sc/manage.py migrate
  pipenv run names_of_sc/manage.py runserver
  ```
  - This migrates the local db (will not use sqlite3 in production) for local
    testing as well as starts the built-in Django test server.
  - At this point, go to your web browser and go to [localhost](https://localhost:8000)
  - You should see the current working version, and can modify the
    templates and static files to get responses. Be wary that modifying the
    views folder can disrupt the running webserver and crash the application.
    In this case, reload the application by entering `Ctrl+C` and running
    ```
    pipenv run names_of_sc/manage.py runserver
    ```
    
