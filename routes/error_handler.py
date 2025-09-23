from flask import Blueprint, render_template, request
from db.DatabaseSingleton import get_databases

error_blueprint = Blueprint("error", __name__)

@error_blueprint.errorhandler(Exception)
def handle_exception(e):
    return render_template("generic_error.html", error=e), 500