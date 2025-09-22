from flask import Blueprint, render_template
from config.config import get_databases

listBlueprint = Blueprint("list", __name__)


@listBlueprint.get("/list")
def my_list():
    databases = get_databases()
    books_cursor = databases['books'].find()

    books = list(books_cursor)
    for book in books:
        print(book)  # debug

    return render_template("list.html", books=books)
