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
    """ Method for App login. It will show login page or redirect to hydration
    page if user logged
    """
    if request.method == 'POST':
        # get the typed username in the username form field
        current_user_name = request.form['username']
        user_password = request.form['password']
        if not current_user_name:
            return render_template("login.html")

        # store previous username to app sessions. If the web browser is closed
        # sessions are removed
        session['user'] = current_user_name

        # relative path to the method. If the method is in another module, use
        # "blueprint_name.method_name" to call required path
        return redirect(url_for("hydration_protocol.hydration_protocol_app", current_user=session['user']))

    if 'user' in session:
        return redirect(url_for("hydration_protocol.hydration_protocol_app", current_user=session['user']))

    return render_template("login.html")


@bp_login.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the current user from the session if it's there and redirect to
    # the login page for a new user logging.
    session.pop('user', None)
    return redirect(url_for('login.login'))
