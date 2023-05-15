"""
Backend for login page
"""

from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session


bp_login = Blueprint("login", __name__, static_folder='static', template_folder='templates')


@bp_login.route("/", methods=['POST', 'GET'])
def login():
    # if 'username' in session:
    #     return f'Logged in as {session["username"]}'
    if request.method == 'POST':
        # session['username'] = request.form["username"]
        # relative path to the method. If the method is in another module, use
        # "blueprint_name.method_name" to call required path
        return redirect(url_for("hydration_protocol.hydration_protocol_app"))
    else:
        return render_template("login.html")


# @bp_login.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('login'))
