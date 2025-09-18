from flask import Blueprint, render_template, request

formBlueprint = Blueprint("form", __name__)


@formBlueprint.post("/form")
def form():
    name = request.form.get("name")
    age = request.form.get("age")
    return render_template("post_result.html", name=name, age=age)
