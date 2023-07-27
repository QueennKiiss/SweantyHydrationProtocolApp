"""
Backend for hydration protocol page
"""

from flask import request
from flask import Blueprint
from flask import session
from flask import render_template

from database.ddbb_local_manager import LocalDBManager


bp_hydration = Blueprint(
    "hydration_protocol", 
    __name__,
    static_folder='static',
    template_folder='templates'
    )

LOCAL_DB = '/home/mmaestro/SWProjects/personal_projects/SweantyHydrationProtocolApp/database/suplement_db.csv'


@bp_hydration.route("/")
@bp_hydration.route("/user", methods=['GET', 'POST'])
def hydration_protocol_app():
    """ Funtion for /hydration/ or /hydration/user endpoints """
    db_manager = LocalDBManager()
    db_manager.read_data_from_db(LOCAL_DB)
    # supplement_list = db_manager.get_filtered_content(TYPE='Beguda')
    whole_supplement_list = db_manager.get_all_db_content()
    current_user_name = session['user']
    print(current_user_name)
    return render_template(
        "hydration_protocol.html",
        current_user=current_user_name,
        supplement_list=whole_supplement_list)


@bp_hydration.route("/user/items", methods=['POST'])
def hydration_protocol_items():
    """ Funtion for /hydration/user/items endpoint """
    db_manager = LocalDBManager()
    db_manager.read_data_from_db(LOCAL_DB)
    whole_supplement_list = db_manager.get_all_db_content()
    # supplement_list = db_manager.get_filtered_content(TYPE='Beguda')
    selected_item = request.form['supplement-list']
    print(selected_item)
    return render_template(
        "hydration_protocol.html",
        current_user="user",
        supplement_list=whole_supplement_list,
        selected_item=selected_item
        )
