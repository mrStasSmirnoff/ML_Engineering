import markdown
import os
from flask import Flask, g 
import shelve

# Create an instance fo Flask
app = Flask(__name__)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = shelve.open("devices.db")
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route("/")
def index():
    """Present some documentation"""

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        #Read the content of the file
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

class DeviceList():
    
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])
        
        return {'message': 'Success', 'data': devices}
