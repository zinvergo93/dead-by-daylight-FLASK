To run server:

1. In your terminal, navigate to the correct folder with "cd dead_by_daylight_server_flask"

2. Enter pypi environment in your terminal with "pipenv shell"

   - please install all necessary dependencies listed in the Pipfile.
     - In your terminal, type "pipenv install", then run the script.

3. Enter a python repl by typing "python" in your terminal.

4. Once you see ">>>" type "from app import db"

5. Next command is "db.create_all()". If you don't get an error, you should get a new repl line back, and an app.sqlite file should appear in your folder.

6. Exit the repl with Ctrl/Cmd + Z

7. Once successful, you can enter the server by running the file. In your terminal, type "python app.py"
