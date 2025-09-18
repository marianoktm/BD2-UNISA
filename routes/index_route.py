from flask import Blueprint, render_template

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    return render_template('index.html')
