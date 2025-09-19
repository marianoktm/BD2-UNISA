from flask import Blueprint, render_template
from config.config import get_databases

listBlueprint = Blueprint("list", __name__)

@listBlueprint.route("/list")
def list():

    databases = get_databases()
    books = databases['books'].find()
    name_books = [books['title'] for books in books]
    print(name_books) #debug



    return render_template("list.html", name_books=name_books)

