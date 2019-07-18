# Generates Flask app at ./apps/<project_name>/app.py

import textwrap

class FlaskApp(object):
    
    APP_BASE = textwrap.dedent(
    """
    from flask import Flask
    from apis import api

    app = Flask(__name__)
    api.init_app(app)

    app.run(debug=True)
    """ )

    def __init__(self, path):
        self.path = path
        self.app_base = FlaskApp.APP_BASE
        
    def create_file(self):
        new_file = open(self.path + '/app.py', 'a')
        new_file.write(self.app_base.strip())
        new_file.close()

        print('SUCCESS: Flask main file created.')


    