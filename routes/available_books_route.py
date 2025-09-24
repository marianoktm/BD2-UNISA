from flask import Blueprint, render_template
from db.DatabaseSingleton import get_databases

availableBlueprint = Blueprint('availableBooks', __name__)


@availableBlueprint.get('/available_books')
def available_books():

    databases = get_databases()
    books_cursor = databases['books'].find({"copy": {"$gt": 0}})

    books = list(books_cursor)

    pagetitle = "Lista dei Libri Disponibili"

    return render_template('new/list.html', books=books, pagetitle=pagetitle)