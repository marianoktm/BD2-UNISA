from flask import Blueprint, render_template
from db.DatabaseSingleton import get_databases

listBlueprint = Blueprint("list", __name__)


@listBlueprint.get("/list")
def my_list():
    databases = get_databases()
    books_cursor = databases['books'].find()

    books = list(books_cursor)
    for book in books:
        print(book)  # debug

    pagetitle = "Lista dei Libri"

    return render_template("new/list.html", pagetitle=pagetitle, books=books)
