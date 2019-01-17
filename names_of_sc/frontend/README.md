## Frontend App Folder
- This folder contains everything that the client-side will see
  - HTML Files are held within the "templates" folder
    - Templates are separated in two folders: base and filler
      - bases are used for parent-child relationships in HTML templates
      - filler is used to fill-in the blocks in the base templates
  - CSS, JavaScript, and Images are held in the static folder and are
    placed in their corresponding folders.
  - The Models (Django's way of handling tables) are held in the models folder
    - Django uses an object-oriented approach to databases by using Python
      objects to reference the database in a sanitized fashion, without need
      for raw SQL queries.
  - View Controllers are held within the views folder.
  - URLs that are listed within the app are listed in urls.py, each of which
    point to a corresponding view controller.
