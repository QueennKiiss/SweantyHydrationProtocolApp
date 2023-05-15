"""
Backend for hydration protocol page
"""

from flask import request
from flask import Blueprint
from flask import render_template


bp_hydration = Blueprint("hydration_protocol", __name__, static_folder='static', template_folder='templates')


@bp_hydration.route("/", methods=['GET', 'POST'])
def hydration_protocol_app():
    return render_template("hydration_protocol.html")
