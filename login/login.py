"""
Backend for login page
"""

from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for


bp = Blueprint("login", __name__, static_folder='static', template_folder='templates')


@bp.route("/", methods=['POST', 'GET'])
@bp.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(f"POST: {request.method}")
        user = request.form["username"]
        # relative path to the method. If the method is in another module, use
        # "blueprint_name.method_name" to call required path
        return redirect(url_for("hydration_protocol.hydration_protocol_app"))
    else:
        print(f"GET: {request.method}")
        return render_template("login.html")
