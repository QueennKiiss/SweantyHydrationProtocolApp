"""
Main module to be executed when deployment.

Manually, it can be executed with:
 
    -flask --app app run --debug
"""

from flask import Flask

from login.login import bp_login
from hydration.hydration_procotol import bp_hydration


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# To use a static folder located in other app section, the blueprint needs to have
# and url_prefix. If the blueprint does not have an url_prefix, it is not
# possible to access the blueprint’s static folder.
app.register_blueprint(bp_login, url_prefix='/login')
app.register_blueprint(bp_hydration, url_prefix='/hydration')

# Makes url_for('/') == url_for('login.index')
# app.add_url_rule() associates the endpoint name with the / url.
# Since the first "/" url is intended to point to the login method in login
# blueprint, the endpoint should be module.method.
app.add_url_rule("/", endpoint="login.login")

# CLI command: flask --app app run --debug
# Python command: app.run(debug=True)
# The main difference from the CLI command is that the server will crash if
# there are errors when reloading. debug=True can be passed to enable debug mode.
# app.run(debug=True)
