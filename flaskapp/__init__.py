"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import flaskapp.views

print('We start off in:', __name__)
if __name__ == '__main__': # = app or __main__
    app.run(debug=True)
    print('We end up in:', __name__)