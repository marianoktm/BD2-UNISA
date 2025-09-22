from flask import Blueprint, render_template, request
from config.config import get_databases

borrowBlueprint = Blueprint("borrowBooks", __name__)


@borrowBlueprint.get("/borrow_books")
def borrow_books():
    databases = get_databases()
    books_cursor = databases['books'].find({"copy": {"$gt": 0}})

    books = list(books_cursor)

    pagetitle = "Prestito Libri"

    return render_template('borrow_books.html',books=books, pagetitle=pagetitle)

@borrowBlueprint.post("/borrow_books")
def handler_borrow_books():
    lista_scelte = request.form.getlist("scelte")
    print(lista_scelte)

